
def testando_PIL():

    from PIL import Image

    #Open serve para carregar a imagem e guardar numa variavel
    image = Image.open("roguelikeitems.png")

    #format = formato da imagem   size = largura e altura  mode = rgb
    print(image.format, image.size, image.mode)

    # Salva o Aquivo com o nome determinado
    image.save("Aquivo.png")

    # Show é para exibir a imagem (Só funciona se voce tiver algo que consiga abrir a imagem)
    image.show()


def entendendo_sys_argv():
    import sys

    #Como o sys.argv funciona: Pegue todos os arquivos que foram passados ao rodar o script no terminal
    print(sys.argv)


#Conversor de png para jpg
def conversor_png_ara_jpg():

    import os, sys
    from PIL import Image


    for entrada_Arquivo in sys.argv[1:]:
        f, e = os.path.splitext(entrada_Arquivo)
        saida_Arquivo = f + ".jpg"

        if entrada_Arquivo != saida_Arquivo:
            try:
                with Image.open(entrada_Arquivo) as im:
                    im.save(saida_Arquivo)
            except OSError:
                print(" Erro em converter " , entrada_Arquivo)


# Cortar, colar e mesclar imagens
def usando_crop():
    from PIL import Image

    im = Image.open("Itens_loja.png")


    box = (0, 0, 16, 16)
    region = im.crop()

    region.show()



# Recortando a Imagem

from PIL import Image


sprite = Image.open("Itens_loja.png")


icone_Largura = 16
icone_Altura = 16


colunas = sprite.width // icone_Largura #13
linhas = sprite.height // icone_Altura #14


for linha in range(linhas):
    for coluna in range(colunas):
        x = coluna * icone_Largura
        y = linha * icone_Altura

        icone = sprite.crop((x, y, x + icone_Largura, y + icone_Altura))
        print(x, y, x + icone_Largura, y + icone_Altura)

print("Terminou")