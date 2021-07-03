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


@mod.capture(rule="[{user.cursorless_symbol_color}] <user.any_alphanumeric_key>")
def cursorless_decorated_symbol(m) -> str:
    """A decorated symbol"""
    try:
        symbol_color = m.cursorless_symbol_color
    except AttributeError:
        symbol_color = "default"

    return {
        "mark": {
            "type": "decoratedSymbol",
            "symbolColor": symbol_color,
            "character": m.any_alphanumeric_key,
        }
    }

