import requests
import json
import urllib.parse
import os

with open('shoppingList.js', 'r') as file:
    js_code = file.read()

shopping_list = []
exec(js_code, globals(), {'shoppingList': shopping_list})

openai_api_key = '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'

google_api_key = 'YOUR_GOOGLE_API_KEY'
google_search_engine_id = 'YOUR_GOOGLE_SEARCH_ENGINE_ID'

ingredients = shopping_list

openai_url = 'https://api.openai.com/v1/engines/davinci-codex/completions'

def generate_recipe_page(recipe, image_url):
    html_content = f'''
    <!DOCTYPE html>
    <html>
      <head>
        <style>
          body {{
            background-image: url({image_url});
            background-size: cover;
            background-position: center;
            font-family: Arial, sans-serif;
          }}

          .container {{
            max-width: 600px;
            margin: 0 auto;
            padding: 40px;
            background-color: rgba(255, 255, 255, 0.8);
          }}

          h1 {{
            font-size: 28px;
            margin-bottom: 20px;
          }}

          p {{
            font-size: 18px;
            line-height: 1.5;
            margin-bottom: 10px;
          }}
        </style>
      </head>
      <body>
        <div class="container">
          <h1>Recipe: {recipe['title']}</h1>
          <p>{recipe['description']}</p>
          <h2>Ingredients</h2>
          <ul>
            {''.join(f'<li>{ingredient}</li>' for ingredient in recipe['ingredients'])}
          </ul>
          <h2>Instructions</h2>
          <ol>
            {''.join(f'<li>{instruction}</li>' for instruction in recipe['instructions'])}
          </ol>
        </div>
      </body>
    </html>
    '''
    return html_content


def save_html_to_file(html_content):
    with open('recipe.html', 'w') as file:
        file.write(html_content)
    print('Recipe page generated successfully!')


def search_recipe_image(recipe):
    query = f"{recipe['title']} recipe"
    query = urllib.parse.quote(query)
    url = f"https://www.googleapis.com/customsearch/v1?key={google_api_key}&cx={google_search_engine_id}&q={query}&searchType=image"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = json.loads(response.text)
        image_url = data['items'][0]['link']
        html_content = generate_recipe_page(recipe, image_url)
        save_html_to_file(html_content)
    except requests.exceptions.RequestException as error:
        print('Error searching for recipe image:', error)
    except (KeyError, IndexError) as error:
        print('Error retrieving image URL:', error)


def generate_recipe():
    headers = {
        'Authorization': f'Bearer {openai_api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'prompt': f"Given the ingredients {ingredients}, provide a recipe.",
        'max_tokens': 200,
        'temperature': 0.7,
        'n': 1,
        'stop': 'Instructions:'
    }

    try:
        response = requests.post(openai_url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        recipe_text = response.json()['choices'][0]['text'].strip()
        recipe = {
            'title': 'Delicious Recipe',
            'description': 'A tasty recipe created just for you!',
            'ingredients': ingredients,
            'instructions': [instruction.strip() for instruction in recipe_text.split('\n')]
        }
        search_recipe_image(recipe)
    except requests.exceptions.RequestException as error:
        print('Error generating recipe:', error)
    except (KeyError, IndexError) as error:
        print('Error parsing recipe response:', error)

generate_recipe()
