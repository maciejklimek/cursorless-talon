from talon import Context, Module

mod = Module()
ctx = Context()

ctx.matches = r"""
app: vscode
"""

pair_symbols = {
    "angle": "angleBrackets",
    "diamond": "angleBrackets",
    "curly": "curlyBrackets",
    "round": "parentheses",
    "square": "squareBrackets",
    "quad": "doubleQuotes",
    "twin": "singleQuotes",
}

mod.list("pair_symbol", desc="A pair symbol")
ctx.lists["self.pair_symbol"] = pair_symbols


pair_surround_types = {
    "outer": {"insideOutsideType": "outside"},
    "outside": {"insideOutsideType": "outside"},
    "inner": {"insideOutsideType": "inside"},
    "inside": {"insideOutsideType": "inside"},
}

mod.list("cursorless_pair_surround_type", desc="Supported pair surround types")
ctx.lists["self.cursorless_pair_surround_type"] = pair_surround_types.keys()

@mod.capture(rule=("{user.cursorless_pair_surround_type}"))
def cursorless_pair_surround_type(m) -> str:
    return pair_surround_types[m.cursorless_pair_surround_type]


@mod.capture(rule=("<user.cursorless_pair_surround_type> {user.pair_symbol}"))
def cursorless_surrounding_pair(m) -> str:
    """Supported extents for cursorless navigation"""
    return {
        "transformation": {
            "type": "surroundingPair",
            "delimiter": m.pair_symbol,
        }
        **m.cursorless_pair_surround_type,
    }
