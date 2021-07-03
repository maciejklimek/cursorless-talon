from dataclasses import dataclass
from talon import Context, Module
import json

ctx = Context()
mod = Module()

ctx.matches = r"""
app: vscode
"""

CONNECTIVES = {"at", "of", "in", "containing"}

BASE_TARGET = {"type": "primitive"}
STRICT_HERE = {
    "type": "primitive",
    "mark": {"type": "cursor"},
    "selectionType": "token",
    "position": "contents",
    "transformation": {"type": "identity"},
    "insideOutsideType": "inside",
}


@mod.capture(
    rule=(
        "[<user.cursorless_position>] "
        "[<user.cursorless_pair_surround_type>] "
        "[<user.cursorless_selection_type> [of | in | containing]] "
        "[<user.cursorless_range_transformation>] "
        "[<user.cursorless_subcomponent> [at]]"
        "(<user.decorated_symbol> | <user.cursorless_mark> | <user.cursorless_unmarked_core> | <user.cursorless_surrounding_pair> | <user.cursorless_containing_scope> | <user.cursorless_subcomponent>)"
        "[<user.cursorless_subcomponent> | <user.cursorless_matching>]"
    )
)
def cursorless_primitive_target(m) -> str:
    """Supported extents for cursorless navigation"""
    object = BASE_TARGET.copy()
    for capture in m: 
        if isinstance(capture, str) and capture in CONNECTIVES:
            continue
        for key, value in capture.items():
            if (
                key in object
                and key == SELECTION_TYPE_KEY
                and ranked_selection_types[value] < ranked_selection_types[object[key]]
            ):
                continue
            object[key] = value
    return object
