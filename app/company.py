#odata
import requests
import pyodata
import pandas as pd

#classes
from app.service import service
from app.helper import helper as h

class companyData:
    
    def fetch():
        valuation = []
        dates = []
    
        p = service.theservice.entity_sets.Company_Valuation.get_entities()
        for p_ in p.execute():
            val = p_.COMPANY_VALUATION
            date = p_.SIM_DATE
            date = h.formatDate(date)
            
            
            valuation.append(float(val))
            dates.append(date)
        return [valuation, dates]

# Visualization
import plotly.express as px

class companyVisualization:
    def getFigure():
        df = pd.DataFrame({
            "Company Valuation": companyData.fetch()[0],
            "Date": companyData.fetch()[1]
        })

        fig = px.line(df, x="Date", y="Company Valuation")
        return fig