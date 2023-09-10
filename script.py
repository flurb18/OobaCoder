import gradio as gr
from pathlib import Path

from extensions.OobaCoder.block import BlockType
from extensions.OobaCoder.layout import Layout

params = {
    "display_name" : "OobaCoder",
    "is_tab" : True
}

OobaCoderDir = Path(__file__).parent

with open(str(OobaCoderDir.joinpath("drag.js")), "r") as f:
    drag_js = f.read().strip()

layout = Layout()

def ui():
    with gr.Row():
        with gr.Column(scale=1):
            # Menu
            with gr.Accordion(label="New Block"):
                with gr.Row():
                    new_block_type_picker = gr.Dropdown(label="Block Type", choices=[bt.name for bt in BlockType])
                    new_block_label = gr.Textbox(label="Block Label", interactive=True)
                    new_block_submit = gr.Button("Create Block")
                new_block_params_labeled = [
                    ( "INPUT-type", gr.Dropdown(label="Input Type", choices=["Upload File", "Input Text"], visible=False) ),
                    ( "INPUT-text", gr.Textbox(label="Input Text", interactive=True, visible=False) ),
                    ( "OUTPUT-type", gr.Dropdown(label="Output Type", choices=["View Text", "Download As File"], visible=False) )
                ]
                new_block_param_names = [i[0] for i in new_block_params_labeled]
                new_block_params = [i[1] for i in new_block_params_labeled]

        with gr.Column(scale=2):
            # Display
            output = gr.HTML(value="")

    def show_block_type_menu(block_type_name):
        return [gr.update(visible=True) if n.startswith(block_type_name) else gr.update(visible=False) for n in new_block_param_names]

    new_block_type_picker.input(
        show_block_type_menu,
        inputs=[new_block_type_picker],
        outputs=new_block_params
    )

    newest_block_id = gr.State("")
    new_block_submit.click(
        layout.new_block,
        inputs=[new_block_label, new_block_type_picker]+new_block_params,
        outputs=[output, newest_block_id]
    ).then(
        None,
        inputs = [newest_block_id],
        outputs = None,
        _js = drag_js
    )

def custom_css():
    with open(str(OobaCoderDir.joinpath("custom.css")), "r") as f:
        css_string = f.read().strip()
    return css_string