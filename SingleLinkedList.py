class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = Node(None)  # 哨兵节点，指向链表的第一个节点

    def is_empty(self):
        # 判断链表是否为空，如果head的next是None则为空
        return self.head.next is None

    def length(self):
        # 获取链表的长度
        current = self.head.next
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def find(self, data):
        # 查找指定元素的位置，返回索引，如果不存在则返回-1
        current = self.head.next
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def CreateLink(self):  # 修正方法名，Python中方法名应该是驼峰式命名
        cnode = self.head
        elem = input("Enter element ('#' to stop): ")
        while elem != '#':
            node = Node(elem)
            cnode.next = node
            cnode = cnode.next
            elem = input("Enter element ('#' to stop): ")

    def InsertTail(self, elem):  # 修正方法名，避免重复定义
        if elem == '#':
            return
        nnode = Node(elem)
        cnode = self.head
        while cnode.next:
            cnode = cnode.next
        cnode.next = nnode

def test_link_list():
    # 创建一个空的链表
    ll = LinkList()

    # 测试链表是否为空
    print("Is the list empty?", ll.is_empty())  # 应该输出 True

    # 创建链表并测试长度
    print("Creating the list...")
    ll.CreateLink()  # 假设用户输入 1, 2, 3, '#' 来创建链表
    print("Length of the list:", ll.length())  # 应该输出 3

    # 测试插入元素到链表尾部
    print("Inserting '4' to the tail of the list.")
    ll.InsertTail('4')
    print("Length of the list after insertion:", ll.length())  # 应该输出 4

    # 测试查找元素位置
    print("Finding element '2' in the list:", ll.find('2'))  # 应该输出 1
    print("Finding element '5' in the list:", ll.find('5'))  # 应该输出 -1 (不存在)

    # 测试链表是否为空
    print("Is the list empty after insertion?", ll.is_empty())  # 应该输出 False

# 调用测试函数
test_link_list()