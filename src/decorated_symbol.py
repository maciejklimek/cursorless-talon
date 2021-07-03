from talon import Context, Module

mod = Module()
ctx = Context()

ctx.matches = r"""
app: vscode
"""

@mod.capture(rule="[{user.symbol_color}] <user.any_alphanumeric_key>")
def decorated_symbol(m) -> str:
    """A decorated symbol"""
    try:
        symbol_color = m.symbol_color
    except AttributeError:
        symbol_color = "default"

    return {
        "mark": {
            "type": "decoratedSymbol",
            "symbolColor": symbol_color,
            "character": m.any_alphanumeric_key,
        }
    }

