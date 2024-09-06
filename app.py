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
def dashboard():
    return render_template('dashboard.html')

# Rota para a página de navegação
@app.route('/navegacao')
def navegacao():
    return render_template('navegacao.html')

# Rota para a página de detalhamento
@app.route('/detalhamento')
def detalhamento():
    return render_template('detalhamento.html')

# Rota para a página de recebimento
@app.route('/recebimento')
def recebimento():
    return render_template('recebimento.html')

# Rota para a página de retirada
@app.route('/retirada')
def retirada():
    return render_template('retirada.html')






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
