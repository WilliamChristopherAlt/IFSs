import matplotlib.pyplot as plt
import numpy as np, matplotlib.colors as mcolors
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


def draw(data, colorMode='binary', cmapName=None):
    if colorMode == 'binary':
        cmap = 'binary'
    elif colorMode == 'grey':    
        cmap_colors = [(25, 25, 25)] + [(i/255, i/255, i/255) for i in range(256)]
        cmap = mcolors.ListedColormap(cmap_colors)
    elif colorMode == 'colorful':
        # Create a custom colormap based on provided map
        custom_cmap = plt.cm.get_cmap(cmapName, 256)
        # Set the color for 0 to white
        custom_cmap_colors = custom_cmap(np.arange(custom_cmap.N))
        custom_cmap_colors[0] = [1, 1, 1, 1]  # White color
        # Create the modified colormap
        cmap = mcolors.ListedColormap(custom_cmap_colors)

    plt.imshow(data, cmap=cmap)

    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def draw_alt(xs, ys):
    plt.scatter(xs, ys, color='green', s = 1)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def coorsToDataMatrix(xs, ys, density, range, pixelCounting=True):
    maxX, minX, maxY, minY = range
    width = int((maxX - minX) * density)
    height = int((maxY - minY) * density)

    if pixelCounting:
        data = np.zeros((height, width), dtype=int)
        for x, y in zip(xs, ys):
            data[-int((y-minY)*density)][int((x-minX)*density)] += 1
    else:
        data = np.zeros((height, width), dtype=bool)
        for x, y in zip(xs, ys):
            data[-int((y-minY)*density)][int((x-minX)*density)] = True

    return data

def save_image(data, file_path, colorMode='binary', cmapName=None):
    if colorMode == 'binary':
        # Convert the boolean matrix to an integer matrix (255 for False, 0 for True)
        int_data = np.where(data, 0, 255).astype(np.uint8)
    elif colorMode == 'grey' or 'colorful':
        if colorMode == 'grey':
            cmap_colors = [(1, 1, 1)] + [(i/255, i/255, i/255) for i in range(256)]
        elif colorMode == 'colorful':
            # Create a custom colormap based on provided map
            custom_cmap = plt.cm.get_cmap(cmapName, 256)
            # Set the color for 0 to white
            cmap_colors = custom_cmap(np.arange(custom_cmap.N))
            cmap_colors[0] = [1, 1, 1, 1]  # White color

        custom_cmap = mcolors.ListedColormap(cmap_colors)
        # Normalize data to range [0, 1] to match the colormap
        # normalized_data = (data - np.min(data)) / (np.max(data) - np.min(data))
        normalized_data = data / np.max(data)
        # Map the normalized values to RGB values using the colormap
        rgb_data = custom_cmap(normalized_data)
        # Scale RGB values to the range [0, 255]
        int_data = (rgb_data[:, :, :3] * 255).astype(np.uint8)

    # Create an image from the RGB matrix
    image = Image.fromarray(int_data)
    image.save(file_path)
