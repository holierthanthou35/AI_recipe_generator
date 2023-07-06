import openai

# Load the API key
openai.api_key = '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'

# Function to generate the webpage content
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
    
    # Extract the generated HTML content
    generated_html = response.choices[0].text.strip()
    
    return generated_html

# Read the ingredients from pantry_.js
with open('pantry_.js', 'r') as file:
    ingredients = file.readlines()

# Generate the webpage content
webpage_content = generate_webpage(ingredients)

# Write the content to a new HTML file
with open('generated_webpage.html', 'w') as file:
    file.write(webpage_content)
