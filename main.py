from src.load_fits import load_fits
from src.show_header import show_header
from src.plot_image import plot_image

file_path = "data/sample.fits"

data, header = load_fits(file_path)

show_header(header)

plot_image(data)
