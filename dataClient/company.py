#odata
import requests
import pyodata
import pandas as pd

#classes
from dataClient.service import service
from dataClient.helper import helper as h

class companyData:
    
    def fetchCompanyValuation():
        dates = []
        
        cashHistory = []
        accReceivables = []
        loanHistory = []
        accPayables = []
        profits = []
        
        debtLoadings = []
        creditRatings = []
        valuation = []
    
        p = service.theservice.entity_sets.Company_Valuation.get_entities()
        for p_ in p.execute():  
            date = p_.SIM_DATE
            date = h.formatDate(date)
            
            cash = p_.BANK_CASH_ACCOUNT
            accReceivable = p_.ACCOUNTS_RECEIVABLE
            loan = p_.BANK_LOAN
            accPayable = p_.ACCOUNTS_PAYABLE
            profit = p_.PROFIT
            
            debtLoading = p_.DEBT_LOADING
            creditRating = p_.CREDIT_RATING
            val = p_.COMPANY_VALUATION
            
            dates.append(date)
            
            cashHistory.append(float(cash))
            accReceivables.append(float(accReceivable))
            loanHistory.append(float(loan))
            accPayables.append(float(accPayable))
            profits.append(float(profit))
            
            debtLoadings.append(float(debtLoading))
            creditRatings.append(creditRating)
            valuation.append(float(val))
            
        return [dates, cashHistory, accReceivables, loanHistory, accPayables, profits, debtLoadings, creditRatings, valuation]

# Visualization
import plotly.express as px

class companyVisualization:
    def getCompanyValuationFigure():
        df = pd.DataFrame({
            "Company Valuation": companyData.fetchCompanyValuation()[8],
            "Date": companyData.fetchCompanyValuation()[0],
            "Credit Rating": companyData.fetchCompanyValuation()[7]
        })

        fig = px.line(df, x="Date", y="Company Valuation", hover_data=["Credit Rating"])
        return fig
    
    def getDebtLoadingProfitsFigure():
        df = pd.DataFrame({
            "Debt Loading": companyData.fetchCompanyValuation()[6],
            "Profit": companyData.fetchCompanyValuation()[5],
            "Cash": companyData.fetchCompanyValuation()[1],
            "Account Receivable": companyData.fetchCompanyValuation()[2],
            "Loans": companyData.fetchCompanyValuation()[3],
            "Account Payables": companyData.fetchCompanyValuation()[4],
            "Credit Rating": companyData.fetchCompanyValuation()[7],
            "Date": companyData.fetchCompanyValuation()[0]
        })

        fig = px.line(df, x="Date", 
                      y=["Debt Loading", "Profit", "Cash", "Account Receivable", "Loans", "Account Payables"],
                      hover_data=["Credit Rating"],
                      labels={"value": "Amount",
                        "variable": "KPI"})
        
        return fig
    
    def getCashProfitsFigure():
        df = pd.DataFrame({
            "Profit": companyData.fetchCompanyValuation()[5],
            "Cash": companyData.fetchCompanyValuation()[1],
            "Account Receivable": companyData.fetchCompanyValuation()[2],
            "Account Payables": companyData.fetchCompanyValuation()[4],
            "Credit Rating": companyData.fetchCompanyValuation()[7],
            "Date": companyData.fetchCompanyValuation()[0]
        })

        fig = px.line(df, x="Date", 
                      y=["Profit", "Cash", "Account Receivable", "Account Payables"],
                      hover_data=["Credit Rating"],
                      labels={"value": "Amount",
                        "variable": "KPI"})
        return fig