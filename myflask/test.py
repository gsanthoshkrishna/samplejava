import plotly.offline as py
import plotly.graph_objs as go


def plotPie():
    labels = ['BANK','IT','PHARMA','METAL']
    values = [10,20,30,40]
    trace = go.pie(labels = labels, values = values)
    pi.iplot([trace],filename='basic_pie_chart')


