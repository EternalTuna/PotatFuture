from PIL import Image, ImageDraw, ImageFont
import random
import math

"""
main section
:param: ascii conv
:in: img
:return: ascii table
"""
BACK_COLOR = "BLACK"
IN_IMG = 'PotattFuture.png'
FNT = ImageFont.truetype('arial.ttf', 7)

im = Image.open(IN_IMG)
(width, height) = im.size

# math !calculations
line = math.ceil(im.size[0]/50 * 13 * 1.2)
row = math.ceil(im.size[1]/50 * 6 * 1.2)

# main !loop
string = ''
for i in range(row):
    for j in range(line):
        string += str(random.choice([0, 1]))
    string += '\n'

# Needs img creation consts
img = Image.new('RGBA', (im.size[0], im.size[1]), BACK_COLOR)
draw_text = ImageDraw.Draw(img)
draw_text.text((1,1), string, spacing=1, font=FNT, fill=0)
img2 = Image.open(IN_IMG)
alphaComposited = Image.alpha_composite(img2, img)

# AlphaComposited?
image = alphaComposited
new_image = Image.new("RGBA", image.size, BACK_COLOR)
new_image.paste(image, (0, 0), image)
new_image.convert('RGB').save('READY_RESULT.jpg', "JPEG")
img22 = Image.open('READY_RESULT.jpg')
img22.show()