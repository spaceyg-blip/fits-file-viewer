from astropy.io import fits


def load_fits(file_path):

    hdul = fits.open(file_path)

    print("Number of HDUs:", len(hdul))

    data = hdul[0].data

    header = hdul[0].header

    return data, header
