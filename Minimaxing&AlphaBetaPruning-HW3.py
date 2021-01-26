#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Nov 16 22:14:11 2020

@author: muhammedburakgormus
"""
#For single stepping, please set the single_step True
single_step = False
##########################################################################################################################
##########################################################################################################################
#Creating Nodes Class to define the nodes
class Nodes():
    
    def __init__(self,number):
        #taking integers as its attribute
        self.number = number
        self.parent = None
        
    def __repr__(self):
        #representing the objects
        return '%s' % self.number 
    
    def __eq__(self,other):
        #checking the equality
        if self.number != other.number:
            return False
        else:
            return True
            
    def __lt__(self,other):
        #lt method is created here to sort the objects in a list
        if self.number < other.number:
            return True
        if self.number >= other.number:
            return False
    
    def get_int(self):
        #taking an integer value of the object
        return self.number
##########################################################################################################################
##########################################################################################################################



##########################################################################################################################
##########################################################################################################################
def generate_leafs(input_string):
    #taking the input as a string and splitting the numbers from space character
    #converting the strings splitted into integers 
    #creating objects from these inputs and returning an object list
    listed_values = input_string.split()
    obj_list = []
    for i in listed_values: 
        int_converted = int(i)
        new_obj = Nodes(int_converted)
        obj_list.append(new_obj)
    return obj_list

def straight_minimaxing(obj_list,mode_selection):
    #takes the objects lists that has a length of 9(leaf nodes)
    #returns the value carried out to the root node
    tripled_list = []
    min_list = []
    counter = 0 
    for i in range(9):
        tripled_list.append(obj_list[i])
        counter = counter + 1
        if counter == 3:
            minimum = min(tripled_list)
            min_list.append(minimum)
            counter = 0 
            tripled_list = []
    my_index = min_list.index(max(min_list))
    if mode_selection == 2:
        print("")
        print("The minimizer chooses the values as follows: ")
        print(min_list)
        print("")
        print("The value chosen by the maximizer is:"+str(max(min_list)))
        print("The index of this value is:"+str(my_index))
        print("İndices 0, 1 and 2 represent left, middle and right respectively")
        print("Therefore; ")
        print("")
    if my_index == 0:
        print("Goes to L(Left)")
    elif my_index == 1: 
        print("Goes to M(Middle)")
    else:
        print("Goes to R(Right)")    
    my_string = "Chosen path leads to the leaf node:"+str((max(min_list)))
    return my_string

def alphabeta(obj_list,mode_selection):
    #takes the objects lists that has a length of 9(leaf nodes)
    #returns the value carried out to the root node and a list containing pruned objects    
    pruned_list=[]
    pruned_indices = []
    my_tuple = ((0,"A"),(1,"B"),(2,"C"),(3,"D"),(4,"E"),(5,"F"),(6,"G"),(7,"H"),(8,"I"))
    first_list = []
    which_node = 1
    for i in range(3):
        first_list.append(obj_list[i])
        if mode_selection == 2: 
            print(str(obj_list[i])+" is checked")
            print("")
    first_min = min(first_list)
    
    if mode_selection == 2: 
        print("The minimum of first three values(A,B,C) is "+str(first_min))
        print("")
        
    second_list = []
    for s in range(3,6,1):
        if obj_list[s] > first_min: 
            if mode_selection == 2: 
                print(str(obj_list[s])+" is checked")
                print("")
            second_list.append(obj_list[s])
        if obj_list[s].get_int() <= first_min.get_int(): 
            if mode_selection == 2: 
                print(str(obj_list[s])+" is checked")
                print("")
            for m in range(s+1,6):
                pruned_list.append(obj_list[m])
                pruned_indices.append(m)
                if mode_selection == 2: 
                    print(str(obj_list[m])+" is pruned")
                    print("")
            break   
        
    if len(second_list) == 3: 
        second_min = min(second_list)
        which_node = 2
        first_min = second_min
        
    if mode_selection == 2:
        print("After checking the first six nodes and comparing the left and middle branch, the value to be carried to the top is "+str(first_min))
        print("")
        
    third_list = []
    for k in range(6,9,1):
        if obj_list[k] > first_min: 
            if mode_selection == 2: 
                print(str(obj_list[k])+" is checked")
                print("")
            third_list.append(obj_list[k])   
        if obj_list[k].get_int() <= first_min.get_int(): 
            if mode_selection == 2:
                print(str(obj_list[k])+" is checked")
                print("")
            for j in range(k+1,9):
                pruned_list.append(obj_list[j])
                pruned_indices.append(j)
                if mode_selection == 2: 
                    print(str(obj_list[j])+" is pruned")
                    print("")
            break   
        
    if len(third_list) == 3: 
        third_min = min(third_list)
        which_node = 3
        first_min = third_min
    
    if mode_selection == 2:
        print("After checking all the nodes and comparing lastly with the right branch, the value to be carried to the top is "+str(first_min))
        print("")
    
    if which_node == 1:
        print("Goes to L(Left)")
    elif which_node == 2:
        print("Goes to M(Middle)")
    else:
        print("Goes to R(Right)")    
    
    my_str = "Chosen path leads to the leaf node:"+str(first_min)+"\nThe pruned list is:"+ str(pruned_list)
    name_str = ""
    
    for elements in pruned_indices: 
        for tuples in my_tuple:
            if elements ==tuples[0]:
                name_str = name_str +str(tuples[1])+ " "
    name_str = name_str + "pruned"
    my_str = my_str + "\n" + name_str

    return my_str

##########################################################################################################################
##########################################################################################################################
mode_selection = int(single_step)+1
print("")

problem_selection = input("For the first problem in Minimaxing please enter 1\nFor the custom problem in Minimaxing please enter 2\nFor the first problem in AlphaBeta please enter 3\nFor the second problem in AlphaBeta please enter 4\nFor the third problem in AlphaBeta please enter 5\nFor the custom problem in AlphaBeta please enter 6: ")
problem_selection = int(problem_selection)
print("")

##########################################################################################################################
##########################################################################################################################       
#TEST DATA FOR MINIMAX
#BULLETPOINT1 
if problem_selection == 1:
    problem1_list = [5,3,1,2,5,4,1,3,3]
    problem1_objects = []
    for elements in problem1_list:
        problem1_objects.append(Nodes(elements))
    print("For the first problem in Minimaxing (A=5 B=3 C=1 D=2 E=5 F=4 G=1 H=3 I=3):")
    print("")
    print(straight_minimaxing(problem1_objects,mode_selection)) 
    print("")
  
##########################################################################################################################
##########################################################################################################################      


##########################################################################################################################
##########################################################################################################################       
#TEST DATA FOR MINIMAX
#BULLETPOINT2 
if problem_selection == 2:
    print("For the second problem in Minimaxing Please Enter the input values by seperating them with a space")
    a = input("Enter: ")
    print("")
    print(straight_minimaxing(generate_leafs(a),mode_selection))
    print("")
##########################################################################################################################
##########################################################################################################################     



##########################################################################################################################
##########################################################################################################################       
#TEST DATA FOR ALPHABETA
#BULLETPOINT1 
if problem_selection == 3:
    problem3_list = [5,3,1,2,5,4,1,3,3]
    problem3_objects = []
    for elements in problem3_list:
        problem3_objects.append(Nodes(elements))
    print("For the first problem in AlphaBeta (A=5 B=3 C=1 D=2 E=5 F=4 G=1 H=3 I=3):")
    print("")
    print(alphabeta(problem3_objects,mode_selection))    
    print("")
##########################################################################################################################
##########################################################################################################################      

##########################################################################################################################
##########################################################################################################################       
#TEST DATA FOR ALPHABETA
#BULLETPOINT2
if problem_selection == 4:
    problem4_list = [5,2,2,5,1,3,2,4,2]
    problem4_objects = []
    for elements in problem4_list:
        problem4_objects.append(Nodes(elements))
    print("For the second problem in AlphaBeta (A=5 B=2 C=2 D=5 E=1 F=3 G=2 H=4 I=2):")
    print("")
    print(alphabeta(problem4_objects,mode_selection))  
    print("")  
##########################################################################################################################
##########################################################################################################################      


##########################################################################################################################
##########################################################################################################################       
#TEST DATA FOR ALPHABETA
#BULLETPOINT3
if problem_selection == 5:
    problem5_list = [1,3,4,1,4,1,3,5,3]
    problem5_objects = []
    for elements in problem5_list:
        problem5_objects.append(Nodes(elements))
    print("For the second problem in AlphaBeta (A=1 B=3 C=4 D=1 E=4 F=1 G=3 H=5 I=3):")
    print("")
    print(alphabeta(problem5_objects,mode_selection)) 
    print("")  
#########################################################################################################################
##########################################################################################################################      


##########################################################################################################################
##########################################################################################################################       
#TEST DATA FOR ALPHABETA
#BULLETPOINT4
if problem_selection == 6:
    print("For the fourth problem in AlphaBeta Please Enter the input values by seperating them with a space")
    b = input("Enter: ")
    print("")
    print(alphabeta(generate_leafs(b),mode_selection))
##########################################################################################################################
##########################################################################################################################      







        
        