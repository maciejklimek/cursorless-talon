from talon import Context, Module

mod = Module()
ctx = Context()

ctx.matches = r"""
app: vscode
"""

mod.list("cursorless_sub_component_type", desc="Supported subcomponent types")

ctx.lists["self.cursorless_sub_component_type"] = {
    "word": "subtoken",
    "char": "character"
}
