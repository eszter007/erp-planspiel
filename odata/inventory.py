#odata
import requests
import pyodata
import pandas as pd

#classes
from service import service

class inventoryData:
    
    def fetch(size):
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
            
            if size in description:
                materials.append(description)
                balances.append(float(balance))
                dates.append(date)
        return [materials, types, balances, dates]

#
import plotly.express as px

class inventoryVisualization:
    def getFigure(size):
        df = pd.DataFrame({
            "Amount": inventoryData.fetch(size)[2],
            "Date": inventoryData.fetch(size)[3],
            "Material": inventoryData.fetch(size)[0]
        })

        fig = px.bar(df, x="Date", y="Amount", color="Material")
        return fig