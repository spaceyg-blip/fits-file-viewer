import matplotlib.pyplot as plt


def plot_image(data):

    plt.imshow(data)

    plt.colorbar()

    plt.title("FITS Image")

    plt.show()
