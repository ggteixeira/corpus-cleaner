# Importação de módulos
import requests
import string
import re
from bs4 import BeautifulSoup
from random import randrange



def get_test_url(default_url='http://hmpg.net/'):
    test_url = input("Digite uma URL: ")
    if len(test_url) == 0:
        return default_url
    else:
        return test_url

# Faz um request da URL e a salva numa variável
def get_page(url=None):
    if url is None:
        return requests.get(get_test_url())
    else:
        url = input()
    return requests.get(url)


# Baixa todo o conteúdo da página referente à URL
def download_page(get_page):
    return get_page.content


# Parseia o HTML, dando uma 'prettifycada' nele.
def html_parse(download_page):
    print(f"Tamanho do texto antes da limpeza: {len(download_page.split())} tokens")
    return BeautifulSoup(download_page, "html.parser")

# Limpa parcialmente o conteúdo, salvando apenas texto presente na página
def html_clean(html_parse):
    return html_parse.findAll(text=True)


# Cria dinamicamente uma lista de tags a serem ignoradas
def set_blacklist(html_clean):
    blacklist = set([token.parent.name for token in html_clean])
    tags_to_be_blacklisted = set(("p", "b", "a" "i"))
    blacklisted_tags = blacklist - tags_to_be_blacklisted

    return blacklisted_tags


# Printa todos os tokens, menos aqueles cujos pais estão na blacklist
def deep_clean(set_blacklist, html_clean):
    output = str()
    for token in html_clean:
        if token.parent.name not in set_blacklist(html_clean):
            output += f"{token }\n"

    # Retira as pontuações do texto
    for token in output:
        if token in string.punctuation:
            output = output.replace(token, "")
        if token == "\n":
            output = output.replace("\n", " ")
    
    print(f"Tamanho limpo? --> {len(output.split())}")
    return output

def write_into_file(deep_clean):
    text_file = open(f'corpora/corpus_{randrange(0, 1000)}.txt', 'w')
    for token in deep_clean:
        text_file.write(token)
    text_file.close()

write_into_file(deep_clean(set_blacklist, html_clean(html_parse(download_page(get_page())))))

