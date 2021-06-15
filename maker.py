import PySimpleGUI as sg
import numpy as np
import pandas as pd
import holoviews as hv
import matplotlib
from holoviews import opts, dim

hv.extension("matplotlib")
hv.output(fig='png', size=500)

def chordMaker(file):
    df = pd.read_csv(file, sep=';')
    names = df['Labels']
    dataset = []
    for i in range(len(df)):
        for name in names:
            ipt = df.iloc[i]['Labels']
            otp = name
            if df.iloc[i][name]==1:
                dataset.append([ipt,otp,1])
    
    
    namesList = hv.Dataset(pd.DataFrame(list(names), columns=['Labels']))
    chord = hv.Chord((dataset,namesList))
    return chord


settings = [[sg.Text("Select matrix"),sg.FileBrowse()],
            [sg.Text("Title"),sg.Input("Title", key='Title')],
            [sg.Text("Edge width"), sg.Input("2", key='Edge Width')],
            [sg.Text("Node Size"), sg.Input("15", key='Node Size')],
            [sg.Text("File Name"), sg.Input("Output", key='File Name')]
           ]
            
run = [[sg.Button("Generate Chard")]]
layout = [[sg.Column(settings),
           sg.VSeperator(),
           sg.Column(run)]]

window = sg.Window(title="Chard Diagram Maker", layout=layout)

while True:
    event, values = window.read()
    if event == "Generate Chard":
        print(values['Browse'])
        print(values['Title'])
        title = values['Title']
        node_size = int(values['Node Size'])
        edge_width = int(values['Edge Width'])
        file_name = values['File Name']
        chord = chordMaker(values['Browse'])
        chord.opts(node_color="Labels", 
                   node_cmap="Category20", 
                   edge_color="Labels", 
                   edge_cmap="Category20", 
                   title=title,
                   labels="Labels",
                   node_size=node_size,
                   edge_linewidth=edge_width)
        hv.save(chord, file_name+'.png', fmt='png')

        
        
    if event == sg.WIN_CLOSED:
        break
