from flask import Flask
import requests
app = Flask(__name__)

sbdb_api_url = "https://ssd-api.jpl.nasa.gov/sbdb_query.api"


# default return Main-belt Asteroid list
# available SBDB Orbit Classes: https://ssd-api.jpl.nasa.gov/doc/sbdb_filter.html
@app.route("/api/query/<string:code>")
@app.route("/api/query")
def query(code="COM"):
    result = requests.get(sbdb_api_url, data={"sb-class": code,
                                               "fields": "e,a,i,om,w,ma"})
    
    return result.json()
    
@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == 'main':
    app.run()