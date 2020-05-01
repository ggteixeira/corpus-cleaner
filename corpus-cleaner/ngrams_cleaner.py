import re

# Abre o arquivo com os n-gramas:
with open("ngrams_terminet/candidatos_backup/2_gram/N,BugFeature,Spoladore.txt", "r") as file:
    file = file.read()
# Abre o arquivo com as stopwords
with open("stopwords/my_stopwords.txt", "r") as stopwords:
    stopwords = stopwords.read()

def str_2_list(text_file):
    """Converte os itens do arquivo de n-gramas em uma lista
    """
    converted_2_list = text_file.split('\n')  # Transforma os itens em uma lista
    return converted_2_list


def list_2_set(converted_2_list):
    """Coloca cada linha (contendo n-gramas) em uma lista.
    Coloca todas as listas de n-gramas dentro de outra lista.
    Lista de listas
    """
    ngrams_list_of_list = list()
    for ngram in converted_2_list:
        ngrams_list_of_list.append(ngram.split())

    return ngrams_list_of_list[50:55]

def filter_ngrams(ngram_list, stopwords_list):    
    # Transforma os itens do arquivo de stopwords em uma lista:
    
    stopwords_list = stopwords_list.split("\n")
    print(f"Lista original: {ngram_list}")
    nova_lista = list()

    for ngram in ngram_list[:]:
        for gram in ngram:
            for stopword in stopwords_list:
                if gram != stopword:
                    pass
                else:
                    ngram_list.remove(ngram)

    return f"Nova lista: {ngram_list}"


# Function call:
print(filter_ngrams(list_2_set(str_2_list(file)), stopwords))