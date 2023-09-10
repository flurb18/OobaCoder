import gradio as gr
from pathlib import Path

from extensions.OobaCoder.block import BlockType
from extensions.OobaCoder.layout import Layout

params = {
    "display_name" : "OobaCoder",
    "is_tab" : True
}

OobaCoderDir = Path(__file__).parent

js_funcs = {
    "process_blocks" : "",
    "save_blocks_pos" : ""
}

for js_func_name in js_funcs.keys():
    with open(str(OobaCoderDir.joinpath(js_func_name+".js")), "r") as f:
        js_funcs[js_func_name] = f.read().strip()

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

    blocks_json = gr.Textbox(value="{}",visible=False)
    new_block_submit.click(
        None,
        inputs = [blocks_json],
        ouptuts = [blocks_json],
        _js = js_funcs["save_blocks_pos"]
    ).then(
        layout.new_block,
        inputs=[blocks_json, new_block_label, new_block_type_picker]+new_block_params,
        outputs=[blocks_json]
    ).then(
        layout.to_html,
        inputs=None,
        outputs=[output]
    ).then(
        None,
        inputs = [blocks_json],
        outputs = None,
        _js = js_funcs["process_blocks"]
    )

def custom_css():
    with open(str(OobaCoderDir.joinpath("custom.css")), "r") as f:
        css_string = f.read().strip()
    return css_string