import panel as pn
pn.extension(design="material")

# Create Buttons
decimal = pn.widgets.Button(icon="point-filled")
zero  = pn.widgets.Button(icon="number-0")
one   = pn.widgets.Button(icon="number-1")
two   = pn.widgets.Button(icon="number-2")
three = pn.widgets.Button(icon="number-3")
four  = pn.widgets.Button(icon="number-4")
five  = pn.widgets.Button(icon="number-5")
six   = pn.widgets.Button(icon="number-6")
seven = pn.widgets.Button(icon="number-7")
eight = pn.widgets.Button(icon="number-8")
nine  = pn.widgets.Button(icon="number-9")
left_paren  = pn.widgets.Button(name="(", width=48)
right_paren = pn.widgets.Button(name=")", width=48)
equals      = pn.widgets.Button(button_type="primary", icon="equal")
divide      = pn.widgets.Button(button_type="success", icon="divide")
multiply    = pn.widgets.Button(button_type="success", icon="x")
subtract    = pn.widgets.Button(button_type="success", icon="minus")
add         = pn.widgets.Button(button_type="success", icon="plus")
back    = pn.widgets.Button(button_type="danger", icon="backspace")
clear   = pn.widgets.Button(button_type="danger", icon="trash")

display = pn.pane.Str(
    "0",
    styles={
        'font-family': 'monospace',
        'font-size': '18px',
        'width': "252px",
        'display': 'flex',
        'justify-content': 'flex-end',
        'white-space': 'nowrap', 
        'overflow': 'hidden',
        'border': 'solid',
        'border-radius': '6px',
        'padding': '6px',
    }
)

# Bind click events
def update_display(value):
    if display.object == "0" or display.object == "ERROR":
        display.object = value
    else:
        display.object += value

def backspace(event):
    if not event:
        return
    display.object = display.object[:-1]
    if display.object == "":
        display.object = "0"

def clear_display(event):
    if not event:
        return
    display.object = "0"

def evaluate(event):
    if not event:
        return
    try:
        display.object = str(eval(display.object))
    except:
        display.object = "ERROR"
    
decimal.on_click(lambda event : update_display("."))
zero.on_click(lambda event : update_display("0"))
one.on_click(lambda event : update_display("1"))
two.on_click(lambda event : update_display("2"))
three.on_click(lambda event : update_display("3"))
four.on_click(lambda event : update_display("4"))
five.on_click(lambda event : update_display("5"))
six.on_click(lambda event : update_display("6"))
seven.on_click(lambda event : update_display("7"))
eight.on_click(lambda event : update_display("8"))
nine.on_click(lambda event : update_display("9"))
left_paren.on_click(lambda event : update_display("("))
right_paren.on_click(lambda event : update_display(")"))
divide.on_click(lambda event : update_display(" / "))
multiply.on_click(lambda event : update_display(" * "))
subtract.on_click(lambda event : update_display(" - "))
add.on_click(lambda event : update_display(" + "))

back.on_click(backspace)
clear.on_click(clear_display)
equals.on_click(evaluate)

#  Create layout
calc_app = pn.Column(
    pn.Column(display),
    pn.Column(pn.Row(left_paren, right_paren, back, clear)),
    pn.Column(pn.Row(seven, eight, nine, divide)),
    pn.Column(pn.Row(four, five, six, multiply)),
    pn.Column(pn.Row(one, two, three, subtract)),
    pn.Column(pn.Row(zero, decimal, equals, add)),
)
calc_app.servable()