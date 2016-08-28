from tempylate import tag, html


def render_template_index():
    body = tag(_id="app", content=tag("fullpage-app"))
    css = [
        'https://cdnjs.cloudflare.com/ajax/libs/' +
        'fullPage.js/2.8.4/jquery.fullPage.min.css',
        'https://cdnjs.cloudflare.com/ajax/libs/' +
        'materialize/0.97.7/css/materialize.min.css',
        '../static/css/style.css'
    ]
    js = [
        'https://cdnjs.cloudflare.com/ajax/libs/' +
        'vue/1.0.26/vue.min.js',
        'https://cdnjs.cloudflare.com/ajax/libs/' +
        'jquery/3.1.0/jquery.min.js',
        'https://cdnjs.cloudflare.com/ajax/libs/' +
        'fullPage.js/2.8.4/jquery.fullPage.min.js',
        'https://cdnjs.cloudflare.com/ajax/libs/' +
        'materialize/0.97.7/js/materialize.min.js',
        'https://cdnjs.cloudflare.com/ajax/libs/' +
        'progressbar.js/1.0.1/progressbar.min.js',
        'https://cdnjs.cloudflare.com/ajax/libs/' +
        'leaflet/1.0.0-rc.3/leaflet.js'
    ]
    js_scripts = [
        '../static/js/data.js',
        '../static/js/homepage.js'
    ]
    return html(title="Homepage",
                js=js,
                css=css,
                js_scripts=js_scripts,
                body=body)
