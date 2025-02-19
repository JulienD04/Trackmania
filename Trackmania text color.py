def hex_to_short_hex(hex_color: str):
    hex_color = hex_color.removeprefix('0x')
    hex_color = hex_color.removeprefix('#')
    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)

    red = hex(int(red / 16))
    green = hex(int(green / 16))
    blue = hex(int(blue / 16))
    return '$' + red.removeprefix('0x') + green.removeprefix('0x') + blue.removeprefix('0x')


def main():
    entre = '000000'
    while entre != '':
        print(hex_to_short_hex(entre))
        entre = input('Hex: ')


if __name__ == '__main__':
    main()
