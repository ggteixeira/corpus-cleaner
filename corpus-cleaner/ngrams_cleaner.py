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

    return ngrams_list_of_list

def filter_ngrams(ngram_list, stopwords_list):    
    # Transforma os itens do arquivo de stopwords em uma lista:
    stopwords_list = stopwords_list.split("\n")

    filtered_ngrams = list()
    blacklist = list()
    blacklist_without_duplicates = list()

    for ngram in ngram_list:  # para cada n-grama
            for stopword in stopwords_list:
                if stopword in ngram:

                    blacklist.append(ngram)
                    # filtered_ngrams.append(ngram)
                    # saida.write(f"{ngram}\n")
    # print(f"S T O P W O R D S: \n\n{stopwords_list}")

    for i in blacklist:
        if i not in blacklist_without_duplicates:
            blacklist_without_duplicates.append(i)
    # print(f"stopword_list: {stopwords_list[10:25]} (...)")
    # print(f"ngram_list: {ngram_list}\n\n\n")
    # print(f"Blacklist sem duplicatas: {blacklist_without_duplicates}") 

    with open("saida_ngrams.txt", "w+") as saida:
        for ngram in ngram_list:
            if ngram not in blacklist_without_duplicates:
                saida.write(f"{ngram}\n")

        # for i in blacklist_without_duplicates:
            # saida.write(f"{i}\n")
            # print(f"{i}\n")
# Function call:
print(filter_ngrams(list_2_set(str_2_list(file)), stopwords))