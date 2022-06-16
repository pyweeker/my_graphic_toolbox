#  https://note.nkmk.me/en/python-pillow-concat-images/

from PIL import Image


import itertools


BASENAME = "whatyouwant" 

STD_SIZE = 4000 # your photo size in pixels , choose what you need for x and y axis


a = BASENAME + "_a.jpg"
b = BASENAME + "_b.jpg"
c = BASENAME + "_c.jpg"
d = BASENAME + "_d.jpg"
e = BASENAME + "_e.jpg"
f = BASENAME + "_f.jpg"
g = BASENAME + "_g.jpg"

list_jpeg = [a,b,c,d,e,f,g]


def get_concat_v(*list_jpeg): # THIS WILL MERGE VERTICALLY

	print(f" list_jpeg  {list_jpeg}")

	flatten_list_jpeg = list(itertools.chain(*list_jpeg))

	print(f" flatten_list_jpeg  {flatten_list_jpeg}")



	list_image = [Image.open(jpeg_file) for jpeg_file in flatten_list_jpeg]





	print(f"type  list_image  {type(list_image)}   \n           list_image  {list_image} ")


	len_img = len(list_image)
	im0 = list_image[0]

	print(f"type  im0  {type(im0)} ")
	print(f"  im0  {im0} ")

	print("\n ____________________________  ")



	img_height = im0.height
	total_img_height = STD_SIZE * len_img

	dst = Image.new('RGB', (STD_SIZE, total_img_height))

	for img in list_image:
		dst.paste(img, (0, img_height * list_image.index(img)))

	return dst




get_concat_v(list_jpeg).save('fusion_v.jpg')
