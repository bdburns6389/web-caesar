from flask import flask

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>
    <html>
      <head>
        <style>
          form
"""

@app.route("/")
def index():
    return "Hello World"

app.run()