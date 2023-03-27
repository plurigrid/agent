import gradio as gr


class Gradio:
    def __init__(self, msg_handler):
        self.msg_handler = msg_handler

    def run(self):
        iface = gr.Interface(
            fn=self.msg_handler,
            inputs=gr.inputs.Textbox(label="..."),
            outputs="text",
            title="Agent",
            description="GM!",
        )
        iface.launch(share=True)
