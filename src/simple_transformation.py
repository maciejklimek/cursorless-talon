from talon import Context, Module
from .matching_transformation import matching_transformation

mod = Module()
ctx = Context()

ctx.matches = r"""
app: vscode
"""

simple_transformations = [
    matching_transformation
]

mod.list("cursorless_simple_transformations", desc="simple transformations")
ctx.lists["self.cursorless_simple_transformations"] = {
    transformation.term for transformation in simple_transformations
}

@mod.capture(rule="{user.cursorless_simple_transformations}")
def cursorless_simple_transformations(m) -> str:
    return simple_transformations[m.cursorless_simple_transformations]
