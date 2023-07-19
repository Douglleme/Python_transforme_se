from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        celular = request.form['celular']
        servico = request.form['servico']
        observacoes = request.form['observacoes']

        # Salvar os dados em um banco de dados ou enviar para um sistema de gestão de clientes, etc.
        # Neste exemplo, apenas exibiremos as informações para demonstração.
        return f"<h1>Serviço solicitado com sucesso!</h1><p>Nome: {nome}</p><p>E-mail: {email}</p><p>Serviço: {servico}</p><p>Observações: {observacoes}</p>"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
