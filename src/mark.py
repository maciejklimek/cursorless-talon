from talon import Context, Module

mod = Module()
ctx = Context()

ctx.matches = r"""
app: vscode
"""


cursor_mark = {"mark": {"type": "cursor"}}
that_mark = {"mark": {"type": "that"}}


@mod.capture(rule="last cursor")
def cursorless_last_cursor_mark(m) -> str:
    return {"mark": {"type": "lastCursorPosition"}}


@mod.capture(rule=(
    "this | "
    "this <user.cursorless_selection_type> | "
    "this <user.cursorless_containing_scope_type>"
))
def cursorless_cursor_mark(m) -> str:
    if len(m) > 1:
        return {**cursor_mark, **m[1]}
    return cursor_mark


@mod.capture(rule=(
    "that | "
    "that <user.cursorless_containing_scope_type>"
))
def cursorless_that_mark(m) -> str:
    if len(m) > 1:
        return {**that_mark, **m[1]}
    return that_mark


@mod.capture(rule=(
    "<user.cursorless_last_cursor_mark> | "
    "<user.cursorless_cursor_mark> | "
    "<user.cursorless_that_mark>"
))
def cursorless_mark(m) -> str:
    return m[0]
