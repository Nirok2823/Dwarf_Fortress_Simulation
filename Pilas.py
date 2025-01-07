# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 10:29:06 2024

@author: Dell
"""

class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val
        
class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.items = []
        
    def push(self, val):
        newNode = Node(val)
        
        if(self.size == 0):
            self.head = newNode;
            self.tail = newNode
            self.size += 1;
            return
        
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail= newNode
        self.size += 1
        
    def pop(self):
        
        if(self.size == 0):
            raise Exception("is empty")
            return
        
        auxPop = self.top()
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return auxPop
        
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
        
        return auxPop
        
        
    def top(self):
        return self.tail.val
    
    def size(self): 
        return self.size
    
    def empty(self):
        return self.size == 0
    
    def printStack(self):
        curr = self.tail
        
        while curr:
            print(curr.val, end = "\n")
            curr = curr.prev
            
        print();
        

        
    
    
    
        
        
        