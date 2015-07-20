from PIL import Image
import sys

name = sys.argv[1]

which = {0 : 'Top', 1 : 'Mid' , 2 : 'Bot' }

image = Image.open(name)
(width, height) = image.size
s_height = height/3

for i in range(3):
    temp = image.copy()
    temper = temp.crop((0, i*s_height, width, (i+1)*s_height))
    temper.save('%s/%s' % (which[i], name))