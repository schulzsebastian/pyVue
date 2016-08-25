from pyvue import div, html_basic


def index():
    return div([div(["Homepage"], _class="section"),
                div(["Skills"], _class="section"),
                div(["Interests"], _class="section"),
                div(["Contact"], _class="section")],
               id="fullpage")


def render_template_index():
    css = [
        'https://cdnjs.cloudflare.com/ajax/libs/' +
        'fullPage.js/2.8.4/jquery.fullPage.min.css',
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
        '../static/js/components.js',
        '../static/js/data.js',
        '../static/js/map.js',
        '../static/js/script.js'
    ]
    return html_basic(title="Homepage",
                      css=css,
                      js=js,
                      js_scripts=js_scripts,
                      body=index())
