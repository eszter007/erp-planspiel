#datetime
from datetime import datetime

class helper:
    palette = ["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A", "#19D3F3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52", "#0CBABA", "#861657"]
    
    def formatDate(date):
        date = datetime.strptime(date, '%m/%d').replace(year=2021)
        return date
    
    def correctDateFormat(date):
        if date[:2] == "13" or not date:
            return False
        else: return True
    
    def getCustomer(customer):
        if customer == "12":
            customer = "Grocery Chains"
        elif customer == "10": 
            customer = "Hypermarkets"
        elif customer == "14":
            customer = "Independent Grocers"
            
        return customer