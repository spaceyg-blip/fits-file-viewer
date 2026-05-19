import matplotlib.pyplot as plt

def plot_image(data):

    plt.figure(figsize=(8,8))

    plt.imshow(
        data,
        origin="lower",
        cmap="inferno"
    )

    plt.colorbar(
        label="Pixel Intensity"
    )

    plt.title(
        "Horsehead Nebula FITS Image"
    )

    plt.xlabel("X Pixel")

    plt.ylabel("Y Pixel")

    plt.tight_layout()

    plt.show()
