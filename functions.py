from PIL import Image


def int_to_bin(integer: int) -> str:
    """Converts an integer to a binary string.

    Args:
        integer (int): The integer to convert.

    Returns:
        str: The binary string.
    """

    # Convert integer in a binary string of length 8
    binary = bin(integer)[2:].zfill(8)
    return binary


def bin_to_int(binary: str) -> int:
    """Converts a binary string to an integer.

    Args:
        binary (str): The binary string to convert.

    Returns:
        int: The integer.
    """

    # Convert binary string to integer
    integer = int(binary, 2)
    return integer


def char_to_int(character: str) -> int:
    """Converts a character to an integer.

    Args:
        character (str): The character to convert.

    Returns:
        int: The integer.
    """

    # Convert character to integer
    integer = ord(character)
    return integer


def int_to_char(integer: int) -> str:
    """Converts an integer to a character.

    Args:
        integer (int): The integer to convert.

    Returns:
        str: The character.
    """

    # Convert integer to character
    character = chr(integer)
    return character


def string_to_binary(string: str) -> str:
    """Converts a string to a binary string.

    Args:
        string (str): The string to convert.

    Returns:
        str: The binary string.
    """

    # Convert string to binary string
    binary_string = ''.join([int_to_bin(char_to_int(character))
                            for character in string])
    return binary_string


def bin_to_string(binary: str) -> str:
    """Converts a binary string to a string.

    Args:
        binary (str): The binary string to convert.

    Returns:
        str: The string.
    """

    # Convert binary string to string
    string = ''.join([int_to_char(bin_to_int(binary[i:i + 8]))
                      for i in range(0, len(binary), 8)])
    return string


def get_pixel_value(image: Image, x: int, y: int) -> tuple:
    """Gets the pixel value of an image at a given position.

    Args:
        image (Image): The image to get the pixel value from.
        x (int): The x coordinate of the pixel.
        y (int): The y coordinate of the pixel.

    Returns:
        tuple: The pixel value.
    """

    # Get pixel value
    pixel_value = image.getpixel((x, y))
    return pixel_value
