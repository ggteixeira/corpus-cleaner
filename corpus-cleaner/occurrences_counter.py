entrada = open("corpora/corpus_unificado.txt", "r", encoding="utf-8")
saida = open("saida_pt.txt", "w", encoding="utf-8")

lexico = {}
for linha in entrada:
    tokens = linha.strip().split(" ")
    for token in tokens:
        if token.isalpha():
            token = token.lower()
            lexico[token] = lexico.get(token, 0) + 1

for token in sorted(lexico.keys(), key=lexico.get, reverse=True):
    saida.write(token + ": " + str(lexico.get(token)) + "\n")


entrada.close()
saida.close()
