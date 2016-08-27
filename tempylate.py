def html(body="", title="", css=[], js=[], js_scripts=[]):
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
    </html>
    """ % (str(title),
           " ".join(css_libraries),
           " ".join(js_libraries),
           str(body),
           " ".join(js_files))


def tag(html_tag="div", js_framework="vue", **kwargs):
    tag = str(html_tag)
    attrs = []
    content = []
    for k, v in kwargs.iteritems():
        if k == "content":
            if isinstance(v, list):
                for _ in v:
                    content.append(_)
            else:
                content.append(v)
        if k.startswith("_"):
            k = k[1:]
            if js_framework == "vue":
                if k.startswith("v"):
                    k = "v-" + k[1:]
                elif k.startswith("_"):
                    k = ":" + k[1:]
            attrs.append(str(k) + "=\"" + str(v) + "\"")
    return "<%s %s>%s</%s>" % (tag, " ".join(attrs), " ".join(content), tag)
