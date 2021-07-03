from talon import Context, Module

mod = Module()
ctx = Context()

ctx.matches = r"""
app: vscode
"""

MARK_THIS = {"mark": {"type": "cursor"}}

marks = {
    "this": MARK_THIS,
    "that": {"mark": {"type": "that"}}

    # "last cursor": {"mark": {"type": "lastCursorPosition"}} # Not implemented
}

mod.list("cursorless_mark", desc="Types of marks")
ctx.lists["self.cursorless_mark"] =  marks.keys()

@mod.capture(rule="{user.cursorless_mark}")
def cursorless_mark(m) -> str:
    return marks[m.cursorless_mark]
