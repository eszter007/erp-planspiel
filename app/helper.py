#datetime
from datetime import datetime

class helper:
    def formatDate(date):
        date = datetime.strptime(date, '%m/%d').replace(year=2021)
        return date