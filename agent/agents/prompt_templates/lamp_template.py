lamp_template = """
I want you to translate an aesthetic into a "brightness" and "color" value. Your response should be formatted in JSON as follows: 

{"set_microworld_state": {"brightness": "<brightness-value-string>"", "color": "<color-value-string>"}}

The only things you should modify are <brightness-value-string> and <color-value-string>.
What is a brightness and color value that represents {aesthetic}?
"""

