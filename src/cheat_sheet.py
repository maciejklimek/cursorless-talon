from talon import Module, ui, registry, skia
from talon.canvas import Canvas

mod = Module()
canvas = None
line_height = 34
text_size = 16
padding = 4


def on_draw(canvas):
    paint = canvas.paint

    # ['FILL', 'STROKE', 'STROKE_AND_FILL',
    # paint.color = "ffffffaa"
    draw_background(canvas)

    y = canvas.y + line_height / 2
    x = canvas.x + line_height

    x, y, w = draw_header(canvas, x, y, 0, "Cursorless cheat sheet")
    y = get_y(canvas)
    w = 0

    x, y, w = draw_header(canvas, x, y, w, "Actions")
    c_actions = registry.lists["user.simple_cursorless_action"][0].keys()
    x, y, w = draw_items(canvas, x, y, w, c_actions)

    x, y, w = column(canvas, x, y, w)

    x, y, w = draw_header(canvas, x, y, w, "Colors")
    c_colors = registry.lists["user.symbol_color"][0]
    x, y, w = draw_items(canvas, x, y, w, c_colors)


def draw_background(canvas):
    canvas.paint.style = canvas.paint.Style.FILL
    canvas.paint.color = "ffffff"
    radius = 10
    rrect = skia.RoundRect.from_rect(canvas.rect, x=radius, y=radius)
    canvas.draw_rrect(rrect)


def get_y(canvas):
    return canvas.y + 1.5 * line_height


def column(canvas, x, y, w):
    return (x + w + 2 * line_height, get_y(canvas), 0)


def draw_header(canvas, x, y, w, text):
    canvas.paint.color = "000000"
    canvas.paint.textsize = text_size
    canvas.paint.font.embolden = True
    rect = canvas.paint.measure_text(text)[1]
    draw_text(canvas, text, x, y)
    return x, y + line_height, max(w, rect.width)


def draw_items(canvas, x, y, w, items):
    canvas.paint.textsize = text_size
    canvas.paint.font.embolden = False
    if isinstance(items, dict):
        return draw_dict(canvas, x, y, w, items)
    return draw_list(canvas, x, y, w, items)


def draw_dict(canvas, x, y, w, items):
    y_org = y
    for text in items.keys():
        x, y, w = draw_key(canvas, x, y, w, text)
    y = y_org
    x_value = x + w + line_height
    for text in items.values():
        x_value, y, w = draw_value(canvas, x_value, y, w, text)
    return x, y, w


def draw_list(canvas, x, y, w, items):
    for text in items:
        x, y, w = draw_key(canvas, x, y, w, text)
    return x, y, w


def draw_key(canvas, x, y, w, text):
    rect = canvas.paint.measure_text(text)[1]

    canvas.paint.color = "e0e0e0"
    radius = 4
    rrect = ui.Rect(x, y, rect.width + 2 * padding, text_size + 2 * padding)
    rrect = skia.RoundRect.from_rect(rrect, x=radius, y=radius)
    canvas.draw_rrect(rrect)

    canvas.paint.color = "282828"
    draw_text(canvas, text, x + padding, y)
    return x, y + line_height, max(w, rect.width)


def draw_text(canvas, text, x, y):
    canvas.draw_text(text, x, y + text_size + padding / 2)


def draw_value(canvas, x, y, w, text):
    canvas.paint.color = "666666"
    rect = canvas.paint.measure_text(text)[1]
    draw_text(canvas, text, x, y)
    return x, y + line_height, max(w, rect.width)


@mod.action_class
class Actions:
    def cheat_sheet_toggle():
        """Toggle cheat sheet"""
        global canvas
        if canvas:
            canvas.close()
            canvas = None
        else:
            screen = ui.main_screen()
            # canvas = Canvas.from_screen(screen)
            canvas = Canvas(
                screen.width * 0.2,
                screen.height * 0.2,
                screen.width * 0.6,
                screen.height * 0.6,
            )
            canvas.register("draw", on_draw)
            canvas.freeze()
        # canvas = Canvas(0, 0, 200, 200, draggable=True, panel=True)
        # canvas = Canvas(0, 0, 200, 200, draggable=True, panel=True, software=False)
        # canvas = Canvas(
        #     screen.width * 0.2,
        #     screen.height * 0.2,
        #     screen.width * 0.8,
        #     screen.height * 0.8,
        #     draggable=True
        # )
        # canvas.show()
