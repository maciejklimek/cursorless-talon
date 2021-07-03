from talon import Context, Module
from .containing_scope import containing_scope_types
from .selection_type import SELECTION_TYPES
from .matching_transformation import matching_transformation

mod = Module()
ctx = Context()

ctx.matches = r"""
app: vscode
"""

unmarked_cores = {
    **containing_scope_types,
    **{
        selection_type.singular: selection_type.json_repr
        for selection_type in SELECTION_TYPES
    },
    matching_transformation.term: matching_transformation.info,
}

mod.list("cursorless_unmarked_core", desc="Core terms whose mark must be inferred")
ctx.lists["self.cursorless_unmarked_core"] = unmarked_cores.keys()

@mod.capture(rule="{user.cursorless_unmarked_core}")
def cursorless_unmarked_core(m) -> str:
    return unmarked_cores[m.cursorless_unmarked_core]
