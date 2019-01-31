import datetime
import xmltodict
from flask import Flask
app = Flask(__name__)

# import xml.etree.ElementTree as ET
# tree = ET.parse('Stats.xml')
# root = tree.getroot()

with open('Stats.xml') as fd:
    xml = xmltodict.parse(fd.read())

@app.route("/")
def hello():
    return repr(str(xml)) + str(datetime.datetime.now())

# this line can be omitted, and you can just run things with FLASK_APP=main.py flask run
# i do not know what the differences are
app.run(debug=True)
