from apa102_pi.driver import apa102
from colour import Color
import time
from helpers import *


class Rainbow:
    def __init__(self, num_led: int, strip: apa102.APA102):
        self.rainbow = [[148, 0, 211], [75, 0, 130], [0, 0, 255], [0, 255, 0], [255, 255, 0], [255, 127, 0], [255, 0, 0]]
        self.strip = strip
        self.num_led = num_led

    def set_rainbow(self, amount):
        led_per_color = int(self.num_led / 14)
        x = 1
        for i in range(1, amount):
            for col in self.rainbow:
                for led in range(1, led_per_color + 1):
                    red = col[0]
                    green = col[1]
                    blue = col[2]
                    self.strip.set_pixel(x, red, green, blue)
                    x += 1
        while x <= self.num_led:
            self.strip.set_pixel(x, self.rainbow[0][0], self.rainbow[0][1], self.rainbow[0][2])
            x += 1
        self.strip.show()

    def breathing(self, spe: int, amount):
        self.set_rainbow(amount)
        spee = speed(spe)
        if spee is not False:
            brightness = 31
            while True:
                self.strip.set_global_brightness(brightness)
                self.strip.show()
                if brightness <= 0:
                    brightness += 1
                else:
                    brightness -= 1
                time.sleep(spee)

    def heart_breathe(self, spe: int, amount):
        self.set_rainbow(amount)
        spee = speed(spe)
        if spee is not False:
            while True:
                self.strip.rotate()
                self.strip.show()

    def moving(self, spe: int, amount):
        self.set_rainbow(amount)
        spee = speed(spe)
        if spee is not False:
            while True:
                self.strip.rotate()
                self.strip.show()
                time.sleep(spee)


class Color_Gradient:
    def __init__(self, num_led: int, strip: apa102.APA102):
        self.num_led = num_led
        self.strip = strip

    def linear_gradient(self, start_hex, finish_hex, num: int, poly: bool):
        s = hex_to_RGB(start_hex)
        f = hex_to_RGB(finish_hex)
        RGB_list = [s]
        for t in range(1, num):
            curr_vector = [
                int(s[j] + (float(t) / (num - 1)) * (f[j] - s[j]))
                for j in range(3)
            ]
            RGB_list.append(curr_vector)
        if poly is True:
            return color_dict(RGB_list)
        else:
            for col in RGB_list:
                self.strip.set_pixel_rgb(RGB_list.index(col)+1, col)
            self.strip.show()

    def gradient_list(self, colors: list, num):
        n_out = int(float(num) / (len(colors) - 1))
        gradient_dict = self.linear_gradient(colors[0], colors[1], n_out, poly=True)

        if len(colors) > 1:
            for col in range(1, len(colors) - 1):
                nex = self.linear_gradient(colors[col], colors[col + 1], n_out, poly=True)
                for k in ("hex", "r", "g", "b"):
                    gradient_dict[k] += nex[k][1:]
        for col in gradient_dict["hex"]:
            self.strip.set_pixel_rgb(gradient_dict["hex"].index(col) + 1, col)
        self.strip.show()

    def blue_green(self):
        blue = Color("blue").get_hex()
        green = Color("green").get_hex()
        self.linear_gradient(blue, green, self.num_led, poly=False)

    def green_blue(self):
        green = Color("green").get_hex()
        blue = Color("blue").get_hex()
        self.linear_gradient(green, blue, self.num_led, poly=False)

    def blue_red(self):
        blue = Color("blue").get_hex()
        red = Color("red").get_hex()
        self.linear_gradient(blue, red, self.num_led, poly=False)

    def red_blue(self):
        red = Color("red").get_hex()
        blue = Color("blue").get_hex()
        self.linear_gradient(red, blue, self.num_led, poly=False)

    def green_red(self):
        green = Color("green").get_hex()
        red = Color("red").get_hex()
        self.linear_gradient(green, red, self.num_led, poly=False)

    def red_green(self):
        red = Color("red").get_hex()
        green = Color("green").get_hex()
        self.linear_gradient(red, green, self.num_led, poly=False)
