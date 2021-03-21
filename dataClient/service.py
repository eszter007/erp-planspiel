# odata 
import requests
import pyodata
from pyodata.v2.model import PolicyFatal, PolicyWarning, PolicyIgnore, ParserError, Config

class service:
    SERVICE_URL = 'https://r73z.ucc.ovgu.de:/odata/700/'

    session = requests.Session()
    session.auth = ('C_3', 'etc-oxide-GARBAGE')
    
    theservice = pyodata.Client(SERVICE_URL, session)