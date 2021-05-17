# import the necessary packages
# from PIL import Image
from skimage import transform
import skimage
skimage.transform.seam_carve
from skimage import filters, data
import argparse
import cv2
import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt
from skimage.filters import sobel,gaussian
from skimage.transform import seam_carve
from skimage import color
from skimage.io import imsave

import numpy as np

# from PIL import Image 
# import PIL 
def seam_carve(numSeams, vertical=True, horizontal=True):
	trainset = pd.read_csv("train.csv", index_col="Id")

	image = data.imread('./tempDir/input.jpeg')
	gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
	# gray = color.rgb2gray(image)
	# mag = filters.sobel(gray.astype("float"))
	eimg = filters.sobel(color.rgb2gray(image))
	# mag = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)
	# sobel5x = cv2.getDerivKernels(1, 0, 5)
	
	# for numSeams in range(20, 140, 20):
		# perform seam carving, removing the desired number
		# of frames from the image -- `vertical` cuts will
		# change the image width while `horizontal` cuts will
		# change the image height
	carved = ''
	if vertical:
		carved = transform.seam_carve(image, eimg, 'horizontal', numSeams)
	if horizontal:
		carved = transform.seam_carve(image, eimg, 'vertical', numSeams)
	# cv2.imshow("ABC", carved)
	# cv2.waitKey(0)
	# skimage.imwrite("output/carved.jpg", carved)
	imsave('./tempDir/carved.jpeg', carved)
	
	# cv2.imwrite('./tempDir/carved.jpeg', carved)
	# plt.imsave('./tempDir/carved.jpeg', carved)
# 	img = Image.open(r'output/carved.png')
# 	picture = picture.save('output/carved.png')
# seam_carve(100, False)