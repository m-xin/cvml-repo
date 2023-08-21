## Traffic Citation Notice Images Processing ##

# Import packages
from collections import Counter
from sklearn.cluster import KMeans
import cv2 as cv
import matplotlib.pyplot as plt
import PIL
import numpy as np

# Image presentation:


def show_img_compar(img_1, img_2):
    f, ax = plt.subplots(1, 2, figsize=(10, 10))
    ax[0].imshow(img_1)
    ax[1].imshow(img_2)
    ax[0].axis('off')
    ax[1].axis('off')
    f.tight_layout()
    plt.show()


# Extract RGB features
img = cv.imread("python_traffic_image/traffic_image/image3-1.png")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img2 = cv.imread("python_traffic_image/traffic_image/image4-1.png")
img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)

dim = (500, 300)  # used for the bar chart
# resize image
img = cv.resize(img, dim, interpolation=cv.INTER_AREA)
img2 = cv.resize(img2, dim, interpolation=cv.INTER_AREA)

show_img_compar(img, img2)
clt = KMeans(n_clusters=5)


def palette_perc(k_cluster):
    width = 300
    palette = np.zeros((50, width, 3), np.uint8)

    n_pixels = len(k_cluster.labels_)
    counter = Counter(k_cluster.labels_)  # count how many pixels per cluster
    perc = {}
    for i in counter:
        perc[i] = np.round(counter[i]/n_pixels, 2)
    perc = dict(sorted(perc.items()))

    # for logging purposes
    print("The percentage is: ")
    print(perc)
    print("The featuring RGB for each color block is: ")
    print(k_cluster.cluster_centers_)

    step = 0

    for idx, centers in enumerate(k_cluster.cluster_centers_):
        palette[:, step:int(step + perc[idx]*width+1), :] = centers
        step += int(perc[idx]*width+1)

    return palette


print("From Img 3-1: ")
clt_1_perc = clt.fit(img.reshape(-1, 3))
show_img_compar(img, palette_perc(clt_1_perc))

print("From Img 4-1: ")
clt_2_perc = clt.fit(img2.reshape(-1, 3))
show_img_compar(img2, palette_perc(clt_2_perc))
