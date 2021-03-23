#odata
import requests
import pyodata
import pandas as pd
import plotly.graph_objects as go

#classes
from dataClient.service import service
from dataClient.helper import helper as h

class satisfactionData:
    
    def fetch():
        dates = []
        materials= []
        areas = []
        averageScores = []
    
        p = service.theservice.entity_sets.NPS_Surveys.get_entities()
        for p_ in p.execute():
            description = p_.MATERIAL_DESCRIPTION 
            date = p_.SIM_DATE
            date = h.formatDate(date)
            area = p_.AREA
            score_0=p_.SCORE_0
            score_1=p_.SCORE_1
            score_2=p_.SCORE_2
            score_3=p_.SCORE_3
            score_4=p_.SCORE_4
            score_5=p_.SCORE_5
            score_6=p_.SCORE_6
            score_7=p_.SCORE_7
            score_8=p_.SCORE_8
            score_9=p_.SCORE_9
            score_10=p_.SCORE_10
            
            scores = [float(score_0), float(score_1), float(score_2), float(score_3), float(score_4), float(score_5), float(score_6), float(score_7), float(score_8), float(score_9), float(score_10)]
            
            totalParticipants = sum(scores)
            scoresSum = sum([scores[0]*0, scores[1]*1, scores[2]*2, scores[3]*3,scores[4]*4, scores[5]*5,scores[6]*6,scores[7]*7,scores[8]*8,scores[9]*9,scores[10]*10])
            averageScore = scoresSum / totalParticipants
            
            averageScores.append(averageScore)
            dates.append(date)
            materials.append(description)
            areas.append(area)
        return [dates, averageScore, materials, areas]

# Visualization
import plotly.express as px

class satisfactionVisualization:
    def getFigure():
        data = satisfactionData.fetch()
        df = pd.DataFrame({
            "Date": data[0],
            "Average Score": data[1],
            "Material" : data[2],
            "Area" : data[3]
        })
        df = df.sort_values("Material")
        
        fig = px.line(df, x="Date", y="Average Score", color="Material", hover_name="Area")
        return fig