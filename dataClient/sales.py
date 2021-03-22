#odata
import requests
import pyodata
import pandas as pd

#classes
from dataClient.service import service
from dataClient.helper import helper as h

class salesData:
    
    def fetch():
        materials = []
        dates = []
        quantities = []
        prices = []
        costs = []
        areas = []
        margins = []
        
        p = service.theservice.entity_sets.Sales.get_entities()
        for p_ in p.execute():
            material = p_.MATERIAL_DESCRIPTION
            date = p_.SIM_DATE
            date = h.formatDate(date)
            quantity = p_.QUANTITY
            quantity = float(quantity)
            price = p_.NET_PRICE
            price = float(price)
            cost = p_.COST
            cost = float(cost) / quantity
            area = p_.AREA
            
            materials.append(material)
            dates.append(date)
            quantities.append(quantity)
            prices.append(price)
            costs.append(cost)
            margins.append(price-cost)
            areas.append(area)
            
        return [materials, dates, quantities, prices, costs, margins, areas]

# Visualization
import plotly.express as px

class salesVisualization:
    def getAmountSoldFigure():
        df = pd.DataFrame({
            "Quantity": salesData.fetch()[2],
            "Date": salesData.fetch()[1],
            "Material": salesData.fetch()[0],
            "Price": salesData.fetch()[3],
            "Area": salesData.fetch()[6]
        })

        fig = px.bar(df, x="Date", y="Quantity", color="Material", hover_data=["Price", "Area"])
        return fig
    
    def getMarginFigure():
        df = pd.DataFrame({
            "Date": salesData.fetch()[1],
            "Material": salesData.fetch()[0],
            "Price": salesData.fetch()[3],
            "Cost": salesData.fetch()[4],
            "Margin": salesData.fetch()[5]
        })

        fig = px.scatter(df, x="Date", y="Margin", color="Material", hover_data=["Price", "Cost"])
        return fig

    def getSalePerAreaFigure():
        df = pd.DataFrame({
            "Material": salesData.fetch()[0],
            "Area": salesData.fetch()[6],
            "Quantity": salesData.fetch()[2],
            "Price": salesData.fetch()[3]
        })

        fig = px.bar(df, x="Area", y="Quantity", color="Material", hover_data=["Price"], barmode="group")
        return fig