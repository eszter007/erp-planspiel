#odata
import requests
import pyodata
import pandas as pd
import plotly.graph_objects as go

#classes
from service import service

class marketData:
    
    def fetch():
        materials= []
        areas = []
        quantities = []
        prices = []
    
        p = service.theservice.entity_sets.Market.get_entities()
        for p_ in p.execute():
            description = p_.MATERIAL_DESCRIPTION 
            area = p_.AREA
            quantity = p_.QUANTITY
            price = p_.AVERAGE_PRICE
            
            materials.append(description)
            areas.append(area)
            quantities.append(float(quantity))
            prices.append(float(price))
        return [materials, areas, quantities, prices]

#
import plotly.express as px

class marketVisualization:
    def getQuantityPerAreaAndMaterial():
        data = marketData.fetch()
        df = pd.DataFrame({
            "Quantity": data[2],
            "Material": data[0],
            "Area": data[1],
            "Price": data[3]
        })
        fig = px.bar(df, x="Area", y="Quantity", color="Material", hover_data=["Area", "Quantity", "Price"], barmode='group')
        return fig
    
    def getPriceAndAmount():
        data = marketData.fetch()
        df = pd.DataFrame({
            "Quantity": data[2],
            "Material": data[0],
            "Area": data[1],
            "Price": data[3]
        })
        fig = px.scatter(df, x="Price", y="Quantity", color="Material", size="Quantity", hover_data=["Area", "Quantity", "Price"])
        return fig        