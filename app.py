
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        formsearch = request.form.get('txtsearch')
        print(formsearch)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()