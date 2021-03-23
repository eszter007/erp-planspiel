#odata
import requests
import pyodata
import pandas as pd

#classes
from dataClient.service import service
from dataClient.helper import helper as h

class supplierData:
    
    def fetch():
        materials = []
        dates = []
        prices = []
        vendors = []
    
        p = service.theservice.entity_sets.Suppliers_Prices.get_entities()
        for p_ in p.execute():
            material = p_.MATERIAL_DESCRIPTION
            date = p_.SIM_DATE
            date = h.formatDate(date)
            price = p_.NET_PRICE
            vendor = p_.VENDOR_NAME
            
            materials.append(material)
            dates.append(date)
            prices.append(float(price))
            vendors.append(vendor)
        return [materials, dates, prices, vendors]

# Visualization
import plotly.express as px

class supplierVisualization:
    def getFigure():
        df = pd.DataFrame({
            "Material":supplierData.fetch()[0],
            "Date":supplierData.fetch()[1],
            "Price":supplierData.fetch()[2],
            "Vendor":supplierData.fetch()[3],
        })

        fig = px.line(df, x="Date", y="Price", color="Material", hover_data=["Material", "Price", "Vendor"])
        return fig