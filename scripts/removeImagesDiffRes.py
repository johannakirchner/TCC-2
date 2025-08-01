import os
from PIL import Image
from io import BytesIO

# Configurações
diretorio = 'data_set/negatives'
largura_esperada = 224
altura_esperada = 224
num_deletados = 0

# Percorre todos os arquivos da pasta
for arquivo in os.listdir(diretorio):
    caminho_arquivo = os.path.join(diretorio, arquivo)
    
    # Só processa arquivos de imagem comuns
    if arquivo.lower().endswith('.jpeg'):
        try:
            # Lê a imagem na memória para evitar bloqueio
            with open(caminho_arquivo, 'rb') as f:
                img_data = BytesIO(f.read())

            with Image.open(img_data) as img:
                largura, altura = img.size

            if largura != largura_esperada or altura != altura_esperada:
                os.remove(caminho_arquivo)
                print(f"Deletado: {arquivo} ({largura}x{altura})")
                num_deletados += 1

        except Exception as e:
            print(f"Erro ao processar {arquivo}: {e}")

print(f"Deletado total de {num_deletados} arquivos")
