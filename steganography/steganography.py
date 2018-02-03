from PIL import Image
import numpy

def convert_image_to_pixels(image):
	listOfPixels = []
	img = Image.open(image)
	im = img.load()
	[width, hight] = img.size
	for x in range(0, hight):
		for y in range(0, width):
			listOfPixels.append(im[y, x])
	return listOfPixels


def convert_pixels_to_image(pixels, size):
	img = Image.new("RGB", size)
	img.putdata(pixels)
	return img
def encode_RGB_image(nOfBits, originalImg, imgToHideIn, newImgName):
	img = Image.open(originalImg)
	im = img.load()
	[width, hight] = img.size
	secretImg = convert_image_to_pixels(originalImg)
	puplicImg = convert_image_to_pixels(imgToHideIn)
	newImg = []
	for x in range(0, hight):
		for y in range(0, width):
			r = 0
			b = 0
			g = 0
			sR = secretImg[width*x+y][0] #red pixels
			sG = secretImg[width*x+y][1] #green pixel
			sB = secretImg[width*x+y][2] #blue pixel
			pR = puplicImg[width*x+y][0]
			pG = puplicImg[width*x+y][1]
			pB = puplicImg[width*x+y][2]
			for j in range (nOfBits):
				bit = 1 << (7-j)
				bit2 = 1 << (nOfBits - j - 1)
				if sR & bit == bit:
					if pR & bit2 != bit2:
						pR += bit2
				elif pR & bit2 == bit2:
					pR -= bit2
				if sG & bit == bit:
					if pG & bit2 != bit2:
						pG += bit2
				elif pG & bit2 == bit2:
					pG -= bit2
				if sB & bit == bit:
					if pB & bit2 != bit2:
						pB += bit2
				elif pB & bit2 == bit2:
					pB -= bit2
			newImg.append((pR, pG, pB))

	img1 = Image.new("RGB", img.size)
	img1.putdata(newImg)
	img1.save(newImgName)

def reveal_RGB_image(filename,nOfBits, newImgName):
	pixels = convert_image_to_pixels(filename)
	hiddenPixels = []
	for i in pixels:
		r = 0
		b = 0
		g = 0
		x = i[0] #red pixels
		y = i[1] #blue pixel
		z = i[2] #green pixel
		for j in range(nOfBits):
			bit = 1 << j
			if (x & bit == bit): #check the first least signgicant bit
				r += 1 << (8 - nOfBits + j) #shift it to be the second most sigficant bit
			if (y & bit == bit):
				g += 1 << (8 - nOfBits + j)
			if (z & bit == bit):
				b += 1 << (8 - nOfBits + j)
		hiddenPixels.append((r, g, b))
	imgl = Image.open(filename)
	img = Image.new("RGB", imgl.size)
	img.putdata(hiddenPixels)
	img.save(newImgName)
	return img


def main():
	x=1
	while x == 1:
		state = input("Please write decode or encode to decode or encode an image: ")
		if state == 'encode':
			nOfBits = int(input("please enter the number of bits you want to shift (less than 4): "))
			originalImg = input("please write the name of the image you want to hide: ")
			imgToHideIn = input("please write the name of the image you want to hide in your orginal image: ")
			img = Image.open(originalImg)
			img1 = Image.open(imgToHideIn)
			if(img.size == img1.size):
				newImgName = input("please write your new image name: ")
				encode_RGB_image(nOfBits, originalImg, imgToHideIn, newImgName)
				x = 0 
			else:
				print("The Two images don't have the same size")

		elif state == 'decode':
			nOfBits = int(input("please enter the number of bits you want to shift (less than 4): "))
			originalImg = input("please write the name of the image that your orginal image is hidden in: ")
			newImgName = input("please write your new image name: ")
			im = reveal_RGB_image(originalImg, nOfBits, newImgName)
			im.show()
			x = 0
		else:
			print("please retype your option: ")
         
if __name__ == '__main__':
	main()
