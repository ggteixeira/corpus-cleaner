# Importação de módulos
import requests
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
    return BeautifulSoup(download_page, "html.parser")


# Limpa parcialmente o conteúdo, salvando apenas texto presente na página
def html_clean(html_parse):
    return html_parse.findAll(text=True)


# Cria dinamicamente uma lista de tags a serem ignoradas
def set_blacklist(html_clean):
    blacklist = set([token.parent.name for token in html_clean])
    blacklist.remove("p")
    return blacklist


# Printa todos os tokens, menos aqueles cujos pais estão na blacklist
def deep_clean(set_blacklist, html_clean):
    output = str()
    for token in html_clean:
        if token.parent.name not in set_blacklist(html_clean):
            output += f"{token }\n"
    return output

def write_into_file(deep_clean):
    text_file = open(f'corpora/corpus_{randrange(0, 100000)}.txt', 'w')
    for token in deep_clean:
        text_file.write(token)
    text_file.close()


write_into_file(deep_clean(set_blacklist, html_clean(html_parse(download_page(get_page())))))