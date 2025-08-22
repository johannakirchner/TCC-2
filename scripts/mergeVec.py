import sys
import glob
import struct
import argparse
import traceback

def exception_response(e):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    for line in lines:
        print(line)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', dest='vec_directory', required=True, help="Diretório com arquivos .vec")
    parser.add_argument('-o', dest='output_filename', required=True, help="Arquivo de saída .vec")
    args = parser.parse_args()
    return args.vec_directory, args.output_filename

def merge_vec_files(vec_directory, output_vec_file):
    if vec_directory.endswith('/'):
        vec_directory = vec_directory[:-1]
    
    files = glob.glob(f'{vec_directory}/*.vec')
    
    if len(files) <= 0:
        print(f'Nenhum arquivo .vec encontrado no diretório: {vec_directory}')
        sys.exit(1)
    
    if len(files) == 1:
        print(f'Apenas 1 arquivo .vec encontrado no diretório: {vec_directory}. Não é possível mesclar um único arquivo.')
        sys.exit(1)
    
    prev_image_size = 0
    
    try:
        with open(files[0], 'rb') as vecfile:
            content = vecfile.read()
            val = struct.unpack('<iihh', content[:12])
            prev_image_size = val[1]
    except IOError as e:
        print(f'Erro de I/O ao processar o arquivo: {files[0]}')
        exception_response(e)
    
    total_num_images = 0
    image_size = prev_image_size
    
    for f in files:
        try:
            with open(f, 'rb') as vecfile:
                content = vecfile.read()
                val = struct.unpack('<iihh', content[:12])
                num_images = val[0]
                image_size = val[1]
                
                if image_size != prev_image_size:
                    err_msg = (
                        f"As dimensões das imagens nos arquivos .vec diferem.\n"
                        f"Tamanho do arquivo {f}: {image_size}\n"
                        f"Tamanho dos arquivos anteriores: {prev_image_size}"
                    )
                    sys.exit(err_msg)
                
                total_num_images += num_images
        
        except IOError as e:
            print(f'Erro de I/O ao processar o arquivo: {f}')
            exception_response(e)
    
    header = struct.pack('<iihh', total_num_images, image_size, 0, 0)
    
    try:
        with open(output_vec_file, 'wb') as outputfile:
            outputfile.write(header)
            for f in files:
                with open(f, 'rb') as vecfile:
                    content = vecfile.read()
                    outputfile.write(content[12:])
    except Exception as e:
        exception_response(e)

if __name__ == '__main__':
    vec_directory, output_filename = get_args()
    
    if not vec_directory:
        sys.exit('É necessário passar o diretório de arquivos .vec com -v')
    
    if not output_filename:
        sys.exit('É necessário passar o nome do arquivo de saída com -o')
    
    merge_vec_files(vec_directory, output_filename)
