def letra_para_numero(letra):
    return ord(letra.upper()) - ord('A')

def numero_para_letra(num):
    return chr((num % 26) + ord('A'))

# Função para repetir a chave até o tamanho do texto
def repetir_chave(texto, chave):
    return (chave * (len(texto) // len(chave) + 1))[:len(texto)]

def vigenere_cifrar(texto, chave):
    texto = texto.upper().replace(" ", "")
    chave = repetir_chave(texto, chave.upper())
    resultado = ""
    for t, k in zip(texto, chave):
        resultado += numero_para_letra(letra_para_numero(t) + letra_para_numero(k))
    return resultado

def vigenere_decifrar(cifrado, chave):
    chave = repetir_chave(cifrado, chave.upper())
    resultado = ""
    for c, k in zip(cifrado, chave):
        resultado += numero_para_letra(letra_para_numero(c) - letra_para_numero(k))
    return resultado

if __name__ == "__main__":
    print("Escolha uma opção:")
    print("1 - Codificar mensagem")
    print("2 - Decifrar mensagem")
    opcao = input("Digite 1 ou 2: ").strip()

    if opcao == "1":
        mensagem = input("Digite a mensagem para codificar: ").strip()
        chave = input("Digite a chave: ").strip()
        cifrada = vigenere_cifrar(mensagem, chave)
        print("Mensagem codificada:", cifrada)
    elif opcao == "2":
        mensagem = input("Digite a mensagem para decifrar: ").strip()
        chave = input("Digite a chave: ").strip()
        decifrada = vigenere_decifrar(mensagem, chave)
        print("Mensagem decifrada:", decifrada)