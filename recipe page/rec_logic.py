import re
import os
import openai
import json
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()
file_path = 'C:\\Users\\avish\\AI_recipe_generator\\backend\\items.json'

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
else:
    print('File not found.')
    exit()

items = []
for item in data:
    items.append(item)


def create_dish_prompt(list_items):
    prompt = f"""create a detailed recipe with only the following ingredients: {','.join(list_items)}. \n"\
    +f"Start off with 'recipe name', 'time required to cook' 'ingredients list' and 'step-by-step procedure for cooking """
    return prompt


response = openai.Completion.create(
  model="text-davinci-003",
  prompt=create_dish_prompt(items),
  temperature=0.3,
  max_tokens=200,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)


def extract_title(text):
    return re.findall('^.*Recipe Name: .*$', text, re.MULTILINE)[0].strip().split('Recipe Name: ')[-1]

