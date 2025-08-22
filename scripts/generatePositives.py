import os
import random
import subprocess

# Caminhos principais
negatives_path = 'data_set/negatives/negatives.txt'
positives_base_path = 'data_set/positives'
vec_output_path = os.path.join(positives_base_path, 'vec')
mergevec_script = 'scripts/mergevec.py'

# Lista de resistores (adicione os nomes conforme necessário)
resistores = [
    'resistor1.jpg',
    'resistor2.jpg',
    'resistor3.jpg',
    'resistor4.jpg'
]

# Parâmetros gerais
num_samples = 1800
w, h = 40, 15

# Função para embaralhar negatives.txt
def shuffle_negatives():
    with open(negatives_path, 'r') as f:
        lines = f.read().splitlines()
    random.shuffle(lines)
    with open(negatives_path, 'w') as f:
        f.write('\n'.join(lines))
    print(f'[OK] negatives.txt embaralhado')

# Loop para cada resistor
for resistor in resistores:
    resistor_name = os.path.splitext(resistor)[0]
    info_path = os.path.join(positives_base_path, f'positive_{resistor_name}')
    lst_path = os.path.join(info_path, f'{resistor_name}.lst')
    vec_path = os.path.join(vec_output_path, f'{resistor_name}.vec')
    
    # Cria pasta para positives do resistor
    os.makedirs(info_path, exist_ok=True)
    os.makedirs(vec_output_path, exist_ok=True)
    
    # Embaralha negatives antes de cada createsamples
    shuffle_negatives()
    
    # Primeiro createsamples (gera .lst)
    cmd_lst = [
        'execs_opencv/opencv_createsamples',
        '-img', os.path.join(positives_base_path, resistor),
        '-bg', negatives_path,
        '-info', lst_path,
        '-maxxangle', '0.5',
        '-maxyangle', '0.5',
        '-maxzangle', '0.5',
        '-num', str(num_samples),
        '-bgcolor', '255',
        '-bgthresh', '8'
    ]
    print(f'[RUN] {" ".join(cmd_lst)}')
    subprocess.run(cmd_lst, check=True)
    
    # Segundo createsamples (gera .vec)
    cmd_vec = [
        'execs_opencv/opencv_createsamples',
        '-info', lst_path,
        '-num', str(num_samples),
        '-w', str(w),
        '-h', str(h),
        '-vec', vec_path
    ]
    print(f'[RUN] {" ".join(cmd_vec)}')
    subprocess.run(cmd_vec, check=True)

# Mescla todos os .vec
cmd_merge = [
    'python', mergevec_script,
    '-v', vec_output_path,
    '-o', os.path.join(vec_output_path, 'vetor.vec')
]
print(f'[RUN] {" ".join(cmd_merge)}')
subprocess.run(cmd_merge, check=True)

print('[OK] Processo concluído!')
