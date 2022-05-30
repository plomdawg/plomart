import random
import time
import glob
import os
from PIL import Image, ImageDraw

PARTS_DIR = "./parts"
IMAGE_WIDTH = 420
IMAGE_HEIGHT = 420


def random_color() -> tuple:
    """ Returns a random color as a tuple """
    color = tuple(random.choices(range(256), k=3))
    print(f"Random color: {color}")
    return color


def get_files(parts_path, part) -> list:
    """ Returns a list of files for a part """
    return glob.glob(f"{parts_path}/{part}*.png")


def paste_image(background: Image, foreground_path: str) -> None:
    """ Pastes an image onto another

    Arguments:
    background -- Image to use as the background
    foreground_path -- File path to the foreground image
    """

    foreground = Image.open(foreground_path).convert('RGBA')
    background.paste(foreground, mask=foreground)


def create_character(parts_path) -> Image:
    """ Returns an Image containing 1 random character and background """
    # Generate a random color for the background
    color = random_color()

    # Create the image and draw the background
    image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), color)

    # Draw the body
    paste_image(image, random.choice(get_files(parts_path, "body")))

    # Fill the body color
    body_color = random_color()

    # Use the middle of the image as the starting point.
    seed = (220, 220)
    ImageDraw.floodfill(image, seed, body_color)

    # Draw the face
    nose = random.choice(get_files(parts_path, "nose"))
    mouth = random.choice(get_files(parts_path, "mouth"))
    eyes = random.choice(get_files(parts_path, "eyes"))
    print(f"Face: {eyes} {nose} {mouth}")
    paste_image(image, eyes)
    paste_image(image, nose)
    paste_image(image, mouth)

    return image


def create_collage(columns, rows) -> Image:
    # Create a large canvas
    image = Image.new("RGB", (IMAGE_WIDTH * columns, IMAGE_HEIGHT * rows))

    # Fill in the characters
    for row in range(0, rows):
        for column in range(0, columns):
            character = create_character()
            x = IMAGE_WIDTH * column
            y = IMAGE_HEIGHT * row
            image.paste(character, (x, y))

    return image


if __name__ == "__main__":
    output_file = "output.png"
    # collage.save(output_file)

    while True:
        character = create_character()
        character.save(output_file)
        time.sleep(0.25)
