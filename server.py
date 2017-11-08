import os
from flask import Flask, render_template, request, flash, redirect, session, \
    jsonify
from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar

@app.route('/')
def index():
    """Main page."""

    return render_template("/chrome/index.html")

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = False

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(debug=True, host="0.0.0.0")