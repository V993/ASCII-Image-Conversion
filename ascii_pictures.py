
from os import major
from typing import NewType, Tuple
from PIL import Image, ImageOps
from sys import argv
from termcolor import colored, cprint
import termcolor

MAXIMUM_CHANNELS = 255 * 4

Pixel = NewType("Pixel", Tuple[int,int,int,int])

CHARACTERS =        ('  ', ', ', '; ', '* ', 'o ', ') ', '/ ', '0 ', '$ ', '@ ')
CHARACTERS_PACKED = ('  ', ',,', ';;', '**', 'oo', '))', '//', '00', '$$', '@@')
BINARY = ('1','0')

HTML_START= """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ASCII Art</title>
</head>
<body>
    <div style="background-color: black; color: white;">
        <pre>{}</pre>
    </div>
</body>
</html>
"""

# return the intensity of a given pixel
def get_intensity(pixel: Pixel) -> float:
    return ( sum(pixel) / MAXIMUM_CHANNELS )

# return the main color in a single pixel
def get_major_color(pixel: Pixel) -> int:
    max_value = max(pixel)
    max_index = pixel.index(max_value)

    if max_value < 50:
        return 3

    return max_index

# return the appropriate character for this particular intensity
def get_character(intensity: float) -> CHARACTERS:

    intensity_char = round(intensity * len(CHARACTERS))
    return CHARACTERS_PACKED[ intensity_char ]

    # Adaptable:
    # if (intensity_char > len(CHARACTERS) // 5):
    #     return CHARACTERS_PACKED[ intensity_char ]
    # else:
    #     return CHARACTERS[ intensity_char ]

# convert input image into a string of characters
def convert_image(image: Image) -> str:

    image_as_string = ''
    colors_of_image = ''

    for pixel in image.getdata():
        intensity = get_intensity(pixel)
        character = get_character(intensity)
        major_color = get_major_color(pixel)
        image_as_string += character
        colors_of_image += str(major_color)*2

    return image_as_string, colors_of_image

# output converted image properly:
def display_image(size: Tuple[int, int], image_string: str, colors: str):
    index = 0
    for _ in range(size[1]):
        # print without color:
        # print(image_string[index:index+size[0]*2])

        # print with color:
        line = image_string[index:index+size[0]*2]
        # flag = True
        for loc,c in enumerate(line):
            pixel_color = colors[loc+index]

            
            # if loc < len(line)-4 and flag:
            #     if line[loc-3] != ' ' and line[loc-2] != ' ' and line[loc-1] != ' ' and c != ' ' \
            #                 and line[loc+1] != ' ' and line[loc+2] != ' ' and line[loc+3] != ' ':
            #         print('dope', end='')
            #         loc += 4
            #         flag = False
            #         continue

            if pixel_color == '0':
                cprint(c,'red', attrs=['bold'], end='')
            if pixel_color == '1':
                cprint(c, 'green', attrs=['bold'], end='')
            if pixel_color == '2':
                cprint(c, 'blue', attrs=['bold'], end='')
            elif pixel_color == '3':
                print(' ', end='')
            # else:
            #     print("e ")


            # print(pixel_color, end='')
            
        print()

        # cprint(line, 'red', 'on_blue')
        index += size[0]*2


# save an html file that can be properly viewed
def save_html(name: str, image_string: str, size: Tuple[int,int]):
    with open(name+".html", 'w') as html_file:
        html_image = ""
        index = 0

        for _ in range(size[1]):
            html_image += image_string[index:index+size[0]*2] + '\n'
            index += size[0]*2

        # write to file:
        # print(html_image)
        html_file.write(HTML_START.format(html_image))


def main():
    image_to_be_converted = argv[1]
    # convert image to 50*50 for readability
    basewidth = int(argv[2])
    img = Image.open(image_to_be_converted)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)

    if argv[3]:
        if argv[3] == "invert":
            img = ImageOps.invert(img)

    # img.save('resized_image.jpg')
    
    # cprint('this should be red','red','on_blue')

    ascii_image_string,colors = convert_image(img)

    # uncomment to display in terminal alone:
    display_image(img.size, ascii_image_string, colors)

    # save to html
    save_html(image_to_be_converted, ascii_image_string, img.size)



if __name__ == "__main__":
    main()


