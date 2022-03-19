from PIL import Image

# Path for your image where it is
image_1 = Image.open(
    r'F:\Sem 4\CE259-PIP\-result.JPG')

# Converting it into pdf
im_1 = image_1.convert('RGB')

# Path where your PDF file will bw saved
im_1.save(r'F:\Sem 4\CE259-PIP\PIP_Practical 10\PIP_Practical 10.pdf')