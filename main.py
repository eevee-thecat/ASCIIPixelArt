import PIL.Image

COMPLEX = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,"^`". '
SIMPLE = "$@. "


def resize(image, new_width=100):
    width, height = image.size
    new_height = round(new_width * height / width)
    return image.resize((new_width, new_height))


def pixel_to_ascii(image, complex_palette):
    pixels = image.getdata()
    ascii_str = []
    if complex_palette:
        palette = COMPLEX
    else:
        palette = SIMPLE
    for pixel in pixels:
        ascii_str.append(palette[round(pixel // (255 / len(palette)))])
        ascii_str.append(palette[round(pixel // (255 / len(palette)))])
    return "".join(ascii_str)


def main():
    print("Welcome to the ASCII art generator!")
    print(
        """Enter 0 to use a sample Obama picture
Enter 1 to use a sample landscape picture
Enter 2 to use your own picture
"""
    )
    choice = input()
    try:
        choice = int(choice)
        if not 0 <= choice <= 2:
            raise ValueError
    except ValueError:
        print("Please enter a valid choice")
        exit(1)

    print(
        """Enter 0 to use a simple palette
Enter 1 to use a complex palette (not always better)
"""
    )
    palette_choice = input()
    try:
        palette_choice = int(palette_choice)
        if not 0 <= palette_choice <= 2:
            raise ValueError
    except ValueError:
        print("Please enter a valid choice")
        exit(1)

    match choice:
        case 0:
            image = PIL.Image.open("obama.jpg")
        case 1:
            image = PIL.Image.open("landscape.webp")
        case 2:
            path = input("Please enter the path to the picture you'd like to use: \n")
            image = PIL.Image.open(path)

    greyscale_image = resize(image.convert("L"))

    ascii_str = pixel_to_ascii(greyscale_image, bool(palette_choice))
    img_width = greyscale_image.width * 2
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i : i + img_width] + "\n"

    print(ascii_img)


if __name__ == "__main__":
    main()
