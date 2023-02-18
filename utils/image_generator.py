from PIL import Image
from PIL import ImageColor
from colorsys import hsv_to_rgb
import json


class ImageGenerator:
    def generate_image(self, hsv):
        # Convert the HSV values to RGB values
        print("\n hsv output 2:\n")
        print(hsv)
        # rgb = tuple(
        #     int(i * 255)
        #     for i in hsv_to_rgb(
        #         hsv["hue"] / 360, hsv["saturation"] / 100, hsv["value"] / 100
        #     )
        # )
        hsv_dict = json.loads(hsv)
        hue = hsv_dict["hue"]
        saturation = hsv_dict["saturation"]
        value = hsv_dict["value"]
        hsv_color_string = f"hsv({hue},{saturation}%,{value}%)"
        rgb_color = ImageColor.getrgb(hsv_color_string)

        # Create a new image with the desired color
        img = Image.new("RGB", (100, 100), rgb_color)

        return img
