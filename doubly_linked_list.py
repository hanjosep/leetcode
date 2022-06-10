class Node:
    def __init__(self, data= None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return
        itr = self.head
        dllstr = ' HEAD IS HERE '
        while itr:
            dllstr += str(itr.data) + ' <--> '
            itr = itr.next
    
        print(dllstr)
    
    def print_backward(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return
        itr = self.head
        dllstr = ' HEAD IS HERE'
        while itr:
            dllstr = ' <--> ' + str(itr.data) + dllstr
            itr = itr.next
    
        print(dllstr)
    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        # self.head = node 
        # self.prev = node 
        if self.head is None:
            self.head = Node(data, None)
            return 
        itr = self.head 
        while itr.prev:
            itr  = itr.prev
        itr.prev = Node(data, node, None)
        self.head = node 
    def insert_at_end(self,data):
        node = Node(data, self.head)
        if self.head is None:
            self.head = Node(data, None)
            return
        itr= self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None,node)
        # self.head = node
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    def get_head(self):
        print(self.head.data, self.head.data)
    def get_len(self):
        count = 0 
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count
        # pass
    def remove_at(self,i):
        if i< 0 or i>= self.get_len():
            raise Exception('Invalid index when removing')
        if i == 0:
            self.head = self.head.next 
            return 
        count = 0
        itr = self.head
        while itr:
            if count == i-1:
                itr.next = itr.next.next
            itr = itr.next 

    def insert_at(self, i, data):
        if i< 0 or i> self.get_len():
            raise Exception('Invalid index when inserting')
        if i == 0:
            self.insert_at_beginning(data)
        count = 0
        itr= self.head
        while itr:
            if count == i -1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node 
                itr.next = node 
                break
            itr = itr.next
            count += 1 

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr.prev)
                itr.next = node
                return
            itr = itr.next 
        raise Exception('Data does not exist in Doubly Linked List while inserting')
        
    def remove_by_value(self, data):
        itr = self.head 
        while itr:
            if itr.data == data:
                itr.data = itr.next.data
                itr.next = itr.next.next
                return
            itr = itr.next 
        raise Exception("Data does not exist in Doubly Linked List while removing")
if __name__ ==  '__main__':
    dll = DoublyLinkedList()
    dll.insert_at_beginning('one')
    dll.insert_at_end('two')
    for i in range(4):
        dll.insert_at_beginning(i * -1)
        dll.insert_at_end(i)
    # dll.insert_values(['a','b','c'])
    dll.insert_after_value(1,1.5)
    dll.remove_by_value('two')
    dll.print_forward()
    dll.print_backward()
    print(dll.get_len())
    dll.get_head()
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()