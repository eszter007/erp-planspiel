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
            date = p_.SIM_DATE
            if h.correctDateFormat(date):
                date = h.formatDate(date)
                material = p_.MATERIAL_DESCRIPTION
                quantity = p_.QUANTITY
                quantity = float(quantity)
                price = p_.NET_PRICE
                price = float(price)
                cost = p_.COST
                cost = float(cost) / quantity
                area = p_.AREA
                customer = p_.DISTRIBUTION_CHANNEL
                customer = h.getCustomer(customer)
                margin = p_.CONTRIBUTION_MARGIN
                margin = float(margin)
                
                materials.append(material)
                dates.append(date)
                quantities.append(quantity)
                prices.append(price)
                costs.append(cost)
                margins.append(margin/quantity)
                areas.append(area)
                customers.append(customer)
            else: continue
            
        return [materials, dates, quantities, prices, costs, margins, areas, customers]
    
    def fetchOwnPrices():
        dates = []
        prices = []
        customers = []
        materials = []
        
        p = service.theservice.entity_sets.Pricing_Conditions.get_entities()
        for p_ in p.execute():
            date = p_.SIM_DATE
            if h.correctDateFormat(date):
                date = h.formatDate(date)
                material = p_.MATERIAL_DESCRIPTION
                customer = p_.DC_NAME
                price = p_.PRICE
                price = float(price)
                
                dates.append(date)
                materials.append(material)
                customers.append(customer)
                prices.append(price)
            else: continue

        return [dates, materials, customers, prices]
            

# Visualization
import plotly.express as px

class salesVisualization:
    data = salesData.fetch()
    ownPrices = salesData.fetchOwnPrices()
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
        fig.update_xaxes(
            dtick="M1",
            tickformat="%b\n%Y")
        fig.write_html("./Demo_Files/Sales/AmountSold.html")
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
        fig.update_xaxes(
            dtick="M1",
            tickformat="%b\n%Y")
        fig.write_html("./Demo_Files/Sales/AmountSoldPerDistributionChannel.html")
        return fig
    
    def getMarginFigure():
        data = salesVisualization.data
        df = pd.DataFrame({
            "Date": data[1],
            "Material": data[0],
            "Price": data[3],
            "Variable Cost": data[4],
            "Margin": data[5]
        })
        df = df.sort_values("Material")

        fig = px.scatter(df, x="Date", y="Margin", color="Material", hover_data=["Price", "Variable Cost"])
        fig.update_xaxes(
            dtick="M1",
            tickformat="%b\n%Y")
        fig.write_html("./Demo_Files/Sales/Margin.html")
        return fig
    
    def getCostFigure():
        data = salesVisualization.data
        df = pd.DataFrame({
            "Date": data[1],
            "Material": data[0],
            "Cost per Unit": data[4]
        })
        df = df.sort_values("Material")

        fig = px.line(df, x="Date", y="Cost per Unit", color="Material")
        fig.update_xaxes(
            dtick="M1",
            tickformat="%b\n%Y")
        fig.write_html("./Demo_Files/Sales/Costs.html")
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
        fig.update_traces(marker_line_width=0)
        fig.update_xaxes(
            dtick="M1",
            tickformat="%b\n%Y")
        fig.write_html("./Demo_Files/Sales/SalesPerArea.html")
        return fig
    
    def getMostPopularProductFigure():
        data = salesVisualization.data
        df = pd.DataFrame({
            "Material": data[0],
            "Area": data[6],
            "Quantity": data[2],
            "Price": data[3]
        })
        fig = px.bar(df, x="Material", y="Quantity", color="Area", hover_data=["Price"])
        fig.update_traces(marker_line_width=0)
        fig.update_xaxes(
            dtick="M1",
            tickformat="%b\n%Y")
        fig.write_html("./Demo_Files/Sales/MostPopular.html")
        return fig
    
    def getOwnPricesOverTime():
        data = salesVisualization.ownPrices
        df = pd.DataFrame({
            "Date" : data[0],
            "Material" : data[1],
            "Customer" : data[2],
            "Price" : data[3]
        })
        df = df.sort_values("Material")
        
        fig = px.scatter(df, x="Date", y="Price", hover_data=["Customer"], color="Material", color_discrete_sequence=h.palette)
        fig.update_yaxes(dtick=0.5) 
        fig.update_xaxes(
            dtick="M1",
            tickformat="%b\n%Y")
        fig.write_html("./Demo_Files/Sales/OwnPricesOverTime.html")
        return fig