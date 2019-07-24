"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/")
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>Hi! This is the home page <br>
    <a href="/hello">Get a compliment</a><br>
    <a href="/diss">Get a diss</a>
    </html>
    """


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br>
          <label> Choose your compliment: </label>
            <select name="compliment">
                <option value="beautiful">beautiful</option>
                <option value="smart">smart</option>
                <option value="funny">funny</option>
                <option value="cheerful">cheerful</option>
            </select><br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

@app.route("/diss")
def say_insult():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/insult">
          What's your name? <input type="text" name="person"><br>
          <label> Choose your diss: </label>
            <select name="diss">
                <option value="ugly">ugly</option>
                <option value="stinky">stinky</option>
                <option value="boring">boring</option>
                <option value="stupid">stupid</option>
            </select><br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)
    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route("/insult")
def insult_person():
    """Get user by name."""

    player = request.args.get("person")

    insult = request.args.get("diss")

    return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
        <a href="/test">Click here for test</a>
      </body>
    </html>
    """.format(player, insult)
    

if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
