#odata
import requests
import pyodata
import pandas as pd

#classes
from service import service

class marketingData:
    
    def fetch(size):
        dates = []
        materials= []
        areas = []
        amounts = []
    
        p = service.theservice.entity_sets.Marketing_Expenses.get_entities()
        for p_ in p.execute():
            description = p_.MATERIAL_DESCRIPTION 
            date = p_.SIM_DATE
            date = service.formatDate(date)
            area = p_.AREA
            amount = p_.AMOUNT
            
            if size in description:
                dates.append(date)
                materials.append(description)
                amounts.append(float(amount))
                areas.append(area)
        return [dates, materials, areas, amounts]

#
import plotly.express as px

class marketingVisualization:
    def getFigure(size):
        data = marketingData.fetch(size)
        df = pd.DataFrame({
            "Amount": data[3],
            "Date": data[0],
            "Material": data[1],
            "Areas" : data[2]
        })

        fig = px.line(df, x="Date", y="Amount", color="Material")
        return fig