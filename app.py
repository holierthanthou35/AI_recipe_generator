from flask import Flask,render_template, request

app = Flask(__name__)

food_items = []

@app.route("/",methods=['POST','GET'])
def getitems():
    if request.method == 'POST':
        data = request.form.get('new_item')
        food_items.append(data)
        return render_template('index.html',food_items = food_items)
    return render_template('index.html',food_items=food_items)

if __name__ == '__main__':
    app.run(debug=True)
