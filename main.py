#print("hello world coolt")

#list = [1, 2, 3, 4, 5]
#for i in list:
#    print("coolt" , i)
import csv
import pandas as pd
from IPython.display import display

#def get_csv_death():
#    data = open("data_roadtrafficdeath.csv")
#    type(data)
#    csvreader = csv.reader(data, delimiter=',')

def get_roadtrafficdeath():
    df_roadtafficdeath = pd.read_csv("data_roadtrafficdeath.csv")
    #df_roadtafficdeath
    display(df_roadtafficdeath.columns)
    #columnn = df_roadtafficdeath.columns
    #print(columnn)
    #location_column = df_roadtafficdeath["Location"]
    #print(location_column)

    df_limit = pd.read_csv("")

    return

#def get_nodes():
    data = open("data_roadtrafficdeath.csv")
    type(data)
    csvreader = csv.reader(data, delimiter=',')
    maze = []
    count = 0

    for row in csvreader:
        int_row=[]
        if count != 0: 
            for element in row:
                int_element = element
                int_row.append(int_element)
        count += 1
        maze.append(int_row[1:])       
    maze.remove(maze[0])
    return maze

#def for_loop(maze):
    for i in maze:
        print(i)

def run():
    #maze = get_nodes()
    #for_loop(maze)
    #return
    get_roadtrafficdeath()

run()

