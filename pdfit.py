from PIL import Image
import os, sys

cwd = os.getcwd()

filename_source = 'Source.jpg'

filename_destination = 'Destination.pdf'

fullpath_source = os.path.join(cwd, filename_source)

fullpath_destination = os.path.join(cwd, filename_destination)



print("cwd = {}", cwd)

""""
images = [
    Image.open("/Users/apple/Desktop/" + f)
    for f in ["bbd.jpg", "bbd1.jpg", "bbd2.jpg"]
]

pdf_path = "/Users/apple/Desktop/bbd1.pdf"
"""

jpeg_image = Image.open(filename_source)

images = [jpeg_image]

jpeg_image.save(
    fullpath_destination, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)

print("  \n jpeg has been PDFified successfully  !")

