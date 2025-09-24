import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from scipy.spatial import distance_matrix

def segment_nn(image_name, colors):
    # Load image
    image = imread(image_name)
    w, h, channels = image.shape

    # Reshape image from (w,h,3) to (w*h,3)
    image = np.reshape(image, (w*h, 3))
    print(f'Image shape {image.shape} size {w}, {h}')

    # Nearest neighbor approach
    # Get distances between pixels in the image and desired colors
    distances = distance_matrix(image, colors)

    # NOTE: this could also be done by setting kmeans with max_iter=1
    # https://stackoverflow.com/questions/60205100/define-cluster-centers-manually

    # Select the closest colors, akin to centroids in kmeans
    labels = np.argmin(distances, axis=1)

    # Create segmented image from desired colors
    segmented = np.array(colors[labels], dtype=np.uint8)

    # Reshape back to (w,h,3)
    segmented = np.reshape(segmented, (w, h, 3))
        
    return segmented

def main():
    # binarization (black and white)
    #colors = np.array([[0,0,0], [255, 255, 255]])
    
    # grayscale
    colors = np.array( [[c,c,c] for c in range(256)] )
    
    img = segment_nn('hogwarts.jpg', colors)

    plt.imshow(img, interpolation='nearest', aspect='auto')
    plt.show()

if __name__ == '__main__':
    main()