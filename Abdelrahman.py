from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"name": "جراب موبايل جلد", "price": "50 جنيه", "img": "https://placehold.co/200x200/orange/white?text=جراب"},
    {"name": "سماعة بلوتوث", "price": "350 جنيه", "img": "https://placehold.co/200x200/blue/white?text=سماعة"},
    {"name": "شاحن سريع 20 وات", "price": "120 جنيه", "img": "https://placehold.co/200x200/green/white?text=شاحن"},
    {"name": "باور بانك 10000", "price": "400 جنيه", "img": "https://placehold.co/200x200/red/white?text=باور+بانك"}
]



@app.route('/')
def home():
     render_template("index."html, products=products)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
    
