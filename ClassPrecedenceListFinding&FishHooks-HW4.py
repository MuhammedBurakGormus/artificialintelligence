#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Nov 24 23:12:50 2020

@author: muhammedburakgormus
"""
tracing_mode = False
problem_choice = int(input("Please Select a problem by entering 1, 2 or 3: "))
print("")
############################################################################################################################################################################################
############################################################################################################################################################################################
def link_creator(a,b,edgelist):
    #this takes two attributes a and b with an edgelist; puts a and b together into a tuple;
    #so creating a link between a and b 
    #adding this link(tuple) to the edgelist
    #returns edgelist
    mytuple = (a,b)
    edgelist.append(mytuple)
    return edgelist

def existing_tree(edgelist,node,extracted_edge_list):
    #this takes an edgelist and a node and a empty list
    #creating a tree that appears from the connections of the taken node 
    #so it basically dismisses the parts of the given edgelist that have no connection with the taken node 
    #it returns an extracted edge list (unconnected parts are removed from the edge list)
    for i in edgelist:
        if i[0] == node :
            extracted_edge_list.append(i)
            existing_tree(edgelist,i[1],extracted_edge_list)
    return extracted_edge_list

def pairs(thelist,paired):
    #this is to make pairs in a given list; for example if we have a list [1,2,3]; this function returns [(1,2),(2,3)]
    #this takes a list and make pairs from the elements in the list and fill the pairs list with the tuples that contains paired elements
    while len(thelist) >= 2:
        paired.append((thelist[0],thelist[1]))
        thelist.pop(0)
        pairs(thelist,paired)
    return paired

def hook_for_one_class(extracted_edge_list,node,paired):
    #this take a list containing the connections(edge_list) and a node (and paired for the pairs function which is used in this function)
    #it basically creates a hook for the taken node; and it pairs the elements in this hook
    #for example; we have [(1,2),(1,3),(1,4)]; it first hooks and gets 2,3,4 ; after it adds 1 to the front of 2,3,4; we have 1,2,3,4; then it makes pairs (1,2), (2,3), (3,4)
    #after this pairing we have paired relations returned as pairs
    empty_list = []
    for items in extracted_edge_list:
        if items[0] == node:
            empty_list.append(items[1])
    empty_list.insert(0,node)
    pairs(empty_list,paired)
    return paired

def hook_list(tree):
    #this is to hook every elements in the tree and get paired list for each items in the tree
    total_paired_list = []
    empty_ikili = []
    for items in tree:
        a = hook_for_one_class(tree,items[0],empty_ikili)
        for lit_items in a:
            if lit_items not in total_paired_list:
                total_paired_list.append(lit_items)
    for items in total_paired_list: 
        if items[0] == items[1]:
            total_paired_list.remove(items)
    return total_paired_list      

def second_part(hook_list):
    #this is to delete tuples from the edge list, and create a class precedence list
    cpl = []
    while (True):
        a = False
        first_index_list = []
        second_index_list= []
        for i in hook_list:
            first_index_list.append(i[0])
            second_index_list.append(i[1])
        #print("first index list")
        #print(first_index_list)
        #print("second index list")
        #print(second_index_list)
        counter = []
        for elements in first_index_list:
            counter.append((first_index_list.count(elements),second_index_list.count(elements)))
        #print("counter")
        #print(counter)
        deleted_items = []
        if len(counter) >= 1:
            for e in range(len(counter)):
                if counter[e][1] == 0:
                    a = True
                    deleted_items.append(e)
            #print("a")
            #print(a)
            #print("deleted_items")
            #print(deleted_items)
            for elements in sorted(deleted_items):
                if hook_list[elements][0] not in cpl:
                    cpl.append(hook_list[elements][0])
                    if tracing_mode == True: 
                        print("Class Precedence List")
                        print(cpl)
                        print("")
            for index in sorted(deleted_items, reverse=True):
                del hook_list[index]
                if tracing_mode == True:
                    print("Removal from Hooklist - New Hook List:")
                    print(hook_list)
                    print("")
        #hook_list len 1e düşünce sonuncuyu da ekle
        if len(counter) == 0:
            cpl.append("Everything")
        if(a == False):
            break
    #print("cpl")
    #print(cpl)
    if tracing_mode == True:
        print("Completed Class Precedence List")
    return cpl

if problem_choice == 1: 
############################################################################################################################################################################################
############################################################################################################################################################################################
    #CREATING EDGE LIST(TREE CONNECTIONS) FOR THE FIRST PROBLEM 1 (REPRESENTING THE LINKS BETWEEN THE NODES AND CREATING AN EDGE LIST)
    edge_list_problem1 = []
    link_creator("ifstream","istream",edge_list_problem1)
    link_creator("istream","ios",edge_list_problem1)
    link_creator("fstream","iostream",edge_list_problem1)
    link_creator("iostream","istream",edge_list_problem1)
    link_creator("iostream","ostream",edge_list_problem1)
    link_creator("ofstream","ostream",edge_list_problem1)
    link_creator("ostream","ios",edge_list_problem1)
    first_problem_tree = link_creator("ios","Everything",edge_list_problem1)
    if tracing_mode == True:
        print("This is the edge list for the first problem")
        print(first_problem_tree)
        print("")
    #first_problem_tree is the common tree(edge list) for the first problem
############################################################################################################################################################################################
    #This is for the ifstream
    #extracting the tree for ifstream from the common tree which is first_problem_tree
    empty_extracted_ifstream = []
    extractred_ifstream = existing_tree(first_problem_tree,"ifstream",empty_extracted_ifstream)
    if tracing_mode == True:
        print("TRACING STARTED FOR IFSTREAM")
        print("This is the extracted tree for ifstream")
        print(extractred_ifstream)
        print("")
    #creating hook list that contains paired nodes for ifstream
    empty_paired_ifstream = []
    #after obtaining hook list;
    #deleting the elements from the list and adding right elements to the class precedence list using second_part function
    hook_list_ifstream = hook_list(extractred_ifstream)  
    if tracing_mode == True:
        print("This is the hook list for ifstream")
        print(hook_list_ifstream)
        print("")
    if tracing_mode == False: 
        print("Class Precedence List for ifstream")
    print(second_part(hook_list_ifstream))
    print("")
    if tracing_mode == True:
        print("TRACING COMPLETED FOR IFSTREAM")
        print("")
############################################################################################################################################################################################
    #This is for the fstream
    #extracting the tree for fstream from the common tree which is first_problem_tree
    empty_extracted_fstream = []
    extractred_fstream = existing_tree(first_problem_tree,"fstream",empty_extracted_fstream)
    if tracing_mode == True:
        print("TRACING STARTED FOR FSTREAM")
        print("This is the extracted tree for fstream")
        print(extractred_fstream)
        print("")
    #creating hook list that contains paired nodes for fstream
    empty_paired_fstream = []
    #after obtaining hook list;
    #deleting the elements from the list and adding right elements to the class precedence list using second_part function
    hook_list_fstream = hook_list(extractred_fstream)  
    if tracing_mode == True:
        print("This is the hook list for fstream")
        print(hook_list_fstream)
        print("")
    if tracing_mode == False: 
        print("Class Precedence List for fstream")
    print(second_part(hook_list_fstream))
    print("")
    if tracing_mode == True:
        print("TRACING COMPLETED FOR FSTREAM")
        print("")
############################################################################################################################################################################################
    #This is for the ofstream
    #extracting the tree for ofstream from the common tree which is first_problem_tree
    empty_extracted_ofstream = []
    extractred_ofstream = existing_tree(first_problem_tree,"ofstream",empty_extracted_ofstream)
    if tracing_mode == True:
        print("TRACING STARTED FOR OFSTREAM")
        print("This is the extracted tree for ofstream")
        print(extractred_ofstream)
        print("")
    #creating hook list that contains paired nodes for fstream
    empty_paired_ofstream = []
    #after obtaining hook list;
    #deleting the elements from the list and adding right elements to the class precedence list using second_part function
    hook_list_ofstream = hook_list(extractred_ofstream)  
    if tracing_mode == True:
        print("This is the hook list for ofstream")
        print(hook_list_ofstream)
        print("")
    if tracing_mode == False: 
        print("Class Precedence List for ofstream")
    print(second_part(hook_list_ofstream))
    print("")
    if tracing_mode == True:
        print("TRACING COMPLETED FOR OFSTREAM")
        print("")
############################################################################################################################################################################################
############################################################################################################################################################################################





if problem_choice == 2: 
############################################################################################################################################################################################
############################################################################################################################################################################################
    #CREATING EDGE LIST(TREE CONNECTIONS) FOR THE SECOND PROBLEM  (REPRESENTING THE LINKS BETWEEN THE NODES AND CREATING AN EDGE LIST)
    edge_list_problem2 = []
    link_creator("Consultant Manager","Consultant",edge_list_problem2)
    link_creator("Consultant Manager","Manager",edge_list_problem2)
    link_creator("Director","Manager",edge_list_problem2)
    link_creator("Permanent Manager","Manager",edge_list_problem2)
    link_creator("Consultant","Temporary Employee",edge_list_problem2)
    link_creator("Temporary Employee","Employee",edge_list_problem2)
    link_creator("Manager","Employee",edge_list_problem2)
    link_creator("Permanent Manager","Permanent Employee",edge_list_problem2)
    link_creator("Permanent Employee","Employee",edge_list_problem2)
    second_problem_tree = link_creator("Employee","Everything",edge_list_problem2)
    #second_problem_tree is the common tree for the second problem
    if tracing_mode == True:
        print("This is the edge list for the second problem")
        print(second_problem_tree)
        print("")
############################################################################################################################################################################################
    #This is for the Consultant Manager(cm)
    #extracting the tree for Consultant Manager from the common tree which is second_problem_tree
    empty_extracted_cm = []
    extracted_cm = existing_tree(second_problem_tree,"Consultant Manager",empty_extracted_cm)
    if tracing_mode == True:
        print("TRACING STARTED FOR CONSULTANT MANAGER")
        print("This is the extracted tree for Consultant Manager")
        print(extracted_cm)
        print("")
    #creating hook list that contains paired nodes for Consultant Manager
    empty_paired_cm = []
    hook_list_cm = hook_list(extracted_cm)
    if tracing_mode == True:
        print("This is the hook list for Consultant Manager")
        print(hook_list_cm)
        print("")
    if tracing_mode == False: 
        print("Class Precedence List for Consultant Manager")
    #after obtaining hook list;
    #deleting the elements from the list and adding right elements to the class precedence list using second_part function
    print(second_part(hook_list_cm))
    print("")
    if tracing_mode == True:
        print("TRACING COMPLETED FOR CONSULTANT MANAGER")
        print("")
############################################################################################################################################################################################
    #This is for the Director(d)
    #extracting the tree for Director from the common tree which is second_problem_tree
    empty_extracted_d = []
    extracted_d = existing_tree(second_problem_tree,"Director",empty_extracted_d)
    if tracing_mode == True:
        print("TRACING STARTED FOR DIRECTOR")
        print("This is the extracted tree for Director")
        print(extracted_d)
        print("")
    #creating hook list that contains paired nodes for Director
    empty_paired_d = []
    hook_list_d = hook_list(extracted_d)
    if tracing_mode == True:
        print("This is the hook list for Director")
        print(hook_list_d)
        print("")
    if tracing_mode == False: 
        print("Class Precedence List for Director")
    #after obtaining hook list;
    #deleting the elements from the list and adding right elements to the class precedence list using second_part function
    print(second_part(hook_list_d))
    print("")
    if tracing_mode == True:
        print("TRACING COMPLETED FOR DIRECTOR")
        print("")
############################################################################################################################################################################################
    #This is for the Permanent Manager(pm)
    #extracting the tree for Permanent Manager from the common tree which is second_problem_tree
    empty_extracted_pm = []
    extracted_pm = existing_tree(second_problem_tree,"Permanent Manager",empty_extracted_pm)
    if tracing_mode == True:
        print("TRACING STARTED FOR PERMANENT MANAGER")
        print("This is the extracted tree for Permanent Manager")
        print(extracted_pm)
        print("")
    #creating hook list that contains paired nodes for Permanent Manager
    empty_paired_pm = []
    hook_list_pm = hook_list(extracted_pm)
    if tracing_mode == True:
        print("This is the hook list for Permanent Manager")
        print(hook_list_pm)
        print("")
    if tracing_mode == False: 
        print("Class Precedence List for Permanent Manager")
    #after obtaining hook list;
    #deleting the elements from the list and adding right elements to the class precedence list using second_part function
    print(second_part(hook_list_pm))
    print("")
    if tracing_mode == True:
        print("TRACING COMPLETED FOR PERMANENT MANAGER")
        print("")
############################################################################################################################################################################################
############################################################################################################################################################################################
    





if problem_choice == 3: 
############################################################################################################################################################################################
############################################################################################################################################################################################
    #CREATING EDGE LIST(TREE CONNECTIONS) FOR THE THIRD PROBLEM  (REPRESENTING THE LINKS BETWEEN THE NODES AND CREATING AN EDGE LIST)
    edge_list_problem3 = []
    link_creator("Jacque","Weightlifters",edge_list_problem3)
    link_creator("Jacque","Shotputters",edge_list_problem3)
    link_creator("Jacque","Athletes",edge_list_problem3)
    link_creator("Weightlifters","Athletes",edge_list_problem3)
    link_creator("Weightlifters","Endomorpha",edge_list_problem3)
    link_creator("Shotputter","Athletes",edge_list_problem3)
    link_creator("Shotputter","Endomorpha",edge_list_problem3)
    link_creator("Athletes","Dwarfs",edge_list_problem3)
    link_creator("Endomorpha","Dwarfs",edge_list_problem3)
    link_creator("Crazy","Professors",edge_list_problem3)
    link_creator("Crazy","Hackers",edge_list_problem3)
    link_creator("Professors","Eccentrics",edge_list_problem3)
    link_creator("Professors","Teachers",edge_list_problem3)
    link_creator("Hackers","Eccentrics",edge_list_problem3)
    link_creator("Hackers","Programmers",edge_list_problem3)
    link_creator("Eccentrics","Dwarfs",edge_list_problem3)
    link_creator("Teachers","Dwarfs",edge_list_problem3)
    link_creator("Programmers","Dwarfs",edge_list_problem3)
    third_problem_tree = link_creator("Dwarfs","Everything",edge_list_problem3)
    #third_problem_tree is the common tree for the third problem
    if tracing_mode == True:
        print("This is the edge list for the third problem")
        print(third_problem_tree)
        print("")
############################################################################################################################################################################################
    #This is for the Crazy
    #extracting the tree for Crazy from the common tree which is third_problem_tree
    empty_extracted_crazy = []
    extracted_crazy = existing_tree(third_problem_tree,"Crazy",empty_extracted_crazy)
    if tracing_mode == True:
        print("TRACING STARTED FOR CRAZY")
        print("This is the extracted tree for Crazy")
        print(extracted_crazy)
        print("")
    #creating hook list that contains paired nodes for Crazy
    empty_paired_crazy = []
    hook_list_crazy = hook_list(extracted_crazy)
    if tracing_mode == True:
        print("This is the hook list for Crazy")
        print(hook_list_crazy)
        print("")
    if tracing_mode == False: 
        print("Class Precedence List for Crazy")
    #after obtaining hook list;
    #deleting the elements from the list and adding right elements to the class precedence list using second_part function
    print(second_part(hook_list_crazy))
    print("")
    if tracing_mode == True:
        print("TRACING COMPLETED FOR CRAZY")
        print("")
############################################################################################################################################################################################
    #This is for the Jacque
    #extracting the tree for Jacque from the common tree which is third_problem_tree
    empty_extracted_jacque = []
    extracted_jacque = existing_tree(third_problem_tree,"Jacque",empty_extracted_jacque)
    if tracing_mode == True:
        print("TRACING STARTED FOR JACQUE")
        print("This is the extracted tree for Jacque")
        print(extracted_jacque)
        print("")
    #creating hook list that contains paired nodes for Crazy
    empty_paired_jacque = []
    hook_list_jacque = hook_list(extracted_jacque)
    if tracing_mode == True:
        print("This is the hook list for Jacque")
        print(hook_list_jacque)
        print("")
    if tracing_mode == False: 
        print("Class Precedence List for Jacque")
    #after obtaining hook list;
    #deleting the elements from the list and adding right elements to the class precedence list using second_part function
    print(second_part(hook_list_jacque))
    print("")
    if tracing_mode == True:
        print("TRACING COMPLETED FOR JACQUE")
        print("")
############################################################################################################################################################################################
############################################################################################################################################################################################
    
        


        
