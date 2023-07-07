import os
import json
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from template import template_string

load_dotenv()
file_path = "../backend/items.json"

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        dict = json.load(file)
else:
    print('File not found.')
    exit()

ingredients = dict.values()

items = []
for i in ingredients:
    items.append(i)

list_str = f"{items}"
prompt_template = ChatPromptTemplate.from_template(template_string)
recipe_prompt = prompt_template.format_messages(list= list_str)

# Call OpenAI 

chat = ChatOpenAI(temperature=0.0)
recipe_str= chat(recipe_prompt)
output_str = recipe_str.content

recipe_dict = json.loads(output_str)

print(recipe_dict)
print(type(recipe_dict))
# recipename = recipe_dict.recipename
# time = recipe_dict.time
# procedure = recipe_dict.procedure

# print(procedure)

