class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None


    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end='__')
            current = current.next
        print('Final')

    def delete(self,key):
        current = self.head

        if not current:
            print('Spisok pust!')
            return

        if current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            print(f'Элемент {key} не нашел')
            return

        prev.next = current.next
        current = None

  #реализация обратного отсчета
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev



Tinker = LinkedList()
Tinker.append(1)
Tinker.append(2)
Tinker.append(3)
Tinker.append('aga')

print('ves spisok takov:')
Tinker.display()

Tinker.delete(4)

Tinker.reverse()
Tinker.display()