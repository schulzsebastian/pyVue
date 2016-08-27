title = 'Homepage'
css_libraries = [
    '../static/css/style.css'
]
js_libraries = [
    '../static/js/jquery.js'
]
body = '<div>Hello!</div>'
js_files = [
    '../static/js/data.js'
]
print html(title, css_libraries, js_libraries, body, js_files)

<!DOCTYPE HTML>
<html>
  <head>
  <title>Homepage</title>
  <link rel="stylesheet" href='../static/css/style.css'>
  <script type="text/javascript" src='../static/js/jquery.js'></script>
  </head>
  <body>
    <div>Hello!</div>
  </body>
  <script type="text/javascript" src='../static/js/data.js'></script>
</html>

*****************************

html_tag = 'div'
_id = 'header'
_style = 'color:red'
_class = 'example'

print tag(html_tag, _id, _style, _class)

<div id="header" style="color:red" class="example"></div>