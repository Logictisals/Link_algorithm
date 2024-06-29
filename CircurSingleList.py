class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """在链表尾部添加新节点"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head  # 使链表循环
        else:
            last_node = self.head
            while last_node.next != self.head:
                last_node = last_node.next
            last_node.next = new_node
            new_node.next = self.head

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

    def insert_after(self, prev_node, data):
        """在指定节点后插入新节点"""
        if not prev_node:
            print("指定节点不存在")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete(self, data):
        """删除链表中值为data的节点"""
        if not self.head:
            return
        current_node = self.head
        while True:
            if current_node.next.data == data:
                break
            current_node = current_node.next
            if current_node == self.head:
                return  # 数据未找到

        if current_node.next == self.head:
            self.head = None
        else:
            current_node.next = current_node.next.next

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
circular_list = CircularLinkedList()
circular_list.append(1)
circular_list.append(2)
circular_list.append(3)
circular_list.display()  # 输出: 1 2 3

circular_list.insert_after(circular_list.find(2), 4)
circular_list.display()  # 输出: 1 2 4 3

circular_list.delete(3)
circular_list.display()  # 输出: 1 2 4

circular_list.delete(1)
circular_list.display()  # 输出: 2 4