# odata 
import requests
import pyodata
from pyodata.v2.model import PolicyFatal, PolicyWarning, PolicyIgnore, ParserError, Config

#datetime
from datetime import datetime

class service:
    SERVICE_URL = 'https://r73z.ucc.ovgu.de:/odata/700/'

    session = requests.Session()
    session.auth = ('C_3', 'etc-oxide-GARBAGE')
    
    theservice = pyodata.Client(SERVICE_URL, session)
    
    def formatDate(date):
        date = datetime.strptime(date, '%m/%d').replace(year=2021)
        return date