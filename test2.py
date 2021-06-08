# gradients based on http://bsou.io/posts/color-gradients-with-python

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


def linear_gradient(start_hex, finish_hex, n: int, poly: bool):
    s = hex_to_RGB(start_hex)
    f = hex_to_RGB(finish_hex)
    RGB_list = [s]
    for t in range(1, n):
        curr_vector = [
            int(s[j] + (float(t) / (n - 1)) * (f[j] - s[j]))
            for j in range(3)
        ]
        RGB_list.append(curr_vector)
    if poly is True:
        return color_dict(RGB_list)
    else:
        return (RGB_list)


def polylinear_gradient(colors, n):
    n_out = int(float(n) / (len(colors) - 1))
    gradient_dict = linear_gradient(colors[0], colors[1], n_out, poly=True)

    if len(colors) > 1:
        for col in range(1, len(colors) - 1):
            next = linear_gradient(colors[col], colors[col + 1], n_out, poly=True)
            for k in ("hex", "r", "g", "b"):
                gradient_dict[k] += next[k][1:]

    return gradient_dict["hex"]

# color_dict = linear_gradient("#FFC300","#581845")
cd = polylinear_gradient(("#07467A", "#6D027C", "#A0B800","#BD6D00","#07467A"), 500)
print(cd)

