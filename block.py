import gradio as gr
from enum import Enum
import secrets

class BlockType(Enum):
    INPUT = 0
    OUTPUT = 1
    SPLIT = 2
    COMBINE = 3
    CONDITIONAL = 4

class Block:
    def __init__(self, heading: str, label: str):
        self.heading = heading
        self.label = label
        self.id = secrets.token_hex(16)

    def html_contents():
        return f"<p>{self.label}</p>"

    def to_html(self):
        html_string = f"""
<div id="{self.id}" class="block">
  <div id="{self.id}header" class="block-header">{self.heading}</div>
  {self.html_contents()}
</div>
""".strip()
        return html_string

class InputBlock(Block):
    def __init__(self):
        super().__init__("INPUT", "Input Block")


class OutputBlock(Block):
    def __init__(self):
        super().__init__("OUTPUT", "Output Block")