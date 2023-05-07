# MSB - Most Secret Bit

Most Secret Bit is a user-friendly Python program that allows users to hide secret messages within an image or retrieve them from an image. This program uses a technique called Least Significant Bit (LSB) to hide information within the pixels of an image.

## How does it work ? 

To hide a secret message, the program converts the message to a binary string and embeds it within the least significant bits of the RGB color values of the image pixels.<br>
This process is done in a way that is invisible to the naked eye, so the image looks unchanged.<br>
The user can also specify a custom ending character in binary format.

To retrieve a secret message, the program extracts the least significant bits of the RGB color values of the image pixels and converts them to binary.<br>
The program then searches for the ending character and returns the secret message as a string.

## How to use the program ? 

Before using Most Secure Bit, make sure to install the Pillow package which is used to handle images:

`python3 -m pip install pillow`

Once installed, clone the repository using :<br>
`git clone https://github.com/Natounet/MostSecretBit.git`

Then simply launch the "main.py" file and follow the console-based menu to hide or retrieve your secret message.

![](https://github.com/Natounet/MostSecureBit/blob/main/menu.gif)
