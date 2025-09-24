import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from sklearn.cluster import KMeans
import kneed

def findOptimumColorCount(image, color_counts):
    inertias = []

    for i in color_counts:
        kmeans = KMeans(n_clusters=i, random_state=0).fit(image)
        
        inertias.append(kmeans.inertia_)
        print(f'kmeans {i} clusters inertia: {kmeans.inertia_}')

    plt.plot(color_counts, inertias)
    plt.show()

    # optimal value for amount of colors
    knee = kneed.KneeLocator(color_counts, inertias, curve="convex", direction="decreasing").elbow
    return knee

def segment_clustering(image_name, color_count=None):
    # Load image
    image = imread(image_name)
    w, h, channels = image.shape

    #image = image[:,:,0:-1]
    #channels -= 1

    # Reshape image from (w,h,3) to (w*h,3) for kmeans
    image = np.reshape(image, (w*h, channels))
    print(f'Image shape {image.shape} size {w}, {h}')

    # KMeans clustering with desired color count
    if color_count is None:
        color_count = findOptimumColorCount(image, range(2, 16))
        
    kmeans = KMeans(n_clusters=color_count, random_state=0).fit(image)

    labels = kmeans.labels_
    print('Centroids ', kmeans.cluster_centers_)

    # Create segmented image from discovered centroids
    segmented = np.array(kmeans.cluster_centers_[labels], dtype=np.uint8)

    # Reshape back to (w,h,3)
    segmented = np.reshape(segmented, (w, h, channels))
    plt.imshow(segmented[:,:,:], interpolation='nearest', aspect='auto')
    plt.show()
    
    return segmented

def main():
    img = segment_clustering('hogwarts.jpg', color_count=15)

    plt.imshow(img, interpolation='nearest', aspect='auto')
    plt.show()

if __name__ == '__main__':
    main()