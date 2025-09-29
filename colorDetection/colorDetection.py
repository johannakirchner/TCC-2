import cv2
import numpy as np

# Carrega a imagem
img = cv2.imread("colorDetection/test2.jpg")

# Converte para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold para remover fundo branco (ajuste o valor conforme a iluminação)
_, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

# Aplica a máscara ao original
resistor_sem_fundo = cv2.bitwise_and(img, img, mask=mask)

# Remover pontos de reflexo (muito brancos dentro do resistor)
# Converte a imagem mascarada para HSV e filtra pixels muito claros
hsv = cv2.cvtColor(resistor_sem_fundo, cv2.COLOR_BGR2HSV)
lower = np.array([0, 0, 0])
upper = np.array([180, 50, 250])  # reduz saturação/valor alto
mask_reflexo = cv2.inRange(hsv, lower, upper)
resistor_limpo = cv2.bitwise_and(resistor_sem_fundo, resistor_sem_fundo, mask=mask_reflexo)

# Salva resultado
cv2.imwrite("resistor_processado.png", resistor_sem_fundo)

# Mostra
#cv2.imshow("Original", img)
#cv2.imshow("Sem Fundo", resistor_sem_fundo)
#cv2.imshow("Reflexo Removido", resistor_limpo)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
