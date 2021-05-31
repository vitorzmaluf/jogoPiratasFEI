from PIL import Image, ImageOps
import glob


images = glob.glob('C:/Users/vinia/Desktop/jogoPiratasFEI/todasImagens/PNG/2/walk/*.png')
#images = glob.glob('C:/Users/vinia/Desktop/jogoPiratasFEI/todasImagens/PNG/2/attack/*.png')


print(images)
for image in images:
    '''im = Image.open(image)
    im = im.resize((100, 100))
    im.save(image)'''


    if 'walk_left' in image:
        im = Image.open(image)
        im_mirror = ImageOps.mirror(im)
        im_mirror.save(image, quality=95)