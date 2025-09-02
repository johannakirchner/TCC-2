import os
import random
import string

# pasta onde estão os arquivos
pasta = "data_set_fotos_resize/negatives"

# pega todos os arquivos (ignora pastas)
arquivos = [f for f in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, f))]

# 1ª etapa: renomeia para nomes aleatórios
for f in arquivos:
    extensao = os.path.splitext(f)[1]
    nome_temp = ''.join(random.choices(string.ascii_letters + string.digits, k=12)) + extensao
    os.rename(os.path.join(pasta, f), os.path.join(pasta, nome_temp))

# 2ª etapa: renomeia de 1 até n
arquivos_temp = [f for f in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, f))]
arquivos_temp.sort()  # ordem consistente

lista_final = []
for i, f in enumerate(arquivos_temp, start=1):
    extensao = os.path.splitext(f)[1]
    novo_nome = f"{i}{extensao}"
    os.rename(os.path.join(pasta, f), os.path.join(pasta, novo_nome))
    lista_final.append(novo_nome)

# 3ª etapa: gera pos.txt
with open(os.path.join(pasta, "negatives.txt"), "w") as f:
    for nome in lista_final:
        f.write(nome + "\n")
