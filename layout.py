from extensions.OobaCoder.block import Block, InputBlock, OutputBlock, BlockType

blocks_json_defaults = {
    'x' : 0,
    'y' : 0
}

class Layout:
    def __init__(self):
        self.blocks = []
        self.new_block_params = {}
        self.new_block_label = ""
        self.new_block_type_name = ""

    def to_html(self):
        html_string = """<div class="layout">"""
        for block in self.blocks:
            html_string += block.to_html()
        html_string += "</div>"
        return html_string

    def new_block(self, blocks_json):
        blocks_dict = json.loads(blocks_json)
        print(self.new_block_type_name)
        if self.new_block_type_name == "INPUT":
            block = InputBlock()
        elif self.new_block_type_name == "OUTPUT":
            block = OutputBlock()
        else:
            return blocks_json
        self.blocks.append(block)
        blocks_dict[block.id] = blocks_json_defaults.copy()
        return json.dumps(blocks_dict)
        