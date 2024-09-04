from flask import Flask, render_template, request, redirect, url_for
import navegation as navy
import detail

app = Flask(__name__)

def navy_mode():
    print("Modo navegação executado")
    destino = "SalaB"
    navy.map(destino)

    return "Modo navegação encerrado"

def detail_mode():
    print("Modo detalhamento executado")
    item = "123"

    detail.solicitar(item)
    detalhes = detail.receber()

    return detalhes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    if request.method == 'POST':
        if request.form['action'] == 'Function One':
            result = navy_mode()
        elif request.form['action'] == 'Function Two':
            result = detail_mode()
        return render_template('index.html', result=result)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
