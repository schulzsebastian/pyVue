import json


def html_basic(body="<div id=\"pyvue\">Hello pyVue!</div>",
               model={'el': '#pyvue'},
               title="Hello pyVue!",
               css=[],
               js=[]):
    js_libraries = ["<script type=\"text/javascript\" src=\"%s\"></script>"
                    % str(lib) for lib in js]
    css_libraries = ["<link rel=\"stylesheet\" href=\"%s\">"
                     % str(lib) for lib in css]
    return """
    <!DOCTYPE HTML>
    <html>
        <head>
        <title>%s</title>
        %s
        <script type=\"text/javascript\"
        src=\"https://cdnjs.cloudflare.com/ajax/libs/vue/1.0.26/vue.min.js\">
        </script>
        %s
    </head>
    <body>
        %s
    </body>
    <script>var vm = new Vue(%s)</script></html>
    """ % (str(title),
           " ".join(css_libraries),
           " ".join(js_libraries),
           str(body),
           json.dumps(model))


def div(content=[""], **kwargs):
    attrs = []
    for k, v in kwargs.iteritems():
        if k.startswith("v"):
            k = "v-" + k[1:]
        elif k.startswith("_"):
            k = k[1:]
        attrs.append(str(k) + "=\"" + str(v) + "\"")
    return "<div " + " ".join(attrs) + ">" + " ".join(content) + "</div>"
