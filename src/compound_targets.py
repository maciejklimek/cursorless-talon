import json
from .primitive_target import BASE_TARGET
from talon import Module

mod = Module()


@mod.capture(
    rule=(
        "<user.cursorless_primitive_target> | "
        "past <user.cursorless_primitive_target> | "
        "<user.cursorless_primitive_target> past <user.cursorless_primitive_target>"
    )
)
def cursorless_range(m) -> str:
    if "past" in m:
        end = json.loads(m[-1])
        if m[0] == "past":
            start = BASE_TARGET.copy()
        else:
            start = json.loads(m.cursorless_primitive_target_list[0])
        return json.dumps(
            {
                "type": "range",
                "start": start,
                "end": end,
            }
        )

    return m[0]


@mod.capture(rule=("<user.cursorless_range> (and <user.cursorless_range>)*"))
def cursorless_target(m) -> str:
    if len(m.cursorless_range_list) == 1:
        return m.cursorless_range
    return json.dumps(
        {
            "type": "list",
            "elements": [json.loads(match) for match in m.cursorless_range_list],
        }
    )
