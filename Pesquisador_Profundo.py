#!/usr/bin/env python3
import webbrowser
import urllib.parse
termo = input("O que você quer pesquisar?")
tipo_busca = input("'Abrangente' ou 'Profunda'?").strip().lower()

#PROFUNDA OU ABRANGENTE
if tipo_busca == "profunda":
    termo_profundo = f'"{termo}"'
    
    termo_url = urllib.parse.quote(termo_profundo)
    url = f"https://www.google.com/search?q={termo_url}"
    
    print("Busca profunda...")
    #URL
    webbrowser.open(url)
    
elif tipo_busca == "abrangente":
    termo_formatado = urllib.parse.quote(termo)
    url2 = f"https://www.google.com/search?q={termo_formatado}"
    
    print("Busca abrangente...")
    webbrowser.open(url2)
    
else:
    print("Opção inválida! Por favor digite apenas 'abrangente' ou 'profunda'.")
    
    