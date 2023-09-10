from extensions.OobaCoder.block import Block, InputBlock, OutputBlock, BlockType

blocks_json_defaults = {
    'x' : 1000,
    'y' : 1000
}

class Layout:
    def __init__(self):
        self.blocks = []

    def to_html(self):
        html_string = """<div class="layout">"""
        for block in self.blocks:
            html_string += block.to_html()
        html_string += "</div>"
        return html_string

    def new_block(self, blocks_json, label, block_type_name, input_type, input_text, output_type):
        blocks_dict = json.loads(blocks_json)
        if block_type_name == "INPUT":
            block = InputBlock()
        elif block_type_name == "OUTPUT":
            block = OutputBlock()
        else:
            return blocks_json
        self.blocks.append(block)
        blocks_dict[block.id] = blocks_json_defaults.copy()
        return json.dumps(blocks_dict)
        