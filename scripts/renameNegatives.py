import os

# caminho para o diretório de imagens
diretorio = "data_set_fotos"

# lista os arquivos
arquivos = os.listdir(diretorio)

imagens = [arquivo for arquivo in arquivos]

for indice, imagem in enumerate(imagens, start=1):
    extensao = os.path.splitext(imagem)[1]
    novo_nome = f"{indice}{extensao}"
    caminho_antigo = os.path.join(diretorio, imagem)
    caminho_novo = os.path.join(diretorio, novo_nome)
    os.rename(caminho_antigo, caminho_novo)
    print(f"{imagem} renomeado para {novo_nome}")

# atualizar a lista de arquivos após renomeação
arquivos = os.listdir(diretorio)

# salvar a lista em um arquivo .txt
with open("negatives/negatives.txt", "w") as arquivo:
    for nome in arquivos:
        caminho_completo = os.path.join(diretorio, nome)
        if os.path.isfile(caminho_completo):  # verifica se é um arquivo
            arquivo.write(f"{nome}\n")

print(f"Lista de arquivos salva")
