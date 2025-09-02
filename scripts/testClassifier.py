import matplotlib.pyplot as plt
import cv2

# Importando o classificador
classificador_1 = 'cascade_fotos\cascade.xml'
rastreador_1 = cv2.CascadeClassifier(classificador_1)

# Importando a imagem a ser utilizada no modelo
imagem = cv2.imread('foto.jpg')

# Transformando a imagem em escala de cinza
imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Encontrando os objetos
objetos = rastreador_1.detectMultiScale(imagem_gray)

# Coordenadas dos pixels e quantidade de objetos encontrados
print(objetos)
print(len(objetos))

# Identificando os objetos encontrados
imagem_resultado = imagem.copy()
for (x, y, w, h) in objetos:
    cv2.rectangle(imagem_resultado, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Convertendo novamente para RGB para exibir corretamente no matplotlib
imagem_resultado = cv2.cvtColor(imagem_resultado, cv2.COLOR_BGR2RGB)

# Visualizando o resultado
plt.figure(figsize=(10, 10))
plt.imshow(imagem_resultado)
plt.axis('off')
plt.show()
