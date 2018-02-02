# Problem Set 5
# Name: Tammam Mustafa
# Collaborators: NONE
# Time: 20

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


def reveal_binary_image(filename):
   
    pixels = convert_image_to_pixels(filename)
    hiddenpixels = []
    for i in pixels:
        temp = 0
        if (i & 1 == 1):
            temp = 255
        # x=i-tmp
        #        tmp+=x&-x

        hiddenpixels.append(temp)
    imgl = Image.open(filename)
    img = Image.new("L", imgl.size)
    img.putdata(hiddenpixels)
    return img


def reveal_RGB_image(filename):
    pixels = convert_image_to_pixels(filename)
    hiddenpixels = []

    #        r = i[0] & -i[0]
    #        b = i[1] & -i[1]
    #        g = i[2] & -i[2]
    #        x = i[0] - r
    #        y = i[1] - g
    #        z = i[2] - b
    #        r += x & -x
    #        g = y & -y
    #        b = z & -z
    for i in pixels:
        r = 0
        b = 0
        g = 0
        x = i[0] #red pixels
        y = i[1] #blue pixel
        z = i[2] #green pixel
        if (x & 1 == 1): #check the first least signgicant bit
            r += 1 << 6 #shift it to be the second most sigficant bit
        if (x & 2 == 2):
            r += 1 << 7
        if (y & 1 == 1):
            g += 1 << 6
        if (y & 2 == 2):
            g += 1 << 7
        if (z & 1 == 1):
            b += 1 << 6
        if (z & 2 == 2):
            b += 1 << 7
        hiddenpixels.append((r, g, b))
    imgl = Image.open(filename)
    img = Image.new("RGB", imgl.size)
    img.putdata(hiddenpixels)
    return img


def main():

    im2 = reveal_RGB_image('hidden2.bmp')
    im2.show()


if __name__ == '__main__':
    main()
