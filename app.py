from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    greeting = ""
    if request.method == 'POST':
        name = request.form['name']
        greeting = f"✨ Happy Diwali, {name}! ✨<br>May your life be filled with joy, prosperity, and the light of happiness."
    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)
