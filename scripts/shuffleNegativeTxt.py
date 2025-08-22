import random

# Caminho para o negatives.txt
negatives_path = 'data_set/negatives/negatives.txt'

# Lê todas as linhas
with open(negatives_path, 'r') as f:
    lines = f.read().splitlines()

# Embaralha
random.shuffle(lines)

# Salva de volta
with open(negatives_path, 'w') as f:
    f.write('\n'.join(lines))

print(f'Arquivo {negatives_path} embaralhado com sucesso!')