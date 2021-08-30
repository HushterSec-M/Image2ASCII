import matplotlib.pylab as plt
from PIL import Image

# filename = r'C:\Users\HYPERPC\Desktop\Screenshot_2.png'
filename = r'images/1.png'

img = Image.open(filename).convert('LA')
img.save('grayscale.png')

img = plt.imread('grayscale.png')

alpha = ['.', ',', ':', '+', '*', '?', '%', 'S', '#', '@']

print(img)

grayscale_img = []

result_str = ''

for row in img:
    for pixel in row:
        char = alpha[0] if str(pixel[0])[0] == 1 else alpha[int(str(pixel[0])[2])]
        print(char, end='')
        result_str += char
    print()
    result_str += '\n'


with open('result.txt', 'w') as f:
    f.write(result_str)
