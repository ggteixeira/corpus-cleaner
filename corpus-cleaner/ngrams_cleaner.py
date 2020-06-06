# Abre o arquivo com os n-gramas:
with open("ngrams_terminet/ngrams.txt", "r") as file:
    file = file.read()

# Abre o arquivo com as stopwords
with open("stopwords/my_stopwords.txt", "r") as stopwords:
    stopwords = stopwords.read()


def str_2_list(text_file):
    """Converte os itens do arquivo de n-gramas em uma lista
    """
    converted_2_list = text_file.split("\n")  # Transforma os itens em uma lista
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

    # filtered_ngrams = list()
    blacklist = list()
    blacklist_without_duplicates = list()

    for ngram in ngram_list:  # para cada n-grama
        for stopword in stopwords_list:  # p/ cada stopword na lista stopwords
            if stopword in ngram:  # se o n-grama contém a stopword

                blacklist.append(ngram)  # adiciona o n-grama à blacklist

    for i in blacklist:  # p/ cada item na blacklist
        if i not in blacklist_without_duplicates:  # se b_w_dplctes ñ contém i
            blacklist_without_duplicates.append(i)  # add i à lista

    with open("saida_ngrams.txt", "w+") as saida:  # abre o arquivo de saída
        for ngram in ngram_list:  # p/ cada n-grama na lista
            if ngram not in blacklist_without_duplicates:  # se blk_w_dplct ñ contém ngram
                saida.write(f"{ngram}\n")  # escreve o n-grama no arquivo e vai pra próxima linha

# Function call:
filter_ngrams(list_2_set(str_2_list(file)), stopwords)
