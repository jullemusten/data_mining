#print("hello world coolt")

#list = [1, 2, 3, 4, 5]
#for i in list:
#    print("coolt" , i)
import csv
import pandas

#def get_csv_death():
#    data = open("data_roadtrafficdeath.csv")
#    type(data)
#    csvreader = csv.reader(data, delimiter=',')

def get_nodes():
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

print(get_nodes())

