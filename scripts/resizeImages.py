import os
from PIL import Image

def reduzir_resolucao_pasta(pasta_entrada, pasta_saida, largura=500, altura=500):
    os.makedirs(pasta_saida, exist_ok=True)

    for arquivo in os.listdir(pasta_entrada):
        caminho_entrada = os.path.join(pasta_entrada, arquivo)

        if os.path.isfile(caminho_entrada) and arquivo.lower().endswith((".jpg", ".jpeg", ".png")):
            img = Image.open(caminho_entrada)
            img_redimensionada = img.resize((largura, altura))
            caminho_saida = os.path.join(pasta_saida, arquivo)
            img_redimensionada.save(caminho_saida)
            print(f"Salvo: {caminho_saida}")

# Exemplo de uso
reduzir_resolucao_pasta("data_set_fotos", "data_set_fotos_resize")
