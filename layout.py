from extensions.OobaCoder.block import Block, InputBlock, OutputBlock, BlockType

class Layout:
    def __init__(self):
        self.blocks = []

    def to_html(self):
        html_string = """<div>"""
        for block in self.blocks:
            html_string += block.to_html()
        html_string += "</div>"
        return html_string

    def new_block(self, label, block_type_name, input_type, input_text, output_type):
        if block_type_name == "INPUT":
            block = InputBlock()
        elif block_type_name == "OUTPUT":
            block = OutputBlock()
        self.blocks.append(block)
        return self.to_html()
