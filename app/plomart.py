import random
import time
import glob
import os
from PIL import Image, ImageDraw

SCRIPT_LOCATION = os.path.realpath(__file__)
PARTS_DIR = os.path.join(os.path.dirname(SCRIPT_LOCATION), 'parts')
IMAGE_WIDTH = 420
IMAGE_HEIGHT = 420


def random_color() -> tuple:
    """ Returns a random color as a tuple """
    return tuple(random.choices(range(256), k=3))


def get_part_files(part) -> list:
    """ Returns a list of files for a part """
    return glob.glob(f"{PARTS_DIR}/{part}*.png")


def paste_image(background: Image, foreground_path: str) -> Image:
    """ Pastes an image onto another

    Arguments:
    background -- Image to use as the background
    foreground_path -- File path to the foreground image

    Returns the combined Image
    """
    foreground = Image.open(foreground_path).convert('RGBA')
    background.paste(foreground, mask=foreground)
    return background


def create_character(background_color, body_color, body, eyes, mouth, nose) -> Image:
    """ Returns an Image containing a character

    Arguments:
    background_color -- (tuple) Color for the background
    body_color -- (tuple) Color for the body
    body -- (str) File path to the body
    eyes -- (str) File path to the eyes
    nose -- (str) File path to the nose
    mouth -- (str) File path to the mouth

    Returns the character as an Image
    """

    # Create the image and draw the background
    image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), background_color)

    # Draw the body
    paste_image(image, body)

    # Fill the body color
    # Use the middle of the image as the starting point
    seed = (220, 220)
    ImageDraw.floodfill(image, seed, body_color)

    # Draw the face
    paste_image(image, eyes)
    paste_image(image, nose)
    paste_image(image, mouth)

    return image


def create_random_character() -> Image:
    """ Returns an Image containing 1 random character and background """
    # Generate a random color for the background and body
    background_color = random_color()
    body_color = random_color()

    # Generate random parts for the body and face
    body = random.choice(get_part_files("body"))
    eyes = random.choice(get_part_files("eyes"))
    mouth = random.choice(get_part_files("mouth"))
    nose = random.choice(get_part_files("nose"))

    return create_character(background_color, body_color, body, eyes, mouth, nose)


def create_collage(columns, rows) -> Image:
    """ Returns a collage of characters as as Image """
    # Create a large canvas
    w = IMAGE_WIDTH * columns
    h = IMAGE_HEIGHT * rows
    image = Image.new("RGB", (w, h))

    # Fill in the characters
    for row in range(0, rows):
        for column in range(0, columns):
            character = create_character()
            x = IMAGE_WIDTH * column
            y = IMAGE_HEIGHT * row
            image.paste(character, (x, y))

    return image


if __name__ == "__main__":
    while True:
        character = create_random_character()
        character.save("output.png")
        time.sleep(0.25)
