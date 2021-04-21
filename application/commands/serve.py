"""Module for serving an API."""

from flask import Flask, send_file

import api

def serve(options, apiObject):
    """Serve an API."""

    # Create a Flask application
    app = Flask(__name__)

    @app.route("/")
    def index():
        """Return the index page of the website."""
        return send_file("../www/index.html")

    @app.route("/greeting/<name>")
    def greeting(name):
        """Return a greeting for the user."""
        return "Hello, {}!".format(name)


    ########################################
    # API calls
    ########################################

    @app.route("/API/data")
    def apiData():
        return apiObject.getAllData()

    @app.route("/API/data/timespan/<_from>/<_to>")
    def dataInTimeSpan(_from, _to):
        if _from == "NULL":
            _from = None
        if _to == "NULL":
            _to = None
        return apiObject.getDataInTimespan(_from, _to)

    @app.route("/API/confirmedCountry/timespan/<_from>/<_to>")
    def confirmedperCountryInTimespan(_from, _to):
        if _from == "NULL":
            _from = None
        if _to == "NULL":
            _to = None
        return apiObject.getConfirmedCountryInTimespan(_from, _to)


    app.run(host=options.address, port=options.port, debug=True)

def create_parser(subparsers):
    """Create an argument parser for the "serve" command."""
    parser = subparsers.add_parser("serve")
    parser.set_defaults(command=serve)
    # Add optional parameters to control the server configuration
    parser.add_argument("-p", "--port", default=8080, type=int, help="The port to listen on")
    parser.add_argument("--address", default="0.0.0.0", help="The address to listen on")
