from flask import Flask, render_template, request
from model import SpellCheckerModule

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        spell_checker = SpellCheckerModule()
        corrected_text = spell_checker.correct_spelling(text)
        corrected_grammar, mistakes_count = spell_checker.correct_grammar(text)
        return render_template("index.html", corrected_text=corrected_text, corrected_grammar=corrected_grammar)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
