                                      Olá! Meu nome e Luis Miguel.
  Sou um programador que tem 12 anos programando por diversão.
Este meu programa e um pesquisador com opções de pesquisa abrangente ou profunda!
Este projeto e open source e totalmente modificavel. 
      Obrigado!

Primeiramente, tenha em mente que tem o pip3 e o python3 instalado em sua maquina/dispositivo.

🐧 1. Instruções para Linux (Arch Linux, Ubuntu, Fedora, etc.)

No Linux, o script está configurado com suporte nativo a Shebang, permitindo que ele seja executado diretamente pelo terminal como um programa do sistema.

    Abra o seu terminal.

    Navegue até o diretório onde salvou o arquivo Pesquisador_Profundo.py:
    Bash

    cd ~/Downloads

    Forneça permissões de execução para o arquivo:
    Bash

    chmod +x buscador.py

    Execute o programa digitando apenas:
    Bash

    ./buscador.py

🪟 2. Instruções para Windows (CMD ou PowerShell)

No Windows, o interpretador do Python gerencia a execução diretamente através da chamada do arquivo.

    Abra o Prompt de Comando (CMD) ou o PowerShell.

    Vá até a pasta onde o script foi baixado (substitua pelo seu usuário real do Windows):
    DOS

    cd C:\Users\SeuUsuario\Downloads

    Inicie o programa chamando o Python:
    DOS

    python Pesquisador_Profundo.py

💡 Dica de Atalho no Windows: Você também pode simplesmente abrir o gerenciador de arquivos e dar um duplo clique sobre o arquivo buscador.py para rodá-lo instantaneamente.

🤖 3. Instruções para Android (Termux)

O Termux permite transformar seu smartphone em um ambiente de desenvolvimento completo para rodar scripts em Python.

    Abra o aplicativo Termux no seu celular.

    Atualize o sistema e as listas de repositórios:
    Bash

    pkg update && pkg upgrade

    Certifique-se de ter o Python e o Git instalados no Termux:
    Bash

    pkg install python git

    Passo Fundamental: Para permitir que o Python interaja com os aplicativos do seu celular (como abrir o Chrome ou Firefox do Android), instale a API de integração do Termux:
    Bash

    pkg install termux-api

    Navegue até a pasta do arquivo e execute:
    Bash

    python3 Pesquisador_Profundo.py
