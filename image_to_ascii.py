#! /usr/bin/python

from PIL import Image

# ASCII_CHARS = ['#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']

ASCII_CHARS = 'W & U m r 1 | + : .'.split(' ')
ASCII_CHARS.append(' ')

# .'`,^:";~
# -_+<>i!lI?
# /\|()1{}[]
# rcvunxzjft
# LCJUYXZO0Q
# oahkbdpqwm
# *WMB8&%$#@


def scale_image(image, new_width=140):
    """Resizes an image preserving the aspect ratio.
    """

    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width * .4)

    new_image = image.resize((new_width, new_height))
    return new_image


def convert_to_grayscale(image):
    return image.convert('L')


def map_pixels_to_ascii_chars(image, range_width=25):
    """Maps each pixel to an ascii char based on the range
    in which it lies.

    0-255 is divided into 11 ranges of 25 pixels each.
    """

    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ASCII_CHARS[pixel_value/range_width] for pixel_value in
                       pixels_in_image]
    return "".join(pixels_to_chars)


def convert_image_to_ascii(image, new_width=140):
    image = scale_image(image)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width] for index in
                   xrange(0, len_pixels_to_chars, new_width)]

    pic_font = 'wB'
    return pic_font + ("\n" + pic_font).join(image_ascii) + "\n"


def handle_image_conversion(image_filepath):
    image = None
    try:
        image = Image.open(image_filepath)
    except Exception as e:
        print("Unable to open image file {image_filepath}."
              .format(image_filepath=image_filepath))
        print e
        return

    image_ascii = convert_image_to_ascii(image)
    return image_ascii

if __name__ == '__main__':
    import sys

    image_file_path = sys.argv[1]
    handle_image_conversion(image_file_path)

