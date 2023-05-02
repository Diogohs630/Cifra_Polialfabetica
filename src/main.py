def cifra_vigenere(mensagem, chave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    tabela_de_vigenere = []
    for i in range(len(alfabeto)):
        mudando_alfabeto = alfabeto[i:] + alfabeto[:i]
        tabela_de_vigenere.append(mudando_alfabeto)

    chave = chave.lower()
    tamanho_chave = len(chave)
    nova_chave = ''.join([chave[i % tamanho_chave] for i in range(len(mensagem))])

    mensagem_cifrada = ""
    for i in range(len(mensagem)):
        letras_mensagem = mensagem[i].lower()
        chave_caracter = nova_chave[i]
        if letras_mensagem in alfabeto:
            indice_linha = alfabeto.index(chave_caracter)
            indice_coluna = alfabeto.index(letras_mensagem)
            letras_criptografada = tabela_de_vigenere[indice_linha][indice_coluna]
            mensagem_cifrada += letras_criptografada
        else:
            mensagem_cifrada += letras_mensagem

    return mensagem_cifrada

def decifrar_vigenere(palavra_cifrada, chave):
    palavra_cifrada = palavra_cifrada.lower()
    chave = chave.lower()

    chave_repetida = chave * (len(palavra_cifrada) // len(chave) + 1)
    chave_repetida = chave_repetida[:len(palavra_cifrada)]

    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    tabela_vigenere = [[0 for i in range(26)] for j in range(26)]
    for i in range(26):
        for j in range(26):
            tabela_vigenere[i][j] = alfabeto[(i + j) % 26]

    mensagem_decifrada = ""
    for i in range(len(palavra_cifrada)):
        letra_criptografada = palavra_cifrada[i]
        letra_chave = chave_repetida[i]
        linha = alfabeto.index(letra_chave)
        coluna = tabela_vigenere[linha].index(letra_criptografada)
        letra_descriptografada = alfabeto[coluna]
        mensagem_decifrada += letra_descriptografada

    return mensagem_decifrada
