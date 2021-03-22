from decouple import config
# odata 
import requests
import pyodata
from pyodata.v2.model import PolicyFatal, PolicyWarning, PolicyIgnore, ParserError, Config

class service:
    SERVICE_URL = config("SERVICEURL")

    session = requests.Session()
    session.auth = (config("USERNAME"), config("PASSWORD"))
    theservice = pyodata.Client(SERVICE_URL, session)