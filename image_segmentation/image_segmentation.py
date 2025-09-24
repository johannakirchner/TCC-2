import numpy as np
from PIL import Image
from PIL import ImageColor
import matplotlib.pyplot as plt
import argparse
from image_segmentation_clustering import segment_clustering
from image_segmentation_nn import segment_nn

def parsecmd():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, required=True, help='Input image name')
    parser.add_argument('-o', '--output', type=str, help='Output image name')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-c', '--colors', type=str, help='List of RGB colors for segmentation')
    group.add_argument('-k', '--clustercount', type=int, help='Number of RGB colors for clustering segmentation')
    parser.add_argument('-rw', '--resizewidth', type=int, help='Resized image width')
    parser.add_argument('-rh', '--resizeheight', type=int, help='Resized image height')
    args = parser.parse_args()
    
    if args.resizewidth is not None and args.resizeheight is None:
        args.resizeheight = args.resizewidth
    elif args.resizewidth is None and args.resizeheight is not None:
        args.resizewidth = args.resizeheight
        
    return args

def main():
    args = parsecmd()
    
    image_name = args.input
    
    # Nearest neighbor segmentation
    if args.colors:
        hexcode_list = args.colors.split()
        colors = [ImageColor.getcolor(hexcode, "RGB") for hexcode in hexcode_list] # 0: to 1: if # is expected
        colors = np.array(colors)
        
        image = segment_nn(image_name, colors)
        
    # Clustering segmentation
    else:
        if args.clustercount:
            image = segment_clustering(image_name, args.clustercount)
        else:
            # Discover optimal clustering count if not given
            image = segment_clustering(image_name)

    # Resize image
    if args.resizewidth is not None and args.resizeheight is not None:
        image = Image.fromarray(image)
        image = image.resize((image.size[0]//10, image.size[1]//10), Image.LANCZOS)
        image = np.array(image)
        
    # Output to file or screen
    if args.output is not None:
        result = Image.fromarray(image)
        result.save(args.output)
    else:
        plt.imshow(image, interpolation='nearest', aspect='auto')
        plt.show()
    
    
if __name__ == '__main__':
    main()