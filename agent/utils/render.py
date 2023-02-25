import gradio as gr
from colorsys import hsv_to_rgb


class Render:
    def hsv_to_html(self, hsv):
        # Convert the HSV values to RGB values
        rgb = tuple(
            int(i * 255)
            for i in hsv_to_rgb(
                hsv["hue"] / 360, hsv["saturation"] / 100, hsv["value"] / 100
            )
        )

        # Create an HTML element with the desired color as its background
        html = f"<div style='background-color: rgb{rgb}; width: 100px; height: 100px;'></div>"
        return html

    def render_color(self, hsv):
        # Launch the Gradio interface in a temporary web page
        print("hsv: \n")
        print(hsv)
        demo = gr.Interface(
            self.hsv_to_rgb, inputs=gr.JSON(hsv), outputs=gr.outputs.HTML()
        )
        output = demo.launch()
        print("output")
        print(output)
