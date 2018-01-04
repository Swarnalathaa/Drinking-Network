# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 19:25:40 2017

@author: swarnalathaa
"""
import pandas as pd

filename = input('Enter a filename: ')
xl = pd.ExcelFile(filename)
sheets = xl.sheet_names
print("With sheets")
print(sheets)

V = input('Enter the sheet name of valves:')
valves = pd.read_excel(filename,V)
print("With columns")
valve_col = list(valves)
print(valve_col)

P = input('Enter the sheet name of pipes:')
pipes =  pd.read_excel(filename,P)
print("WIth columns")
pipe_col = list(pipes)
print(pipe_col)

valves_node1 = valves['Node1'].values.tolist()
valves_node2 = valves['Node2'].values.tolist()
valve_ID = valves['ID'].values.tolist()

pipes_node1 = pipes['Node1'].values.tolist()
pipes_node2 = pipes['Node2'].values.tolist()
pipe_ID = pipes['ID'].values.tolist() 



adjacent_pipes = []
adjacent_valves = []

# For all pipes looking for all adjacent pipes and creating a adjacency list 
for i in range(0,len(pipes_node1)):
    inter = []
    
    for j in range(0,len(pipes_node1)):
        
        if i != j:
            if pipes_node1[i] == pipes_node1[j] or pipes_node1[i] == pipes_node2[j]:
                inter.append(j)
            elif pipes_node2[i] == pipes_node1[j] or pipes_node2[i] == pipes_node2[j]:
                inter.append(j)
            else:
                pass
    adjacent_pipes.append(inter)

# For all valves looking for all adjacent valves and pipes and creating a adjacency list
for i in range(0,len(pipes_node1)):
    inter = []
    
    for j in range(0,len(valves_node1)):
        
        if i != j:
            if pipes_node1[i] == valves_node1[j] or pipes_node1[i] == valves_node2[j]:
                inter.append(j)
            elif pipes_node2[i] == valves_node1[j] or pipes_node2[i] == valves_node2[j]:
                inter.append(j)
            else:
                pass
    adjacent_valves.append(inter)

loop = 1

def DFS(n,adjacent_pipes,adjacent_valves):
    
    # DFS to travese through graph and find the valves to close
    visited = []
    stack = []
    valve_closei = []
    stack.append(n)
    
    while stack:
        s = stack[0]
        del stack[0]
        
        if s not in visited:
            visited.append(s)
            stack = stack + adjacent_pipes[s]
            valve_closei = valve_closei + adjacent_valves[s]
            # to remove any duplicates in the valve list
    
    valve_closei = list(set(valve_closei))
            
    valve_close = []
    
    # getting the valve ID
    
    for i in range(len(valve_closei)):
        valve_close.append(valve_ID[i])
    
    print('The valves to be closed are:')
    
    print(valve_close)


print("To get the list of valves to be closed to isolate the pipe type pipe_isolate():") 
    
def pipe_isolate():
    #pipe_isolate = input("Enter the ID of Pipe to isolate :")
    pipe_isolate = input("Enter the pipe to isolate:")
    pipe_ind = pipe_ID.index(pipe_isolate) 
    
    DFS(pipe_ind,adjacent_pipes,adjacent_valves)
    
    print("To isolate another pipe pipe type pipe_isolate():")
    


    

    
        
        
        
        