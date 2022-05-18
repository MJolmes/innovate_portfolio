from flask import Flask, render_template, redirect, Blueprint
from views import my_view


app = Flask(__name__)
app.register_blueprint(my_view) # sets the blueprint

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", e=e)




if __name__ == "__main__":
    app.run(debug=True, port=8000) # debugging is activated and the project is set to hosted on port 9000