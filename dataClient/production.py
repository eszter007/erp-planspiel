#odata
import requests
import pyodata
import pandas as pd

#classes
from dataClient.service import service
from dataClient.helper import helper as h

class productionData:
    def fetchProductionData():
        dates = []
        materials = []
        yields = []
    
        p = service.theservice.entity_sets.Production.get_entities()
        for p_ in p.execute():
            date = p_.SIM_DATE
            if h.correctDateFormat(date):
                date = h.formatDate(date)
                material = p_.MATERIAL_DESCRIPTION
                pyield = p_.YIELD
                
                materials.append(material)
                dates.append(date)
                yields.append(int(pyield))
            else: continue
        return [dates, materials, yields]
    
    def fetchProductionOrderData():
        dates = []
        materials = []
        productionOrders = []
        targetQuantities = []
        confirmedQuantities = []
    
        p = service.theservice.entity_sets.Production_Orders.get_entities()
        for p_ in p.execute():
            date = p_.SIM_DATE
            if h.correctDateFormat(date):
                date = h.formatDate(date)
                material = p_.MATERIAL_DESCRIPTION
                productionOrder = p_.PRODUCTION_ORDER
                productionOrder = int(productionOrder)
                targetQuantity = p_.TARGET_QUANTITY
                targetQuantity = int(targetQuantity)
                confirmedQuantity = p_.CONFIRMED_QUANTITY
                confirmedQuantity = int(confirmedQuantity)
                
                materials.append(material)
                dates.append(date)
                productionOrders.append(productionOrder)
                targetQuantities.append(targetQuantity)
                confirmedQuantities.append(confirmedQuantity)
            else: continue
        return [dates, materials, productionOrders, targetQuantities, confirmedQuantities]
    
    def fetchPurchaseOrderData():
        dates = []
        materials = []
        quantities = []
    
        p = service.theservice.entity_sets.Purchase_Orders.get_entities()
        for p_ in p.execute():
            material = p_.MATERIAL_DESCRIPTION
            date = p_.SIM_DATE
            date = h.formatDate(date)
            quantitity = p_.QUANTITY
            quantitity = float(quantitity)
            
            materials.append(material)
            dates.append(date)
            quantities.append(quantitity)
        return [dates, materials, quantities]

# Visualization
import plotly.express as px

class productionVisualization:
    prodData = productionData.fetchProductionData()
    prodOrderData = productionData.fetchProductionOrderData()
    purchaseOrderData = productionData.fetchPurchaseOrderData()
    
    #
    # Production
    #
    def getProductionFigure():
        data = productionVisualization.prodData
        df = pd.DataFrame({
            "Date":data[0],
            "Material":data[1],
            "Yield":data[2]
        })
        df = df.sort_values("Material")
        
        fig = px.bar(df, x="Date", y="Yield", color="Material")
        fig.write_html("./Demo_Files/Production/ProductionFigure.html")
        return fig
    
    #
    # Production Order
    #
    
    def getTargetQuantityFigure():
        data = productionVisualization.prodOrderData
        df = pd.DataFrame({
            "Date":data[0],
            "Material":data[1],
            "Target Quantity":data[3]
        })
        df = df.sort_values("Material")
        
        fig = px.bar(df, x="Date", y="Target Quantity", color="Material")
        fig.write_html("./Demo_Files/Production/TargetQuantity.html")
        return fig
    
    def getConfirmedQuantityFigure():
        data = productionVisualization.prodOrderData
        df = pd.DataFrame({
            "Date":data[0],
            "Material":data[1],
            "Confirmed Quantity":data[4]
        })
        df = df.sort_values("Material")
        
        fig = px.bar(df, x="Date", y="Confirmed Quantity", color="Material")
        fig.write_html("./Demo_Files/Production/ConfirmedQuantity.html")
        return fig
    
    #
    # Purchase Orders
    #
    
    def getPurchaseOrderFigure():
        data = productionVisualization.purchaseOrderData
        df = pd.DataFrame({
            "Date":data[0],
            "Material":data[1],
            "Purchase Order":data[2]
        })
        df = df.sort_values("Material")
        
        fig = px.bar(df, x="Date", y="Purchase Order", color="Material")
        fig.write_html("./Demo_Files/Production/PurchaseOrder.html")
        return fig
    
    def getProductivityFigure():
        data = {
            "January": 81.786,
            "February": 66.786,
            "March": 83.690,
            "April": 50.834,
            "May": 65.833,
            "June": 81.736,
            "July": 91.666,
            "August": 86.429,
            "September": 89.999,
            "October": 89.166,
            "November": 80.943,
            "December": 79.524
        }
        df = pd.DataFrame.from_dict(list(data.items()))
        df.columns = ["Month", "Productivity in %"]

        fig = px.line(df, x="Month", y="Productivity in %")
        fig.write_html("./Demo_Files/Production/ProductivityInPercent.html")
        return fig
