import yaml, json, sys

SWAGGER_HTML_TEMPLATE = """
<!-- HTML for static distribution bundle build -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Swagger UI</title>
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/swagger-ui.css" >
    <link rel="icon" type="image/png" href="./favicon-32x32.png" sizes="32x32" />
    <link rel="icon" type="image/png" href="./favicon-16x16.png" sizes="16x16" />
    <style>
      html
      {
        box-sizing: border-box;
        overflow: -moz-scrollbars-vertical;
        overflow-y: scroll;
      }

      *,
      *:before,
      *:after
      {
        box-sizing: inherit;
      }

      body
      {
        margin:0;
        background: #fafafa;
      }
    </style>
  </head>

  <body>
    <div id="swagger-ui"></div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/swagger-ui-bundle.js"> </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/swagger-ui-standalone-preset.js"> </script>
    <script>
    window.onload = function() {
      var swagger_spec = %s
      // Begin Swagger UI call region
      const ui = SwaggerUIBundle({
        spec: swagger_spec,
        dom_id: '#swagger-ui',
        deepLinking: true,
        presets: [
        SwaggerUIBundle.presets.apis,
        SwaggerUIStandalonePreset
        ],
        plugins: [
        SwaggerUIBundle.plugins.DownloadUrl
        ],
        layout: "StandaloneLayout"
      })
      // End Swagger UI call region

      window.ui = ui
    }
  </script>
  </body>
</html>
"""

spec = yaml.load(sys.stdin, Loader=yaml.FullLoader)
sys.stdout.write(SWAGGER_HTML_TEMPLATE % json.dumps(spec))