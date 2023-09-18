from flask import Flask, render_template, request
import itertools
import datetime

app = Flask(__name__, template_folder='C:\\Users\\Rafael\\Desktop\\Combinações')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar_combinacoes', methods=['POST'])
def gerar_combinacoes():
    cfops = request.form.get('cfops')
    estados_emissor = request.form.get('estado_emissor')
    estados_destinatario = request.form.get('estado_destinatario')
    regime_emissor = request.form.get('regime_emissor')
    regime_destinatario = request.form.get('regime_destinatario')
    linha_emissor = request.form.get('linha_emissor')
    linha_destinatario = request.form.get('linha_destinatario')

    cfops = cfops.split(',')
    estados_emissor = estados_emissor.split(',')
    estados_destinatario = estados_destinatario.split(',')
    regime_emissor = regime_emissor.split(',')
    regime_destinatario = regime_destinatario.split(',')
    linha_emissor = linha_emissor.split(',')
    linha_destinatario = linha_destinatario.split(',')

    todos_critérios = [cfops, estados_emissor, estados_destinatario, regime_emissor, regime_destinatario, linha_emissor, linha_destinatario]

    combinações = list(itertools.product(*todos_critérios))

    resultado = "<h2>Resultado das Combinações:</h2><ul>"
    for combinação in combinações:
        resultado += f"<li>{', '.join(map(str, combinação))}</li>"
    resultado += "</ul>"

    pasta_resultados = 'C:\\Users\\Rafael\\Desktop\\Combinações\\Resultados'
    data_de_hoje = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    nome_do_arquivo = f'{pasta_resultados}\\Resultado_combinacoes_{data_de_hoje}.txt'
    
    with open(nome_do_arquivo, 'w') as arquivo_destino:
        for combinação in combinações:
            arquivo_destino.write(f"{', '.join(map(str, combinação))}\n")

    return resultado

if __name__ == '__main__':
    app.run(debug=True)
