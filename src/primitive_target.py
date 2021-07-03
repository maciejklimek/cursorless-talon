from dataclasses import dataclass
from talon import Context, Module
from .mark import MARK_THIS
from .selection_type import SELECTION_TYPE_KEY, RANKED_SELECTION_TYPES

ctx = Context()
mod = Module()

ctx.matches = r"""
app: vscode
"""

BASE_TARGET = {"type": "primitive"}
STRICT_HERE = {
    "type": "primitive",
    "mark": {"type": "cursor"},
    "selectionType": "token",
    "position": "contents",
    "transformation": {"type": "identity"},
    "insideOutsideType": "inside"
}


parameters = [
    "<user.cursorless_position>",             # before, above
    "<user.cursorless_selection_type>",       # token, line, file
    "<user.cursorless_containing_scope>",     # funk, state, class
    "<user.cursorless_subcomponent>"          # first past second word

    # "<user.cursorless_pair_surround_type>",   # inner, outer
    # "<user.cursorless_surrounding_pair>",     # inner curly, outer round
    # "<user.cursorless_matching>",             # matching
]

optional_parameters = " ".join(f"[{p}]" for p in parameters)

marks = "|".join([
    *parameters,
    "<user.decorated_symbol>", # blue air
    "<user.cursorless_mark>"  # this, that
])


# "[{user.cursorless_position}] "
# "[{user.cursorless_pair_surround_type}] "
# "[{user.cursorless_selection_type} [of | in | containing]] "
# "[<user.cursorless_range_transformation>] "
# "[<user.cursorless_subcomponent> [at]]"
# "(<user.decorated_symbol> | {user.cursorless_mark} | {user.unmarked_core} | <user.cursorless_surrounding_pair> | <user.cursorless_containing_scope> | <user.cursorless_subcomponent>)"
# "[<user.cursorless_subcomponent> | {user.cursorless_matching}]"
    
@mod.capture(rule=(f"{optional_parameters} ({marks})"))
def cursorless_primitive_target(m) -> str:
    """Supported extents for cursorless navigation"""
    object = BASE_TARGET.copy()
    for capture in m:
        for key, value in capture.items():
            if (
                key in object
                and key == SELECTION_TYPE_KEY
                and RANKED_SELECTION_TYPES[value] < RANKED_SELECTION_TYPES[object[key]]
            ):
                continue
            object[key] = value
    return object
