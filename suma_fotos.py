from PIL import Image, ImageChops as ic
# from PIL import ImageChops as ic
import random

def xoreador(imagen_a, imagen_b):
    datos_a = imagen_a.getdata()
    datos_b = imagen_b.getdata()
    datos_new = [0]*len(datos_a)
    # for r,g,b in datos_a:
    for i, ((ra, ga, ba), (rb, gb, bb)) in enumerate(zip(datos_a, datos_b)):
        datos_new[i] = (ra^rb, ga^gb, ba^bb) 
    image_new = Image.new('RGB', imagen_b.size, 255)
    image_new.putdata(datos_new)
    return image_new
    
def imagen_ruidosa(width, height):
    pil_map = Image.new('RGB', (width, height), 255)
    ruidosidad = map(lambda x: (
        int(random.random()*256),
        int(random.random()*256),
        int(random.random()*256)), [0] * width * height)
    pil_map.putdata(ruidosidad)
    return pil_map

im_source_b = Image.open('b.png')
im_source_a = Image.open('a.png')
width, height = im_source_b.size
im_ruidin = imagen_ruidosa(width, height)
# xoreador(im_source, im_ruidin)


im_ruidin.save('bla.png')
im_encryptada = xoreador(im_source_a, im_ruidin)
im_encryptada.save('encris.png')
im_encryptada_chafa = xoreador(im_source_a, im_source_b)
im_encryptada_chafa.save('encris_chafa.png')

im_recuperada = xoreador(im_encryptada, im_ruidin)
im_recuperada.save('me_deben_unos_chilaquiles.png')
