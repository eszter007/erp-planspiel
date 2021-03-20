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

class inventory:
        
    def fetch():
        materials = []
        types = []
        balances = []
        dates = []
    
        p = service.theservice.entity_sets.Inventory.get_entities()
        for p_ in p.execute():
            description = p_.MATERIAL_DESCRIPTION 
            date = p_.SIM_DATE
            date = service.formatDate(date)
            balance = p_.INVENTORY_OPENING_BALANCE
            materialType = p_.MATERIAL_TYPE
            
            if not (materialType == "Raw materials"):
                if "500" in description:
                    materials.append(description)
                    balances.append(float(balance))
                    dates.append(date)
        return [materials, types, balances, dates]