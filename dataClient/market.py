#odata
import requests
import pyodata
#plotly
import pandas as pd
import plotly.graph_objects as go
from itertools import cycle
#classes
from dataClient.service import service
from dataClient.helper import helper as h

class marketData:
    
    def fetch():
        materials= []
        areas = []
        quantities = []
        prices = []
        periods = []
        dcs = []
    
        p = service.theservice.entity_sets.Market.get_entities()
        for p_ in p.execute():
            description = p_.MATERIAL_DESCRIPTION 
            area = p_.AREA
            quantity = p_.QUANTITY
            price = p_.AVERAGE_PRICE
            period = p_.SIM_PERIOD
            period = int(period)
            dc = p_.DISTRIBUTION_CHANNEL
            dc = h.getCustomer(dc)
            
            
            materials.append(description)
            areas.append(area)
            quantities.append(float(quantity))
            prices.append(float(price))
            periods.append(period)
            dcs.append(dc)
        return [materials, areas, quantities, prices, periods, dcs]

# Visualization
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
        df = df.sort_values("Material")
        
        fig = px.bar(df, x="Area", 
                     y="Quantity", 
                     color="Material", 
                     hover_data=["Area", "Quantity", "Price"], 
                     barmode='group', 
                     color_discrete_sequence=h.palette)
        return fig
    
    def getMostPopularProduct():
        data = marketData.fetch()
        df = pd.DataFrame({
            "Quantity": data[2],
            "Material": data[0],
            "Price": data[3],
            "Area": data[1]
        })
        df = df.sort_values("Material")
        
        fig = px.bar(df, x="Material", 
                     y="Quantity", 
                     color="Area", 
                     hover_data=["Price"])
        return fig
    
    def getPriceAndAmount():
        data = marketData.fetch()
        df = pd.DataFrame({
            "Quantity": data[2],
            "Material": data[0],
            "Area": data[1],
            "Price": data[3]
        })
        df = df.sort_values("Material")
        
        fig = px.scatter(df, x="Price", 
                         y="Quantity", 
                         color="Material", 
                         size="Quantity", 
                         hover_data=["Area", "Quantity", "Price"], 
                         color_discrete_sequence=h.palette)
        fig.update_xaxes(dtick=0.5) 
        
        return fig
    
    def getAveragePrice():
        data = marketData.fetch()
        df = pd.DataFrame({
            "Material": data[0],
            "Quantity": data[2],
            "Price": data[3]
        })
        
        muesliDict = dict()

        #print(df.sort_values(by=["Price"]))
        for index, row in df.iterrows():
            if row["Quantity"] == 0:
                continue
            
            materialName = row["Material"]

            if materialName in muesliDict:
                minPrice = muesliDict[materialName][0]
                maxPrice = muesliDict[materialName][1] 
                quantity = muesliDict[materialName][2]
                pricePerPurchase = muesliDict[materialName][3]
                
                muesliDict[materialName] = [min(row["Price"], minPrice),
                                            max(row["Price"], maxPrice),
                                            quantity + row["Quantity"],
                                            pricePerPurchase + (row["Quantity"] * row["Price"])]
            else:
                muesliDict[materialName] = [row["Price"],
                                            row["Price"], 
                                            row["Quantity"],
                                            row["Quantity"] * row["Price"]]
            
        for key in muesliDict:
            muesliDict[key] = [muesliDict[key][0], muesliDict[key][1], muesliDict[key][3]/muesliDict[key][2]]
        
        df = pd.DataFrame.from_dict(muesliDict, orient="index", columns=["minimumPrice", "maximumPrice", "averagePrice"])
        df = df.sort_values(df.columns[0])
        
        fig = px.bar(df, x=muesliDict.keys(), y=["minimumPrice", "averagePrice", "maximumPrice"], 
                     barmode="group",
                     labels={
                        "x": "Products",
                        "value": "Price",
                        "variable": "Type"})
        return fig
    
    # Over time data
    def getPricesOverTime():
        data = marketData.fetch()
        df = pd.DataFrame({
            "Material": data[0],
            "Quantity": data[2],
            "Price": data[3],
            "Period": data[4]
        })
        df = df[df.Price != 0]
        df = df.sort_values("Material")
        
        fig = px.scatter(df, x="Period", 
                    y="Price", 
                    color="Material", 
                    size="Quantity", 
                    color_discrete_sequence=h.palette)
        fig.update_yaxes(dtick=0.5) 
        fig.update_xaxes(dtick=1) 
        
        return fig
    
    def getPopularityOverTime():
        data = marketData.fetch()
        df = pd.DataFrame({
            "Material": data[0],
            "Quantity": data[2],
            "Price": data[3],
            "Period": data[4]
        })
        df = df[df.Price != 0]
        df = df.sort_values("Material")
        
        fig = px.bar(df, x="Period", 
                    y="Quantity", 
                    color="Material", 
                    hover_data=["Price"], 
                    color_discrete_sequence=h.palette)
        return fig
    
    def getPurchaseVolumePeriodsFigure():
        data = marketData.fetch()
        df = pd.DataFrame({
            "Material": data[0],
            "Quantity": data[2],
            "Customer": data[5],
            "Price": data[3],
            "Period": data[4]
        })
        df = df[df.Price != 0]
        df = df.sort_values("Material")
        
        fig = px.bar(df, x="Period", 
                    y="Quantity", 
                    color="Customer", 
                    hover_data=["Price", "Quantity"],
                    color_discrete_sequence=h.palette)
        return fig