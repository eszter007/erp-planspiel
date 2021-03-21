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
        
        fig = px.bar(df, x=muesliDict.keys(), y=["minimumPrice","maximumPrice", "averagePrice"], 
                     barmode="group",
                     labels={
                        "x": "Products",
                        "value": "Price",
                        "variable": "Type"})
        return fig
        

marketVisualization.getAveragePrice()