from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>
    <html>
      <head>
        <style>
          form {{
              background-color: #eee;
              padding: 20px;
              margin: 0 auto;
              width: 540px;
              font: 16px sans-serif;
              border-radius: 10px;
          }}
          textarea {{
              margin: 10px 0;
              width: 540px;
              height: 120px;
          }}
        </style>
      </head>
      <body>
        <form action="/" method="post">
          <label for="Rotate_by">Rotate_by: </label>
          <input type="text" name="rot" value=0>
          <textarea name="text">{0}</textarea>
          <input type="submit" value="Submit"/>
        </form>
      </body>
    </html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rotate_by = int(request.form['rot'])
    text_enter = str(request.form['text'])

    rotated_string = rotate_string(text_enter, rotate_by)
     
    return form.format(rotated_string)


app.run()
