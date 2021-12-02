
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        formsearch = request.form.get('txtsearch')
        print(formsearch)
    return render_template('index.html')

def sample_sum_func(a = 0, b = 0):
    return a + b

def sample_sub_func(a = 0, b = 0):
    return a - b

if __name__ == '__main__':
    app.run()