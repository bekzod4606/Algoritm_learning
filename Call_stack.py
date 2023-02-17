# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 17:18:04 2023

@author: bekzo
"""

class Stack:
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, data):
        self.stack.append(data)
        return True
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack.pop()
        
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack[-1]