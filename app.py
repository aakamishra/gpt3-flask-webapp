import os

import openai
from flask import Flask, redirect, render_template, request, url_for

# intialize applicagion object
app = Flask(__name__)

# load API key from environment / note that the python-noenv package is necessary for this
openai.api_key = os.getenv("OPENAI_API_KEY")

# establish API protocol
@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        # generate a form request for getting the character faction
        star_wars_faction = request.form["Faction"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_star_wars_prompt(star_wars_faction),
            temperature=0.9,
        )
        # return result object to display for the html index
        return redirect(url_for("index", result=response.choices[0].text))

    # display result from returned js object and launch index html 
    result = request.args.get("result")
    return render_template("index.html", result=result)



def generate_star_wars_prompt(animal):
    return """Suggest three names for a character in Star Wars.
Faction: Rebels 
Names: Captain Andor, Bay Organa, Ben Solo
Faction: Empire
Names: Darth Evil, Ventress, Cato Fett
Faction: {}
Names:""".format(
        animal.capitalize()
    )