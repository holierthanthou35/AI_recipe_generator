from flask import Flask,render_template, request
from rec_logic import wrapper

app = Flask(__name__)

food_items = ['rice','pasta']

@app.route("/",methods=['POST','GET'])
def getitems():
    if request.method == 'POST':
        data = request.form.get('new_item')
        food_items.append(data)
        return render_template('landing_page.html')
    return render_template('landing_page.html')

@app.route("/render-page",methods = ['POST','GET'])
def pantrypage():
    if request.method == 'POST':
        button_value = request.form["button"]
        food_items.append(button_value)
        print(food_items)
        return render_template('index1.html',food_items=food_items)
    return render_template('index1.html',food_items=food_items)

@app.route("/recipe-page",methods=['POST','GET'])
def recipegenrate():
    recipe_dict=wrapper(food_items)
    return recipe_dict['procedure']

if __name__ == '__main__':
    app.run(debug=True)
