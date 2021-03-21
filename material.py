#odata
import requests
import pyodata
import pandas as pd

#classes
from service import service

class materialData:
    
    def fetch(typeOfMaterial, unitType, size):
        materials = []
        dates = []
        quantities = []
    
        p = service.theservice.entity_sets.Goods_Movements.get_entities()
        for p_ in p.execute():
            material = p_.MATERIAL_DESCRIPTION
            date = p_.SIM_DATE
            date = service.formatDate(date)
            quantity = p_.QUANTITY_ABS
            materialType = p_.MATERIAL_TYPE 
            unit = p_.UNIT
            
            if materialType == typeOfMaterial and unitType in unit and size in material:
                quantities.append(float(quantity))
                dates.append(date)
                materials.append(material)
        return [materials, dates, quantities]

#
import plotly.express as px

class materialVisualization:
    def getFigure(typeOfMaterial, unitType, size):
        df = pd.DataFrame({
            "Quantity": materialData.fetch(typeOfMaterial, unitType, size)[2],
            "Date": materialData.fetch(typeOfMaterial, unitType, size)[1],
            "Material": materialData.fetch(typeOfMaterial, unitType, size)[0]
        })

        fig = px.bar(df, x="Date", y="Quantity", color="Material")
        return fig