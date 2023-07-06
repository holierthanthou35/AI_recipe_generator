import openai

openai.api_key = 'YOUR_API_KEY'

with open('pantry_.js', 'r') as file:
    ingredients = file.readlines()


def generate_webpage(ingredients):
    # Generate the HTML content using OpenAI API
    response = openai.Completion.create(
        engine='davinci',
        prompt=f"<!DOCTYPE html><html><body><h1>Recipe</h1><ul>{''.join(f'<li>{ingredient}</li>' for ingredient in ingredients)}</ul></body></html>",
        max_tokens=200,
        temperature=0.6,
        n=1,
        stop=None,
        timeout=5
    )

    generated_html = response.choices[0].text.strip()
    
    return generated_html


webpage_content = generate_webpage(ingredients)

with open('generated_webpage.html', 'w') as file:
    file.write(webpage_content)
