class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """在链表尾部添加新节点"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.prev = self.head
            self.head.next = self.head  # 使链表循环
        else:
            last_node = self.head
            while last_node.next != self.head:
                last_node = last_node.next
            last_node.next = new_node
            new_node.prev = last_node
            new_node.next = self.head
            self.head.prev = new_node

    def display(self):
        """打印链表中的所有元素"""
        current_node = self.head
        if current_node is None:
            print("链表为空")
            return
        while True:
            print(current_node.data, end=" ")
            current_node = current_node.next
            if current_node == self.head:
                break
        print()

    def insert_after(self, data, new_data):
        """在指定数据后插入新节点"""
        current_node = self.head
        while True:
            if current_node.data == data:
                break
            current_node = current_node.next
            if current_node == self.head:
                return  # 数据未找到

        new_node = Node(new_data)
        new_node.next = current_node.next
        new_node.prev = current_node
        current_node.next = new_node
        if new_node.next:
            new_node.next.prev = new_node

    def delete(self, data):
        """删除链表中值为data的节点"""
        current_node = self.head
        while True:
            if current_node.data == data:
                break
            current_node = current_node.next
            if current_node == self.head:
                return  # 数据未找到

        if current_node == self.head:
            self.head = current_node.next
            self.head.prev = None
        else:
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev

    def find(self, data):
        """查找链表中第一个值为data的节点"""
        current_node = self.head
        if current_node is None:
            return None
        while True:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
            if current_node == self.head:
                return None  # 数据未找到

# 使用示例
circular_doubly_list = CircularDoublyLinkedList()
circular_doubly_list.append(1)
circular_doubly_list.append(2)
circular_doubly_list.append(3)
circular_doubly_list.display()  # 输出: 1 2 3

circular_doubly_list.insert_after(2, 4)
circular_doubly_list.display()  # 输出: 1 2 4 3

circular_doubly_list.delete(3)
circular_doubly_list.display()  # 输出: 1 2 4

circular_doubly_list.delete(1)
circular_doubly_list.display()  # 输出: 2 4