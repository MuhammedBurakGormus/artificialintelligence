#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Oct 12 16:39:22 2020

@author: muhammedburakgormus
"""

"""SECTION2 - GROUP BIFKE
GROUP MEMBERS:  21602797 - Muhammed Burak Görmüş
	  	21602930 - Abdullah Fırat Uyar
		21501551 - İpeksu Tutsak
		21000292 - Koral Yıldıran
		21802629 - Salih Efe Boyacı """

"""In our program we use BFS, and we choose (a) for the second part of the assignment
(6cannibals,6missionaries,and a boat holding up to 4)"""

"""When you run the code, you will be asked to enter a or b. If you enter a, you will see the solution for 5 cannibals, 
5 missionaries, and a boat holding up to 3. If you enter b, you will see the solution for 6 cannibals, 
6 missionaries, and a boat holding up to 4. The first part of print will show the state spaces from the beginning step by step.
objects for space states have the following attributes:
(#left cannibals, #left missionaries, boat position, #right cannibals, #right missionaries). 
The second print is in the similar format given in the assignment description. It shows the cannibals and missionaries side by side, 
and the cannibals and missionaries sent by boat. For example;  
                                             Left Side:CCCCCCMMMMMM
                                             Right Side:
                                             Send right:CM
After sending,                                              
                                             Left Side:CCCCCMMMMM
                                             Right Side:CM
                                             Send left:M                              
                                             

Our program starts with breadth_first_search(initial_state). This function takes a state which is the root state and it returns the
final(aimed) state if it exists. During this search the children of states are created by childs(state,moves) function. Moves is a list
obtained generate_moves() function. Generate_moves() returns a list of possible set of #cannibals, #missionaries in the boat
according to the boat capacity. After reaching the aimed state, finding_parents returns the path from root to aimed state in a reverse 
order. Last function, print_the_path() prints the solutions steps in a desired format."""


class State():
    
    def __init__(self,left_cannibals,left_missionaries,position,right_cannibals,right_missionaries,boat_capacity):
        """creating an object with attributes of the numbers of cannibals and missionaries at each side
        -- this object also stores the position of the boat and the maximum capacity of the boat """
        
        self.left_cannibals = left_cannibals
        self.left_missionaries = left_missionaries
        self.position = position
        self.right_cannibals = right_cannibals
        self.right_missionaries = right_missionaries
        self.boat_capacity = boat_capacity
        self.parent = None
     
    def __repr__(self):
        #representation of an object(state space)
        
        return '(%s, %s,%s, %s,%s)' % (self.left_cannibals,self.left_missionaries,self.position,self.right_cannibals,self.right_missionaries)
    
    def is_succeed(self):
        """creating a method to check whether we reached the wanted result
        -- wanted result is the state where all cannibals and missionaries are at the right side
        -- i.e. the number of cannibals and missionaries at left side should be zero"""
        
        if self.left_cannibals==0 and self.left_missionaries == 0:
            return True
        else:
            return False
        
    def is_safe(self):
        """checking whether the state is safe, i.e. whether the missionaries are outnumbered by cannibals
        -- it checks for the bothside whether the number of missionaries are bigger than the number of cannibals
        -- note that it is not necessarily true if the number of missionaries are equal to zero """
        
        if (self.right_missionaries == 0 or self.right_missionaries >= self.right_cannibals) \
                    and (self.left_missionaries == 0 or self.left_missionaries >= self.left_cannibals) :
            return True
        else:
            return False
        
    def __eq__(self,other):
        #preventing initiating two objects with same attributes
        return self.left_cannibals == other.left_cannibals and self.left_missionaries == other.left_missionaries \
            and self.position == other.position and self.right_cannibals == other.right_cannibals \
                and self.right_missionaries == other.right_missionaries and self.boat_capacity == other.boat_capacity
    
    def __hash__(self):
        #hashing the objects attributes to create nodes and later check it(to make easy in breadth first search)
        return hash((self.left_cannibals,self.left_missionaries,self.position,self.right_cannibals,self.right_missionaries,self.boat_capacity))
                
def generate_moves(initial_state):
    """this function takes an initial state which contains the information of boat capacity
    then it returns a list which contains possible moves.
    Possible moves mean the #cannibals and #missionaries on the boat.
    For example if the boat capacity is 2;
    the list named moves consists of [(0, 1), (0, 2), (1, 0), (1, 1), (2, 0)].
    For example first element of the list represents 0cannibal and 1 missionary on the boat
    the second element of the list represents 0 cannibal and 2 missionary etc."""
    
    moves = []
    for c in range(initial_state.boat_capacity+1):
        for m in range(initial_state.boat_capacity + 1):
            if m+c <= initial_state.boat_capacity and (m!=0 or c!=0) and ((m!=0 and c <= m) or (m==0 and c >=m)): 
                """the explanation of if condition statements 
                1.the sum of #cannibals and #missionaries cannot be bigger than boat capacity
                2.boat cannot go by itself and 
                3.the #cannibals cannot be bigger than the #missionaries on the boat(it is not necessarily true if #missionaries on the boat is 0)
                -- c represents #cannibals; m represents #missionaries"""
                a = (c,m)
                moves.append(a)
    return moves

def childs(cur_state,moves):
    """this function takes a state, and a possible moves list generated by generate_moves
    and it returns a list consists of the children of this current state"""
    
               
    children = []
    #creating childrens of cur_state trying all the moves and checking whether they are safe
    for i in range(len(moves)):
        #it means that we are trying all possible moves as the for loop runs
        if cur_state.position == "left":
            #creating a new state(new object) trying possible moves, this state is the child of cur_state
            #i.e. extending our nodes and after that we will check whether it is safe
            #new states position should be now 'right'
            new_state = State(cur_state.left_cannibals-moves[i][0] ,cur_state.left_missionaries-moves[i][1], 'right',
                              cur_state.right_cannibals+moves[i][0],cur_state.right_missionaries+moves[i][1],
                              cur_state.boat_capacity)
            #the number of cannibals and missionaries at the left decreases as the boat goes to right
            #the number of cannibals and missionaries ath the right increases
            #NOW IT IS TIME TO CHECK WHETHER IT IS SAFE
            if new_state.is_safe():
                new_state.parent = cur_state #the parent of new state is cur_state which we originated from
                children.append(new_state)
                
            
        if cur_state.position == "right":
            new_state = State(cur_state.left_cannibals+moves[i][0] ,cur_state.left_missionaries+moves[i][1], 'left',
                              cur_state.right_cannibals-moves[i][0],cur_state.right_missionaries-moves[i][1],
                              cur_state.boat_capacity)
            if new_state.is_safe():
                new_state.parent = cur_state
                children.append(new_state)
                
    return children
                
def breadth_first_search(initial_state):
    #it will take an input of the state given by the user 
    #it will return the aimed state(zero cannibals and missionaries at left) if it exists, if it does not it will return None
    
    moves = generate_moves(initial_state) #generating possible moves using the function generate_moves() above
    queue = []  #queue should be a list, not a set bcs sets are to store unordered unique elements 
    explored = set() #set is used to make sure the items are not duplicated
    queue.append(initial_state)
    while len(queue) != 0: #as long as the queue is not empty
        state = queue.pop(0) #taking the first element(node) of the queue to examine it
                             #removing the element from the queue because it is the current node we are gonna examine
        if state.is_succeed():
            return state #if the state is succeed, we will stop searching
        explored.add(state) #adding state to explored set to later check to prevent looping
        children_of_current_node = childs(state,moves) #those children will be added to the back of queue if they are not explored or not already in the queue
        for kids in children_of_current_node:
            if (kids not in queue) or (kids not in explored):
                queue.append(kids)
    return None
    
def finding_parents(final_state):
    #With BFS, we reached the aimed final state. This function will the take end node, and it will return the path from final node to starting node      
    path = []
    path.append(final_state)
    parent = final_state.parent
    while parent:
        path.append(parent)
        parent = parent.parent
    return path
        
def print_the_path(path):
    #it will print all the states in the path returned by finding_parents()
    #we should start from the end of the path because the last item is the root
    print("(#cannibals_left,#missionaries_left,boat_position,#cannibals_right,#missionaries_right)")
    for i in reversed(path):
        print(i)
        
    print("")
    
    for i in range(len(path)-1, -1, -1):
        print("Left Side:" + str(path[i].left_cannibals*'C') + str(path[i].left_missionaries*'M'))
        print("Right Side:" +str(path[i].right_cannibals*'C') + str(path[i].right_missionaries*'M'))
        if(i != 0):
            moveC = path[i].left_cannibals - path[i-1].left_cannibals
            moveM = path[i].left_missionaries - path[i-1].left_missionaries
            if(moveC > 0 or moveM > 0):
                print("Send right:" + str(abs(moveC)*'C') +str(abs(moveM)*'M'))
            else:
                print("Send left:" + str(abs(moveC)*'C') +str(abs(moveM)*'M'))
        print("")
        
        
info = input("a for 5 cannibals, 5 missionaries and a boat holding up to 3\nb for 6 cannibals, 6 missionaries and a boat holding up to 4\nEnter your choice(a or b): ")
#creating the root space state(object)
if info == "a":
    root_state = State(5,5,'left',0,0,3)
    final_state = breadth_first_search(root_state)
    path = finding_parents(final_state)
    print_the_path(path)
elif info == "b":
    root_state = State(6,6,'left',0,0,4)
    final_state = breadth_first_search(root_state)
    path = finding_parents(final_state)
    print_the_path(path)
else:
    print("Please enter a valid info input")