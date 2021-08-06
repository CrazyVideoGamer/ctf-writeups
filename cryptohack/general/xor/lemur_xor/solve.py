from PIL import Image
from PIL import ImageChops

flag_xored = Image.open("flag.png")
lemur_xored = Image.open("lemur.png")

flag_pixels = flag_xored.load()
lemur_pixels = lemur_xored.load()

width, height = flag_xored.size # flag.png and lemur.png have same width & height

flag_xor_lemur = Image.new("RGB", (width, height), "black") # this will contain flag_original xor lemur_original (because the 2 secret key xor's are canceled out from the flag_xored and the lemur_xored). This is good because then we dont have the key anymore.
new_image_pixels = flag_xor_lemur.load()

for i in range(width):
    for j in range(height):

        r1, g1, b1 = flag_pixels[i, j]
        r2, g2, b2 = lemur_pixels[i, j]
        
        #print(r1, g1, b1, "and", r2, g2, b2)

        new_image_pixels[i, j] = (r1 ^ r2, g1 ^ g2, b1 ^ b2)

flag_xor_lemur.save("result.png")

flag_xored.close()
lemur_xored.close()
flag_xor_lemur.close()
