import pytesseract
from PIL import ImageGrab
import pyautogui
import time

text = ''

img = ImageGrab.grab((165, 395, 1145, 455)) # don't forget to change this numbers !
pix = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        c = pix[i, j]
        if 160 < c[0] and 160 < c[1] and 160 < c[2]:
            img.putpixel((i, j), (255, 255, 255))
        else:
            img.putpixel((i, j), (0, 0, 0))
text += pytesseract.image_to_string(img)
text += ' '

img = ImageGrab.grab((165, 450, 1145, 495)) # don't forget to change this numbers !
pix = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        c = pix[i, j]
        if 160 < c[0] and 160 < c[1] and 160 < c[2]:
            img.putpixel((i, j), (255, 255, 255))
        else:
            img.putpixel((i, j), (0, 0, 0))
text += pytesseract.image_to_string(img)
text += ' '

img = ImageGrab.grab((165, 505, 1145, 540)) # don't forget to change this numbers !
pix = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        c = pix[i, j]
        if 160 < c[0] and 160 < c[1] and 160 < c[2]:
            img.putpixel((i, j), (255, 255, 255))
        else:
            img.putpixel((i, j), (0, 0, 0))
text += pytesseract.image_to_string(img)
text += ' '

img = ImageGrab.grab((165, 555, 1145, 585)) # don't forget to change this numbers !
pix = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        c = pix[i, j]
        if 160 < c[0] and 160 < c[1] and 160 < c[2]:
            img.putpixel((i, j), (255, 255, 255))
        else:
            img.putpixel((i, j), (0, 0, 0))
text += pytesseract.image_to_string(img)

arr = text.split(' ')
for i in arr:
    pyautogui.typewrite(i)
    pyautogui.typewrite(' ')
