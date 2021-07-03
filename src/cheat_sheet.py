from talon import Module, ui, registry, skia, actions
from talon.canvas import Canvas
import re
import webbrowser

mod = Module()
mod.mode("cursorless_cheat_sheet", "Mode for showing cursorless cheat sheet gui")
cheat_sheet = None
last_mouse_pos = None

line_height = 34
text_size = 16
close_size = 24
padding = 4
instructions_url = "https://github.com/pokey/cursorless-talon/tree/master/docs"


class CheatSheet:
    def __init__(self):
        screen = ui.main_screen()
        self.canvas = Canvas(
            screen.width * 0.05,
            screen.height * 0.05,
            screen.width * 0.9,
            screen.height * 0.9
        )
        self.canvas.blocks_mouse = True
        self.canvas.register("draw", self.draw)
        self.canvas.register("mouse", self.mouse)
        self.canvas.freeze()

    def close(self):
        self.canvas.unregister("draw", self.draw)
        self.canvas.unregister("mouse", self.mouse)
        self.canvas.close()

    def mouse(self, e):
        global in_drag, last_mouse_pos
        if e.event == "mousedown" and e.button == 0:
            last_mouse_pos = e.gpos
        elif e.event == "mousemove" and last_mouse_pos:
            diff_x = e.gpos.x - last_mouse_pos.x
            diff_y = e.gpos.y - last_mouse_pos.y
            last_mouse_pos = e.gpos
            self.canvas.move(
                self.canvas.rect.x + diff_x,
                self.canvas.rect.y + diff_y
            )
        elif e.event == "mouseup" and e.button == 0:
            last_mouse_pos = None
            if is_in_rect(self.canvas, e.gpos, get_close_rect(self.canvas)):
                actions.user.cursorless_cheat_sheet_toggle()
            elif is_in_rect(self.canvas, e.gpos, self.url_rect):
                actions.user.cursorless_cheat_sheet_toggle()
                actions.user.cursorless_open_instructions()

    def draw(self, canvas):
        self.x = canvas.x + line_height

        self.draw_background(canvas)
        self.draw_title(canvas)
        self.draw_legend(canvas)
        self.draw_close(canvas)
        self.draw_url(canvas)

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
            "bring T to T": "Replace T2 with T1",
            "bring T": "Replace S with T"
        })

        self.next_row()
        self.draw_header(canvas, "Compound targets")
        self.draw_items(canvas, {
            "T and T": "T1 and T2",
            "T past T": "T1, T2 and between",
            "past T": "S, T and between"
        })

        self.next_column(canvas)

        self.draw_header(canvas, "Transformations")
        self.draw_items(canvas, get_list("containing_scope_type").keys())

        self.next_column(canvas)

        self.draw_header(canvas, "Marks")
        # self.draw_items(canvas, get_list("cursorless_mark").keys()e)

    def draw_background(self, canvas):
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

    def draw_close(self, canvas):
        canvas.paint.textsize = close_size
        rect = get_close_rect(canvas)
        padding = close_size * 0.375
        canvas.draw_text("X", rect.x + padding, rect.y + rect.height - padding)

    def draw_url(self, canvas):
        rect = get_url_rect(canvas)
        self.url_rect = rect
        canvas.paint.color = "6495ED"
        canvas.paint.textsize = text_size
        canvas.paint.style = canvas.paint.Style.FILL
        draw_text(canvas, instructions_url, rect.x + line_height / 2, rect.y + padding)

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

    def cursorless_open_instructions():
        """Open web page with cursorless instructions"""
        webbrowser.open(instructions_url)

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

def get_close_rect(canvas):
    wh = 1.5 * close_size
    cr = canvas.rect
    return ui.Rect(
        cr.x + cr.width - wh,
        cr.y,
        wh,
        wh
    )

def get_url_rect(canvas):
    canvas.paint.textsize = text_size
    rect = canvas.paint.measure_text(instructions_url)[1]
    wh = rect.width + line_height
    cr = canvas.rect
    return ui.Rect(
        cr.x + cr.width - wh,
        cr.y  + cr.height - line_height,
        wh,
        line_height
    )

def in_range(value, min, max):
    return value >= min and value <= max

def is_in_rect(canvas, mouse_pos, rect):
    return (in_range(mouse_pos.x, rect.x, rect.x + rect.width)
        and in_range(mouse_pos.y, rect.y, rect.y + rect.height))