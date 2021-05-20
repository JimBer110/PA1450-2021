"""Module for serving an API."""

from flask import Flask, send_file, send_from_directory
from flask_cors import CORS

import api

import exporter

def serve(options, apiObject):
    """Serve an API."""

    # Create a Flask application
    app = Flask(__name__)
    cors = CORS(app)

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

    @app.route("/js/<_path>")
    def send_js(_path):
        return send_from_directory('../www/js/', _path)

    @app.route("/styles/<_path>")
    def send_styles(_path):
        return send_from_directory('../www/styles/', _path)

    @app.route("/API/newCasesPerCapita")
    def newCasesPerCapita():
        return apiObject.getListOfCountriesByNewCasesPerCap()

    @app.route("/API/totalCasesPerCapita")
    def totalCasesPerCapita():
        return apiObject.getListOfCountriesByTotalCasesPerCap()

    @app.route("/API/data")
    def apiData():
        return apiObject.getAllData()

    @app.route("/API/countries")
    def apiCountries():
        return apiObject.getCountries()

    @app.route("/API/data/timespan/<_from>/<_to>")
    def dataInTimeSpan(_from, _to):
        if _from == "NULL":
            _from = None
        if _to == "NULL":
            _to = None
        return apiObject.getDataInTimespan(_from, _to)

    @app.route("/API/confirmedCountryChange/timespan/<_from>/<_to>")
    def confirmedperCountryInTimespan(_from, _to):
        if _from == "NULL":
            _from = None
        if _to == "NULL":
            _to = None
        return apiObject.getConfirmedCountryInTimespan(_from, _to)

    @app.route("/API/confirmedCountryByDay/timespan/<_from>/<_to>/<_country>")
    def confirmedperCountryInTimespanByDay(_from, _to, _country):
        if _from == "NULL":
            _from = None
        if _to == "NULL":
            _to = None
        if _country == "NULL":
            _country = "worldwide"
        return apiObject.getTotalCasesForCountryInTimespan(_from, _to, _country)

    @app.route("/API/vaccinationdata")
    def vac_data():
        return apiObject.vaccinationsdata()


    @app.route("/download/<_country>/<_from>/<_to>/<_data>")
    def download(_country,_from,_to,_data):
        if _from == "NULL":
            _from = None
        if _to == "NULL":
            _to = None
        if _country == "NULL":
            _country = "worldwide"
        if _data == "NULL":
            _data = "1111"
        temp = apiObject.getDataInTimespan(_from, _to)
        return send_from_directory(exporter.createFile(temp,_data,_country), 'export.json', as_attachment=True)

    app.run(host=options.address, port=options.port, debug=False)

def create_parser(subparsers):
    """Create an argument parser for the "serve" command."""
    parser = subparsers.add_parser("serve")
    parser.set_defaults(command=serve)
    # Add optional parameters to control the server configuration
    parser.add_argument("-p", "--port", default=8080, type=int, help="The port to listen on")
    parser.add_argument("--address", default="0.0.0.0", help="The address to listen on")
