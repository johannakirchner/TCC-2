import cv2
import os
import matplotlib.pyplot as plt

# Caminho do classificador
classificador_1 = os.path.join("cascade_fotos", "cascade.xml")
rastreador_1 = cv2.CascadeClassifier(classificador_1)

# Importando a imagem a ser utilizada no modelo
imagem = cv2.imread("foto.jpg")

# Verificação: se a imagem foi carregada
if imagem is None:
    raise FileNotFoundError("Não consegui abrir 'foto.jpg'. Confirme o caminho do arquivo.")

# Transformando a imagem em escala de cinza
imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Encontrando os objetos
objetos = rastreador_1.detectMultiScale(imagem_gray)

# Coordenadas dos pixels e quantidade de objetos encontrados
print("Coordenadas:", objetos)
print("Quantidade de objetos:", len(objetos))


# Lista para armazenar os recortes (ROIs)
imagens_detectadas = []
for (x, y, w, h) in objetos:
    roi = imagem[y:y+h, x:x+w]
    imagens_detectadas.append(roi)

for i, roi in enumerate(imagens_detectadas):
    plt.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
    plt.title(f"Detecção {i}")
    plt.axis("off")
    plt.show()

