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
            date = p_.SIM_DATE
            if h.correctDateFormat(date):
                material = p_.MATERIAL_DESCRIPTION
                date = h.formatDate(date)
                price = p_.NET_PRICE
                vendor = p_.VENDOR_NAME
                
                materials.append(material)
                dates.append(date)
                prices.append(float(price))
                vendors.append(vendor)
            else: continue
        return [materials, dates, prices, vendors]

# Visualization
import plotly.express as px

class supplierVisualization:
    data = supplierData.fetch()
    def getFigure():
        data = supplierVisualization.data
        df = pd.DataFrame({
            "Material":data[0],
            "Date":data[1],
            "Price":data[2],
            "Vendor":data[3],
        })
        
        fig = px.line(df, x="Date", y="Price", color="Material", hover_data=["Material", "Price", "Vendor"])
        fig.update_yaxes(dtick=0.5)
        fig.update_xaxes(
            dtick="M1",
            tickformat="%b\n%Y")
        fig.write_html("./Demo_Files/Suppliers/Figure.html")
        return fig