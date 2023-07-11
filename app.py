from flask import Flask, render_template, send_file  # Importe os módulos necessários
from threading import Timer  # Importe a classe Timer do módulo threading
import os  # Importe o módulo os para encerrar o servidor
from datetime import datetime, timedelta  # Importe o módulo datetime para cálculos de tempo

app = Flask(__name__)  # Crie uma instância do aplicativo Flask
request_counts = []  # Lista para armazenar os carimbos de data/hora das requisições
window_size = timedelta(seconds=1)  # Defina a janela de tempo para contar as requisições

def update_requests_per_second():
    """
    Função para atualizar a lista de carimbos de data/hora das requisições a cada segundo.
    Ela é chamada repetidamente usando um objeto Timer.
    """
    current_time = datetime.now()  # Obtenha o carimbo de data/hora atual
    request_counts.append(current_time)  # Adicione o carimbo de data/hora atual à lista

    # Remova as requisições antigas da lista
    while request_counts and request_counts[0] <= current_time - window_size:
        request_counts.pop(0)

    # Crie um novo objeto Timer para chamar esta função após 1 segundo
    timer = Timer(1.0, update_requests_per_second)
    timer.daemon = True  # Defina o objeto Timer como um daemon para encerrar quando o programa principal encerrar
    timer.start()  # Inicie o Timer

def count_requests_per_second():
    """
    Função para contar o número de requisições feitas dentro da janela de tempo.
    Ela retorna a contagem de requisições feitas no último segundo.
    """
    current_time = datetime.now()  # Obtenha o carimbo de data/hora atual
    request_counts.append(current_time)  # Adicione o carimbo de data/hora atual à lista

    # Remova as requisições antigas da lista
    while request_counts and request_counts[0] <= current_time - window_size:
        request_counts.pop(0)

    return len(request_counts)  # Retorna a contagem de requisições no último segundo

def shutdown_server():
    """
    Função para encerrar o servidor Flask de forma adequada.
    Ela é chamada quando a contagem de requisições ultrapassa um limite.
    """
    os._exit(1)  # Encerra o programa imediatamente

@app.route('/', methods=["GET", "POST"])
def main():
    """
    Rota Flask para a página principal.
    Ela renderiza o modelo 'index.html' e passa a contagem de requisições para ele.
    """
    count = count_requests_per_second()  # Obtenha a contagem de requisições
    return render_template("index.html", count=count)  # Renderiza o modelo com a contagem

@app.route('/return_file')
def return_file():
    """
    Rota Flask para retornar um arquivo.
    Ela verifica a contagem de requisições e retorna o arquivo se ele existir.
    """
    count = count_requests_per_second()  # Obtenha a contagem de requisições
    try:
        print(count)
        if count >= 160:  # Verifica se a contagem de requisições ultrapassa um limite
            shutdown_server()  # Encerra o servidor

        return send_file('file.pdf')  # Retorna o arquivo 'file.pdf'
    except FileNotFoundError:
        return "File not Found"  # Retorna uma mensagem de erro se o arquivo não for encontrado

if __name__ == "__main__":
    update_requests_per_second()  # Inicia a atualização das contagens de requisições a cada segundo
    app.run(host="0.0.0.0", debug=False)  # Executa o aplicativo Flask no host local