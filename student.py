import csv
import plotly.express as px
import numpy as np

def plotgraph(path):
    with open(path) as csv_file:
        df=csv.DictReader(csv_file)
        fitfigure=px.scatter(df,x='Days Present',y='Marks In Percentage')
        fitfigure.show()

def getDataSource(path):
    Marks_In_Percentage=[]
    Days_Present=[]
    with open(path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            Marks_In_Percentage.append(float(row['Marks In Percentage']))
            Days_Present.append(float(row['Days Present']))
    return{'x':Marks_In_Percentage,'y':Days_Present}

def findcorelation(dataSource):
    corelation=np.corrcoef(dataSource['x'],dataSource['y'])
    print('Co-Relation Between Marks In Percentage and Days Present-\n',corelation[0,1])

def setup():
    path='student attendance.csv'
    dataSource=getDataSource(path)
    findcorelation(dataSource)
    plotgraph(path)

setup()