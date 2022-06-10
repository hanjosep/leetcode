from ast import iter_child_nodes
from tkinter import W


class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node 
    
    def prt(self):
        if self.head is None:
            print('Linked list is empty')
            return
        itr = self.head
        llstr = ''

        while itr:

            llstr += str(itr.data) + '-->'
            itr = itr.next 

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next: # while there exists an itr next, keep going to the end.
            itr = itr.next

        itr.next = Node(data, None)
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def get_len(self):
        count = 0 
        itr=  self.head
        while itr:
            count +=1
            itr = itr.next
        return count 
    def remove_at(self, i):
        if i < 0 or i >= self.get_len():
            raise Exception("Invalid index when removing")
        if i == 0:
            self.head = self.head.next
            return 
        count = 0
        itr = self.head 
        while itr: 
            if count == i - 1:
                itr.next = itr.next.next
            itr = itr.next 
            count +=1

    def insert_at(self, i, data):
        if i< 0 or i >= self.get_len():
            raise Exception("Invalid index when inserting")

        if i == 0:
            self.insert_at_beginning(data)
            return 

        count = 0 
        itr = self.head
        while itr: 
            if count == i - 1:
                node = Node(data, itr.next) # creates new Node with the desired data, connects the rest to the next 
                itr.next = node 
                break
            itr = itr.next 
            count += 1
    # Exercises:
    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                #create Node, where data = data_to_insert and next = tail of current itr.data
                node = Node(data_to_insert,itr.next) 
                itr.next = node 
                return 
            itr = itr.next 
        raise Exception('Data does not exist in Linked List while inserting')
        

    def remove_by_value(self, data):
        itr = self.head
        while itr: 
            if itr.data == data: 
                # set current data and next to the next data and next 
                itr.data = itr.next.data
                itr.next = itr.next.next 
                return  
            itr = itr.next 
        raise Exception('Data does not exist in Linked List while removing')
if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(89)
    # ll.insert_at_end(29)
    ll.insert_values(['one','two', 'three'])
    ll.insert_at(2, 'pi')
    ll.insert_after_value('one','3/2')
    ll.remove_by_value('3/2')
    ll.insert_values(range(4))
    ll.prt()