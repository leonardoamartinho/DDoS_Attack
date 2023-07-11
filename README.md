# DDoS_Attack
Projeto de Simulação de Ataque DDoS para a disciplina Redes de Computadores II

- Descrição: Este projeto visa simular um ataque DDoS através da criação de um servidor local com o framework Flask, e da execução ininterrupta de requisições GET em múltiplos hosts dentro da mesma sub-rede. As requisições são executadas continuamente até que o Rate Limit do servidor seja ultrapassado, de modo que o servidor é automaticamente derrubado.

- Arquivos:
1. app.py = Cria o servidor local e contém a lógica para o cálculo de pacotes/segundo.
2. templates/index.html = Página principal do servidor.
3. static/stylesheets/style.css = Arquivo CSS de index.html.
4. static/images/programming.gif = Gif que é visualizado na página principal do servidor.
5. file.pdf = Arquivo PDF que é enviado em cada requisição GET.
6. ataque.py = programa que executa as requisições GET para o ataque.

- Bibliotecas:
1. flask
2. threading
3. os
4. datetime

- Instruções:
1. Execute o programa app.py para levantar o servidor local.
2. Utilize o URL gerado para acessar a página principal no navegador. Caso esteja utilizando o Visual Studio Code, apenas dê Ctrl+click no link gerado.
3. Copie o URL completo e adicione a rota "/return_file". Ex: "http://192.168.68.114:5000/return_file"
4. Cole o URL gerado na variável "url" do programa ataque.py.
5. Execute o programa ataque.py para realizar as requisições ininterruptas.
6. Aguarde o número de requisições por segundo ser alto o bastante para derrubar o servidor. O valor do Rate Limit pode ser alterado dinamicamente na linha 66 do programa app.py.
7. Ao atingir o limite, o servidor será automaticamente desligado, e o programa ataque.py, interrompido.
8. Recarregue a página principal do servidor e receba a mensagem de "Página Não Encontrada" do navegador.
