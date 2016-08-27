from pyvue import tag, html


def render_template_index():
    body = tag(_id="app", content=tag("elo", __x="test"))
    js = [
        'https://cdnjs.cloudflare.com/ajax/libs/' +
        'vue/1.0.26/vue.min.js',
    ]
    js_scripts = [
        '../static/js/script.js'
    ]
    return html(title="Homepage",
                js=js,
                js_scripts=js_scripts,
                body=body)
