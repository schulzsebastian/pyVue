from pyvue import div, html_basic


def index():
    return div(
        [div(vtext="testString"),
         div(vtext="testInt"),
         div([div(vtext="i")], vfor="i in testArray")], id="app")


def render_template_index():
    model = {
        'el': "#app",
        'data': {
            'testString': 'Hello!',
            'testInt': 10,
            'testArray': [1, 2, 3, 4]
        }
    }
    return html_basic(title="Example App", model=model, body=index())
