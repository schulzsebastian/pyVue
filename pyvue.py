import json


def html_basic(body="<div id=\"pyvue\">Hello pyVue!</div>",
               title="Hello pyVue!",
               css=[],
               js=[],
               js_scripts=[]):
    css_libraries = ["<link rel=\"stylesheet\" href=\"%s\">"
                     % str(lib) for lib in css]
    js_libraries = ["<script type=\"text/javascript\" src=\"%s\"></script>"
                    % str(lib) for lib in js]
    js_files = ["<script type=\"text/javascript\" src=\"%s\"></script>"
                % str(lib) for lib in js_scripts]
    return """
    <!DOCTYPE HTML>
    <html>
        <head>
        <title>%s</title>
        %s
        %s
    </head>
    <body>
        %s
    </body>
    %s
    """ % (str(title),
           " ".join(css_libraries),
           " ".join(js_libraries),
           str(body),
           " ".join(js_files))


def div(content=[""], **kwargs):
    attrs = []
    for k, v in kwargs.iteritems():
        if k.startswith("v"):
            k = "v-" + k[1:]
        elif k.startswith("_"):
            k = k[1:]
        attrs.append(str(k) + "=\"" + str(v) + "\"")
    return "<div " + " ".join(attrs) + ">" + " ".join(content) + "</div>"
