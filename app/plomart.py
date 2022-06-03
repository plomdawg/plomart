import random
import time
import glob
import os
from PIL import Image, ImageDraw
from pathlib import Path

SCRIPT_LOCATION = os.path.realpath(__file__)
PARTS_DIR = os.path.join(os.path.dirname(SCRIPT_LOCATION), 'parts')
IMAGE_WIDTH = 420
IMAGE_HEIGHT = 420


class Part:
    def __init__(self, kind, path):
        # body, eyes, mouth, or nose
        self.kind = kind
        # path to the .png (e.g. "parts/nose2.png")
        self.path = Path(path)
        # name (e.g. "nose2")
        self.name = self.path.name[0:-4]
        # number (e.g. "2")
        self.number = self.name[-1:]
        # open the image file
        self.image = Image.open(self.path).convert('RGBA')


def get_parts(part) -> list:
    """ Returns a list of Part for some type """
    return [Part(kind=part, path=file_path) for file_path in glob.glob(f"{PARTS_DIR}/{part}*.png")]


# Load the part files.
BODY_PARTS = get_parts("body")
EYES_PARTS = get_parts("eyes")
MOUTH_PARTS = get_parts("mouth")
NOSE_PARTS = get_parts("nose")


def random_color() -> tuple:
    """ Returns a random color as a tuple """
    return tuple(random.choices(range(256), k=3))


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
    image.paste(body.image, mask=body.image)

    # Fill the body color
    # Use the middle of the image as the starting point
    seed = (220, 220)
    ImageDraw.floodfill(image, seed, body_color)

    # Draw the face
    image.paste(eyes.image, mask=eyes.image)
    image.paste(nose.image, mask=nose.image)
    image.paste(mouth.image, mask=mouth.image)

    return image


def create_random_character() -> Image:
    """ Returns an Image containing 1 random character and background """
    # Generate a random color for the background and body
    background_color = random_color()
    body_color = random_color()

    # Generate random parts for the body and face
    body = random.choice(BODY_PARTS)
    eyes = random.choice(EYES_PARTS)
    mouth = random.choice(MOUTH_PARTS)
    nose = random.choice(NOSE_PARTS)

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
            character = create_random_character()
            x = IMAGE_WIDTH * column
            y = IMAGE_HEIGHT * row
            image.paste(character, (x, y))

    return image


if __name__ == "__main__":
    create_collage(5, 5).save("collage.png")
    print("created random collage: collage.png")
    create_random_character().save("output.png")
    print("created random character: output.png")
    # while True:
    #    create_random_character().save("output.png")
    #    print("created random character")
    #    time.sleep(0.25)
