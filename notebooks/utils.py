import matplotlib.pyplot as plt
import numpy as np
import os


def listdir_ignore_hidden(path):
    """generator to yield dirs but ignore hidden folders
    """
    for d in os.listdir(path):
        if not d.startswith('.'):
            yield d
            
            
def show_batch(data_loader, batch_size, classes):
    """Show all images in a batch
    """
    
    dataiter = iter(data_loader)
    images, labels = next(dataiter)
    images = images.numpy() # convert images to numpy for display
    images.shape

    # plot the images in the batch, along with the corresponding labels
    fig = plt.figure(figsize=(20, 10))
    for i in np.arange(batch_size):
        ax = fig.add_subplot(2, batch_size//2, i+1, xticks=[], yticks=[])

        img = (images[i] / 2) + 0.5  # unnormalize
        plt.imshow(np.transpose(img, (1, 2, 0))) 

        ax.set_title(classes[labels[i]])