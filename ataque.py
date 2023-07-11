import requests # Importa o mnódulo para realizar as requisições GET

url = "http://192.168.68.114:5000/return_file"  # URL para a qual as requisições serão feitas
status = 200 # Status da requisição
i = 1  # Variável para contar o número de pacotes enviados
while status == 200:
    response = requests.get(url)  # Envia uma requisição GET para a URL
    print(response.status_code)  # Imprime o código de status da resposta
    print("Packets sent: ", i)  # Imprime o número do pacote
    i += 1  # Incrementa o número de pacotes
    status = response.status_code # Fecha o Loop
