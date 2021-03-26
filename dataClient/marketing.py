#odata
import requests
import pyodata
import pandas as pd
import plotly.graph_objects as go

#classes
from dataClient.service import service
from dataClient.helper import helper as h

class marketingData:
    
    def fetch(size):
        dates = []
        materials= []
        areas = []
        amounts = []
    
        p = service.theservice.entity_sets.Marketing_Expenses.get_entities()
        for p_ in p.execute():
            date = p_.SIM_DATE
            if h.correctDateFormat(date):
                date = h.formatDate(date)
                description = p_.MATERIAL_DESCRIPTION
                area = p_.AREA
                amount = p_.AMOUNT
                
                if size in description:
                    dates.append(date)
                    materials.append(description)
                    amounts.append(float(amount))
                    areas.append(area)
            else: continue
        return [dates, materials, areas, amounts]

# Visualization
import plotly.express as px

class marketingVisualization:
        
    def getFigureByTime(size):
        data = marketingData.fetch(size)
        df = pd.DataFrame({
            "Amount": data[3],
            "Date": data[0],
            "Material": data[1],
            "Area" : data[2]
        })
        df = df.sort_values("Material")
        
        fig = px.bar(df, x="Date", y="Amount", color="Material", hover_name="Area", color_discrete_sequence=h.palette)
        fig.write_html("./Demo_Files/Marketing/FigureByTime.html")
        return fig
    
    def getFigureByArea():
        data = marketingData.fetch("")
        df = pd.DataFrame({
            "Amount": data[3],
            "Date": data[0],
            "Material": data[1],
            "Area" : data[2]
        })
        df = df.sort_values("Material")
        
        fig = px.bar(df, x="Date", y="Amount", color="Area", hover_name="Material")
        fig.write_html("./Demo_Files/Marketing/FigureByArea.html")
        return fig
        