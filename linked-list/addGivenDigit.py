""" Add the given digit to a number stored in a linked list (Medium)
https://www.geeksforgeeks.org/add-the-given-digit-to-a-number-stored-in-a-linked-list/

Given a linked list which represents an integer number where every node is a digit if the represented integer. 
The task is to add a given digit N to the represented integer.

Input: 9 -> 9 -> 3 -> NULL, N = 7
Output:
9 -> 9 -> 3 -> NULL
1 -> 0 -> 0 -> 0 -> NULL

Input: 2 -> 9 -> 9 -> NULL, N = 5
Output:
2 -> 9 -> 9 -> NULL
3 -> 0 -> 4 -> NULL """

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value: int):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAfter(self, value: int):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return new_node

        previous_node, current_node = self.head, self.head.next
        
        while current_node is not None:
            previous_node = current_node
            current_node = current_node.next
        
        previous_node.next = new_node
        new_node.next = current_node

        return self.head
       
    
    def printList(self):
        ptr = self.head
        while ptr:
            print(ptr.val, end="->")
            ptr = ptr.next
        print("NULL")

    def addDigit(self, N: int):
        # To keep track of the last node
        # whose value is less than 9
        lastNode = None
        curr = self.head

        while curr.next is not None:
            # If found a node with value
            # less than 9
            if curr.val < 9:
                lastNode = curr
            
            # Otherwise keep traversing
            # the list still end
            curr = curr.next

            # Add the given digit to the last node
            curr.val = curr.val + N

            # In case of overflow in the last node
            if curr.val > 9:
                curr.val = curr.val % 10

                # If the list is of the 
                # form 9 -> 9 -> 9 -> ...
                if lastNode is None:
                    # Insert a node at the beginnig as 
                    # there would be overflow in the 
                    # head in this case 
                    self.insert(1)

                    # Adjust the lastNode pointer to 
                    # propagate the carry effect to 
                    # all the nodes of the list
                    lastNode = self.head.next

                # Forward propagate carry effect
                while lastNode != curr:
                    lastNode.val = (lastNode.val + 1) % 10
                    lastNode = lastNode.next


if __name__ == "__main__":
    # Creating the Linked List
    l1 = LinkedList()

    # Adding elements to the Linked List
    l1.insert(3)
    l1.insert(9)
    l1.insert(9)

    # Printing the original list
    l1.printList()

    # Adding the digit
    l1.addDigit(7)

    # Printing the modified list
    l1.printList()

