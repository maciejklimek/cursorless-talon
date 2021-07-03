from talon import Context, Module

mod = Module()
ctx = Context()

ctx.matches = r"""
app: vscode
"""

mod.list("cursorless_symbol_color", desc="Supported symbol colors for token jumping")

ctx.lists["self.cursorless_symbol_color"] = {
    "gray": "default",
    "blue": "blue",
    "green": "green",
    "rose": "red",
    "squash": "yellow",
    "plum": "purple",
}
