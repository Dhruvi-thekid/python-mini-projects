# image size dimensions in gif

import imageio.v3 as iio
import os
from PIL import Image
from PIL import ImageOps

# Desired GIF size (width, height)
SIZE = (300, 300)

filenames = ['marvel_spider.png', 'cake_spider.png', 'yo_spider.png']
images = []

for filename in filenames:
    img = Image.open(filename)
    #img = img.resize(SIZE, Image.LANCZOS)   # resize
    img = ImageOps.fit(img, SIZE, Image.LANCZOS)
    images.append(img)

# Save GIF
images[0].save(
    'team.gif',
    save_all=True,
    append_images=images[1:],
    duration=500,
    loop=0
)

if os.path.exists("team.gif"):
    print("GIF created successfully: team.gif")
