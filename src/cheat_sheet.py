from talon import Module, ui, registry, skia, actions
from talon.canvas import Canvas
import re

mod = Module()
mod.mode("cursorless_cheat_sheet", "Mode for showing cursorless cheat sheet gui")
cheat_sheet = None

line_height = 34
text_size = 16
padding = 4


class CheatSheet:
    def __init__(self):
        # canvas = Canvas.from_screen(screen)
        screen = ui.main_screen()
        self.canvas = Canvas(
            screen.width * 0.05,
            screen.height * 0.05,
            screen.width * 0.9,
            screen.height * 0.9,
        )
        self.canvas.register("draw", self.draw)
        self.canvas.freeze()

    def close(self):
        self.canvas.close()
        self.canvas = None

    def draw(self, canvas):
        self.x = canvas.x + line_height

        self.draw_background(canvas)
        self.draw_title(canvas)
        self.draw_legend(canvas)

        self.y = get_y(canvas)
        self.w = 0

        self.draw_header(canvas, "Actions")
        self.draw_items(canvas, get_list("simple_cursorless_action"))

        self.next_row()
        self.draw_header(canvas, "Colors")
        self.draw_items(canvas, get_list("symbol_color"))

        self.next_column(canvas)

        self.draw_header(canvas, "Sub types")
        self.draw_items(canvas, get_list("cursorless_sub_component_type"))

        self.next_row()
        self.draw_header(canvas, "Positions")
        self.draw_items(canvas, get_list("cursorless_position").keys())

        self.next_column(canvas)

        self.draw_header(canvas, "Swap")
        self.draw_items(canvas, {
            "swap T with T": "Swaps both Ts",
            "swap with T": "Swap S with T"
        })

        self.next_row()
        self.draw_header(canvas, "Bring")
        self.draw_items(canvas, {
            "bring T to T": "Replace T_2 with T_1",
            "bring T": "Replace S with T"
        })

        self.next_row()
        self.draw_header(canvas, "Compound targets")
        self.draw_items(canvas, {
            "T and T": "Ts",
            "T past T": "Ts and between",
            "past T": "S, T and between"
        })

        self.next_column(canvas)

        self.draw_header(canvas, "Transformations")
        self.draw_items(canvas, get_list("containing_scope_type").keys())

        self.next_column(canvas)

        self.draw_header(canvas, "Marks")
        self.draw_items(canvas, get_list("cursorless_mark").keys())

    def draw_background(self, canvas):
        # paint.color = "ffffffaa"
        radius = 10
        rrect = skia.RoundRect.from_rect(canvas.rect, x=radius, y=radius)
        canvas.paint.style = canvas.paint.Style.FILL
        canvas.paint.color = "ffffff"
        canvas.draw_rrect(rrect)

        canvas.paint.style = canvas.paint.Style.STROKE
        canvas.paint.color = "000000"
        canvas.draw_rrect(rrect)

    def draw_title(self, canvas):        
        self.y = canvas.y + line_height / 2
        self.w = 0
        self.draw_header(canvas, "Cursorless cheat sheet")
    
    def draw_legend(self, canvas):
        self.y = canvas.y + canvas.height - line_height
        self.draw_value(canvas, "S = selection    T = target")

    def next_column(self, canvas):
        self.x = self.x + self.w + 2 * line_height
        self.y = get_y(canvas)
        self.w = 0

    def next_row(self):
        self.y += line_height

    def draw_header(self, canvas, text):
        canvas.paint.color = "000000"
        canvas.paint.textsize = text_size
        canvas.paint.style = canvas.paint.Style.FILL
        canvas.paint.font.embolden = True
        rect = canvas.paint.measure_text(text)[1]
        draw_text(canvas, text, self.x, self.y)
        self.y += line_height
        self.w = max(self.w, rect.width)

    def draw_items(self, canvas, items):
        canvas.paint.textsize = text_size
        canvas.paint.style = canvas.paint.Style.FILL
        canvas.paint.font.embolden = False
        if isinstance(items, dict):
            self.draw_dict(canvas, items)
        else:
            self.draw_list(canvas, items)

    def draw_dict(self, canvas, items):
        x_org = self.x
        y_org = self.y
        w_org = self.w

        self.w = 0
        for text in items.keys():
            self.draw_key(canvas, text)
        width_key = self.w

        self.x = x_org + width_key + line_height
        self.y = y_org
        self.w = 0
        for text in items.values():
            self.draw_value(canvas, text)
        width_value = self.w

        self.x = x_org
        self.w = max(w_org, width_key + line_height + width_value)

    def draw_list(self, canvas, items):
        for text in items:
            self.draw_key(canvas, text)

    def draw_key(self, canvas, text):
        rect = canvas.paint.measure_text(text)[1]

        canvas.paint.color = "e0e0e0"
        radius = 4
        rrect = ui.Rect(self.x, self.y, rect.width + 2 * padding, text_size + 2 * padding)
        rrect = skia.RoundRect.from_rect(rrect, x=radius, y=radius)
        canvas.draw_rrect(rrect)

        canvas.paint.color = "282828"
        draw_text(canvas, text, self.x + padding, self.y)

        self.y += line_height
        self.w = max(self.w, rect.width)

    def draw_value(self, canvas, text):
        canvas.paint.color = "666666"
        rect = canvas.paint.measure_text(text)[1]
        draw_text(canvas, text, self.x, self.y)
        self.y += line_height
        self.w = max(self.w, rect.width)


@mod.action_class
class Actions:
    def cursorless_cheat_sheet_toggle():
        """Toggle cursorless cheat sheet"""
        global cheat_sheet
        if cheat_sheet:
            actions.mode.disable("user.cursorless_cheat_sheet")
            cheat_sheet.close()
            cheat_sheet = None
        else:
            cheat_sheet = CheatSheet()
            actions.mode.enable("user.cursorless_cheat_sheet")

def get_list(name):
    items = registry.lists[f"user.{name}"][0].copy()
    if isinstance(items, dict):
        make_dict_readable(items)
    return items

def get_y(canvas):
    return canvas.y + 1.5 * line_height

def draw_text(canvas, text, x, y):
    canvas.draw_text(text, x, y + text_size + padding / 2)

def make_dict_readable(dict):
    for k in dict:
        dict[k] = make_readable(dict[k])

def make_readable(text):
    return re.sub(r"(?<=[a-z])(?=[A-Z])", " ", text).lower().capitalize()
