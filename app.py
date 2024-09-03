from flask import Flask, render_template, request, redirect, url_for
import navegation as navy

app = Flask(__name__)

def function_one():
    print("Function One Executed")
    return "Function One Executed"

def function_two():
    print("Function Two Executed")
    return "Function Two Executed"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    if request.method == 'POST':
        if request.form['action'] == 'Navegacao':
            result = navy.map()
        elif request.form['action'] == 'Function Two':
            result = function_two()
        return render_template('index.html', result=result)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
