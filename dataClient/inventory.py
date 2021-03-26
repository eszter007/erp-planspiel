#odata
import requests
import pyodata
import pandas as pd

#classes
from dataClient.service import service
from dataClient.helper import helper as h

class inventoryData:
    
    def fetch(size):
        materials = []
        types = []
        balances = []
        dates = []
    
        p = service.theservice.entity_sets.Inventory.get_entities()
        for p_ in p.execute(): 
            date = p_.SIM_DATE
            if h.correctDateFormat(date):
                date = h.formatDate(date)
                description = p_.MATERIAL_DESCRIPTION 
                balance = p_.INVENTORY_OPENING_BALANCE
                materialType = p_.MATERIAL_TYPE
                
                if size in description:
                    materials.append(description)
                    balances.append(float(balance))
                    dates.append(date)
            else: continue
        return [materials, types, balances, dates]

# Visualization
import plotly.express as px

class inventoryVisualization:
    def getFigure(size):
        df = pd.DataFrame({
            "Amount": inventoryData.fetch(size)[2],
            "Date": inventoryData.fetch(size)[3],
            "Material": inventoryData.fetch(size)[0]
        })
        df = df.sort_values("Material")

        fig = px.bar(df, x="Date", y="Amount", color="Material")
        fig.write_html("./Demo_Files/Inventory/" + size + "inventory.html")
        return fig