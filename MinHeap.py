# -*- coding: utf-8 -*-
"""
Created on Mon May 25 09:21:54 2020

@author: HP
"""

class MinHeap:
    #HeapObject class that stores that wraps the key and value.
    class HeapObject:
        def __init__(self,key,value):
            self.key=key
            self.value=value
        
    def __init__(self):
        self.__array=[]#initialising the heap array.
        
    #performing add Operation.
    def add(self,key,value=None):
        heapObject=self.HeapObject(key,value)
        self.__array.append(heapObject)
        self.__addOperation()
    
    #Performing Add Operation.
    def __addOperation(self):
        currentPos=len(self.__array)-1
        while(currentPos!=0):
            parentPos=self.__getParentPos(currentPos)
            if(not self.__check(currentPos,parentPos)):
                break;
            
            self.__array[currentPos],self.__array[parentPos]=self.__array[parentPos],self.__array[currentPos]
            currentPos=parentPos
        
    
            
           
            
    #This Method returns the parentPos of a childPosition.    
    def __getParentPos(self,childPos):
        if(childPos%2==0):
            return childPos//2-1
        return childPos//2
    
    #Mwthod Checks whether parentObj is Greater than child object.
    def __check(self,childPos,parentPos):
        childObj=self.__array[childPos]
        parentObj=self.__array[parentPos]
        if(childObj.key<parentObj.key):
            return True
        return False
    
    #Method that returns the top object as a tuple and removes it.
    def poll(self):
        if(len(self.__array)==0):
            raise Exception("RunTime Exception:PriorityQueue is Empty")
        
        heapObjectTop=self.__array[0]
        self.__array[0]=self.__array[len(self.__array)-1]
        self.__array.pop()
        if(len(self)>0):
            self.__removeOperation()
            
        if(heapObjectTop.value==None):
            return heapObjectTop.key
        return heapObjectTop.value
    
    #Method that returns the top object as a tuple
    def peek(self):
        if(len(self.__array)==0):
            raise Exception("RunTime Exception:PriorityQueue is Empty")
        heapObject=self.__array[0]
        if(heapObject.value==None):
            return heapObject.key
        return heapObject.value
    
    #Method that performs the remove operation of a heap.
    def __removeOperation(self):
        #print("Inside remove operation")
        currentPos=0
        children=self.__getChildren(currentPos)
        while(len(children)>0):
            #print("Inside while loop")
            minPos=self.__getMin(children)
            if(not self.__check(minPos,currentPos)):
                break
            self.__array[currentPos],self.__array[minPos]=self.__array[minPos],self.__array[currentPos]
            currentPos=minPos
            children=self.__getChildren(currentPos)
            
    #Method that returns the children of a parentPos
    def __getChildren(self,parentPos):
        count=self.__numberOfChildren(parentPos)
        if(count==2):
            return [2*parentPos+1,2*parentPos+2]
        if(count==1):
            return [2*parentPos+1]
        return []
    
    #Method that returns the number of children.
    def __numberOfChildren(self,parentPos):
        left=2*parentPos+1
        right=2*parentPos+2
        count=0
        if(left<len(self.__array)):
            count+=1
            if(right<len(self.__array)):
                count+=1
        return count
    #Method that returns the minimum of the children.
    def __getMin(self,children):
        if(len(children)==2):
            leftObj=self.__array[children[0]]
            rightObj=self.__array[children[1]]
            if(leftObj.key>rightObj.key):
                return children[1]
        return children[0]
    
    #Method to return the length of the priority queue
    def __len__(self):
        return len(self.__array);
    
    #Check whether the method is empty or not and returns a boolean based on that.
    def isEmpty(self):
        if(len(self.__array)==0):
            return True
        return False
    
        
        
        