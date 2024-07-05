import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar


def descriptografar(texto_encriptado, palavra_chave):
    texto_encriptado = texto_encriptado.upper()
    palavra_chave = palavra_chave.upper()
    texto_descriptografado = ""
    index = 0
    for letra in texto_encriptado:
        if letra == " ":
            texto_descriptografado += " "
        elif letra.isalpha():
            codigo = ord(letra)
            chave = ord(palavra_chave[index]) - ord("A")
            novo_codigo = codigo - chave
            if novo_codigo < ord("A"):
                novo_codigo += 26
            nova_letra = chr(novo_codigo)
            texto_descriptografado += nova_letra
            index += 1
            if index == len(palavra_chave):
                index = 0
        else:
            pass
    return texto_descriptografado


image = cv2.imread("qrcode.png")
decodedObjects = pyzbar.decode(image)
for obj in decodedObjects:
    data = obj.data.decode("utf-8")
    print("Texto encriptado:", data)
    key = input("Digite a chave da cifra de Vigenère : ")
    decrypted_data = descriptografar(data, key)
    print("Texto descriptografado:", decrypted_data)
