import random
import time
import glob
import os
from PIL import Image, ImageDraw

PARTS_DIR = "./parts"


def random_color() -> tuple:
    """ Returns a random color as a tuple """
    color = tuple(random.choices(range(256), k=3))
    print(f"Random color: {color}")
    return color


def get_files(part) -> list:
    """ Returns a list of files for a part """
    return glob.glob(f"{PARTS_DIR}/{part}*.png")


def paste_image(background: Image, foreground_path: str) -> None:
    """ Pastes an image onto another

    Arguments:
    background -- Image to use as the background
    foreground_path -- File path to the foreground image
    """

    foreground = Image.open(foreground_path).convert('RGBA')
    background.paste(foreground, mask=foreground)


def create_masterpiece(output_file):
    # Generate a random color for the background
    color = random_color()

    # Create the image and draw the background
    image = Image.new("RGB", (420, 420), color)

    # Draw the body
    paste_image(image, random.choice(get_files("body")))

    # Fill the body color
    # Use the middle of the image as the starting point.
    seed = (220, 220)
    print(f"Color at seed {seed}: {image.getpixel(seed)}")
    body_color = random_color()
    ImageDraw.floodfill(image, seed, body_color)

    # Draw the face
    paste_image(image, random.choice(get_files("eyes")))
    paste_image(image, random.choice(get_files("nose")))
    paste_image(image, random.choice(get_files("mouth")))

    # Save the file
    image.save(output_file)


if __name__ == "__main__":
    output_file = "output.png"
    while True:
        create_masterpiece(output_file)
        time.sleep(0.25)
