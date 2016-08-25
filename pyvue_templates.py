from pyvue import div, html_basic


def index():
    return div([div(["Homepage"], _class="section"),
                div(["Skills"], _class="section"),
                div(["Interests"], _class="section"),
                div(["Contact"], _class="section")],
               id="fullpage")


def render_template_index():
    model = {
        'el': "#fullpage",
        'data': {
            'testString': 'Hello!',
            'testInt': 10,
            'testArray': [1, 2, 3, 4]
        }
    }
    css_libs = [
        'https://cdnjs.cloudflare.com/ajax/libs/' +
        'fullPage.js/2.8.4/jquery.fullPage.min.css'
    ]
    js_libs = [
        'https://cdnjs.cloudflare.com/ajax/libs/' +
        'jquery/3.1.0/jquery.min.js',
        'https://cdnjs.cloudflare.com/ajax/libs/' +
        'fullPage.js/2.8.4/jquery.fullPage.min.js'
    ]
    return html_basic(title="Homepage",
                      css=css_libs,
                      js=js_libs,
                      model=model,
                      body=index())
