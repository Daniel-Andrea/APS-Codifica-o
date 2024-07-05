
import qrcode
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label


def criptografar(texto, palavra_chave):
    texto = texto.upper()
    palavra_chave = palavra_chave.upper()
    texto_criptografado = ""
    indice = 0
    for letra in texto:
        if letra == " ":
            texto_criptografado += " "
        elif letra.isalpha():
            codigo = ord(letra)
            chave = ord(palavra_chave[indice]) - ord("A")
            novo_codigo = codigo + chave
            if novo_codigo > ord("Z"):
                novo_codigo -= 26
            nova_letra = chr(novo_codigo)
            texto_criptografado += nova_letra
            indice += 1
            if indice == len(palavra_chave):
                indice = 0
        else:
            pass
    return texto_criptografado


texto_original = str(input("Digite sua chave (por favor somente letras, sem acentuação, fique atento):  "))
palavra_chave = 'teste'
texto_criptografado = criptografar(texto_original, palavra_chave)


def generate_qr(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img


class QRCodeApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text='QR Code')
        layout.add_widget(label)
        data_criptografada = criptografar(texto_original, palavra_chave)
        img = generate_qr(data_criptografada)
        img.save("qrcode.png")
        image = Image(source='qrcode.png')
        layout.add_widget(image)
        return layout


if __name__ == '__main__':
    QRCodeApp().run()

print('o palavra original é: ', texto_original)
print('A palavra criptografada é: ', texto_criptografado)
