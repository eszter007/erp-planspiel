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
        customers = []
        
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
            customer = p_.DISTRIBUTION_CHANNEL
            customer = h.getCustomer(customer)
            
            materials.append(material)
            dates.append(date)
            quantities.append(quantity)
            prices.append(price)
            costs.append(cost)
            margins.append(price-cost)
            areas.append(area)
            customers.append(customer)
            
        return [materials, dates, quantities, prices, costs, margins, areas, customers]
    
    def fetchOwnPrices():
        dates = []
        prices = []
        customers = []
        materials = []
        
        p = service.theservice.entity_sets.Pricing_Conditions.get_entities()
        for p_ in p.execute():
            date = p_.SIM_DATE
            date = h.formatDate(date)
            material = p_.MATERIAL_DESCRIPTION
            customer = p_.DC_NAME
            price = p_.PRICE
            price = float(price)
            
            dates.append(date)
            materials.append(material)
            customers.append(customer)
            prices.append(price)

        return [dates, materials, customers, prices]
            

# Visualization
import plotly.express as px

class salesVisualization:
    data = salesData.fetch()
    def getAmountSoldFigure():
        data = salesVisualization.data
        df = pd.DataFrame({
            "Quantity": data[2],
            "Date": data[1],
            "Material": data[0],
            "Price": data[3],
            "Area": data[6],
            "Customer": data[7]
        })
        df = df.sort_values("Material")

        fig = px.bar(df, x="Date", y="Quantity", color="Material", hover_data=["Price", "Area", "Customer"])
        return fig
    
    def getAmountSoldPerDistributionChannelFigure():
        data = salesVisualization.data
        df = pd.DataFrame({
            "Quantity": data[2],
            "Date": data[1],
            "Material": data[0],
            "Price": data[3],
            "Area": data[6],
            "Customer": data[7]
        })
        df = df.sort_values("Material")

        fig = px.bar(df, x="Date", y="Quantity", color="Customer", hover_data=["Price", "Area", "Material"])
        return fig
    
    def getMarginFigure():
        data = salesVisualization.data
        df = pd.DataFrame({
            "Date": data[1],
            "Material": data[0],
            "Price": data[3],
            "Cost": data[4],
            "Margin": data[5]
        })
        df = df.sort_values("Material")

        fig = px.scatter(df, x="Date", y="Margin", color="Material", hover_data=["Price", "Cost"])
        return fig

    def getSalePerAreaFigure():
        data = salesVisualization.data
        df = pd.DataFrame({
            "Material": data[0],
            "Area": data[6],
            "Quantity": data[2],
            "Price": data[3]
        })
        df = df.sort_values("Material")

        fig = px.bar(df, x="Area", y="Quantity", color="Material", hover_data=["Price"], barmode="group")
        return fig
    
    def getMostPopularProductFigure():
        data = salesVisualization.data
        df = pd.DataFrame({
            "Material": data[0],
            "Area": data[6],
            "Quantity": data[2],
            "Price": data[3]
        })
        df = df.sort_values(["Quantity"]).reset_index(drop=True)
        df = df.sort_values("Material")
        
        fig = px.bar(df, x="Material", y="Quantity", color="Area", hover_data=["Price"])
        return fig
    
    def getOwnPricesOverTime():
        data = salesVisualization.data
        df = pd.DataFrame({
            "Date" : data[0],
            "Material" : data[1],
            "Customer" : data[2],
            "Price" : data[3]
        })
        df = df.sort_values("Material")
        
        fig = px.scatter(df, x="Date", y="Price", hover_data=["Customer"], color="Material", color_discrete_sequence=h.palette)
        fig.update_yaxes(dtick=0.5) 
        
        return fig