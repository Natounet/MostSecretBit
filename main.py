import functions
from PIL import Image

"""
MSB - Most Secure Bit
Author: Nathan CORNELOUP
Date: 07/05/2023

This program allows you to hide a secret message in an image, as well as recover a secret message from an image.
"""

def init():
    """ Initializes the program and variables """

    print("  __  __ ___ ___         __  __        _     ___                 _     ___ _ _   ")
    print(" |  \/  / __| _ )  ___  |  \/  |___ __| |_  / __| ___ __ _ _ ___| |_  | _ |_) |_ ")
    print(" | |\/| \__ \ _ \ |___| | |\/| / _ (_-<  _| \__ \/ -_) _| '_/ -_)  _| | _ \ | _|")
    print(" |_|  |_|___/___/       |_|  |_\___/__/\__| |___/\___\__|_| \___|\__| |___/_|\__|")

    print("Welcome on MSB, the Most Secure Bit program !")
    print("This program allows you to hide a secret message in an image.")
    print("You can also recover a secret message from an image.")

    print("1) Hide a secret in an image")
    print("2) Recover a secret from an image")

    choice = str(input("> ")).strip()

    # Hide secret
    if (choice == "1"):
        path = str(input("Path to the image: ")).strip()
        secret = str(input("Secret to hide: ")).strip()
        output_path = str(
            input("Path to the output image (must end with .png): ")).strip()

        print("Do you want to use custom ending character ? (y/n)")
        if (str(input("> ")).strip() == "y"):
            ending_char_bin = str(
                input("Ending character (binary code): ")).strip()
        else:
            ending_char_bin = "00000000"  # NULL character

        image = Image.open(path)
        hide_secret(image, secret, ending_char_bin, output_path)

    # Recover secret
    if (choice == "2"):
        path = str(input("Path to the image: ")).strip()

        print("Do you want to use custom ending character ? (y/n)")
        if (str(input("> ")).strip() == "y"):
            ending_char_bin = str(
                input("Ending character (binary code): ")).strip()
        else:
            ending_char_bin = "00000000"  # NULL character

        image = Image.open(path)
        print(recover_secret(image, ending_char_bin))


def hide_secret(image: Image, secret: str, ending_char_bin: str, output: str) -> None:
    """Hides a secret in an image.

    Args:
        image (Image): The image to hide the secret in.
        secret (str): The secret to hide.
        ending_char_bin (str): The binary code of the ending character.
        output (str): The path to the output image.
    """

    # 1) We need to convert the secret to a binary string
    binary_secret = functions.string_to_binary(secret)+ending_char_bin
    i = 0
    # In each pixels, we can hide 3 bits, so we need to check if the image is big enough
    if len(binary_secret) > image.width * image.height * 3:
        raise ValueError("Image is too small to hide the secret.")

    # 2) Iterate over the pixels of the image
    print("Hiding secret...")
    for x in range(image.width):
        for y in range(image.height):

            (r, g, b) = functions.get_pixel_value(image, x, y)
            (rb, gb, bb) = (functions.int_to_bin(r),
                            functions.int_to_bin(g), functions.int_to_bin(b))
            (rb, gb, bb) = (list(rb), list(gb), list(bb))

            # 2.1) Hide the secret in the pixels
            if (i < len(binary_secret)):
                rb[-1] = binary_secret[i]
                i += 1

            if (i < len(binary_secret)):
                gb[-1] = binary_secret[i]
                i += 1

            if (i < len(binary_secret)):
                bb[-1] = binary_secret[i]
                i += 1

            # 2.2) Convert the pixels back to integers
            r = functions.bin_to_int(''.join(rb))
            g = functions.bin_to_int(''.join(gb))
            b = functions.bin_to_int(''.join(bb))

            # 2.3) Set the new pixel value
            image.putpixel((x, y), (r, g, b))

            if (i >= len(binary_secret)):
                break

    # 4) Save the image
    print("Saving image...")
    image.save(output)
    print("Image saved as " + output)


def recover_secret(image: Image, ending_char_bin: str) -> str:
    """Recovers a secret from an image.

    Args:
        image (Image): The image to recover the secret from.
        ending_char_bin (str): The binary code of the ending character.

    Returns:
        str: The secret.
    """
    binary_secret = ""

    # 1) Iterate over the pixels of the image
    for x in range(image.width):
        for y in range(image.height):

            (r, g, b) = functions.get_pixel_value(image, x, y)
            (rb, gb, bb) = (functions.int_to_bin(r),
                            functions.int_to_bin(g), functions.int_to_bin(b))
            (rb, gb, bb) = (list(rb), list(gb), list(bb))

            # 1.1) Recover the secret from the pixels
            binary_secret += rb[-1]

            # 1.2) Check if the secret is complete
            if (binary_secret[-8:] == ending_char_bin):
                return functions.bin_to_string(binary_secret[:-8])

            binary_secret += gb[-1]
            if (binary_secret[-8:] == ending_char_bin):
                return functions.bin_to_string(binary_secret[:-8])

            binary_secret += bb[-1]
            if (binary_secret[-8:] == ending_char_bin):
                return functions.bin_to_string(binary_secret[:-8])

    # Raise exception if no secret was found
    raise ValueError("No secret was found in the image.")


init()
