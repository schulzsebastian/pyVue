import json


def html_basic(body="<div id=\"pyvue\">Hello pyVue!</div>",
               model={'el': '#pyvue'},
               title="Hello pyVue!",
               css=[""],
               js=[""]):
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
           " ".join(css),
           " ".join(js),
           str(body),
           json.dumps(model))


def div(content=[""], **kwargs):
    attrs = []
    for k, v in kwargs.iteritems():
        if k.startswith("v"):
            k = "v-" + k[1:]
        attrs.append(str(k) + "=\"" + str(v) + "\"")
    return "<div " + " ".join(attrs) + ">" + " ".join(content) + "</div>"
