def hex_to_RGB(hex):
    return [int(hex[i:i + 2], 16) for i in range(1, 6, 2)]


def RGB_to_hex(RGB):
    RGB = [int(x) for x in RGB]
    return "#" + "".join(["0{0:x}".format(v) if v < 16 else
                          "{0:x}".format(v) for v in RGB])


def color_dict(gradient):
    return {"hex": [RGB_to_hex(RGB) for RGB in gradient],
            "r": [RGB[0] for RGB in gradient],
            "g": [RGB[1] for RGB in gradient],
            "b": [RGB[2] for RGB in gradient]}


def speed(spee):
    if spee == 10:
        speed_after = 0.001
    elif spee == 9:
        speed_after = 0.009
    elif spee == 8:
        speed_after = 0.03
    elif spee == 7:
        speed_after = 0.05
    elif spee == 6:
        speed_after = 0.07
    elif spee == 5:
        speed_after = 0.09
    elif spee == 4:
        speed_after = 0.12
    elif spee == 3:
        speed_after = 0.5
    elif spee == 2:
        speed_after = 1
    elif spee == 1:
        speed_after = 3
    elif spee == 0:
        speed_after = False
    else:
        speed_after = False
    return speed_after
