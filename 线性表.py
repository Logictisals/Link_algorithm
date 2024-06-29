class SequentialList:
    def __init__(self):
        self._data = []

    def destroy(self):
        del self._data
        self._data = []

    def reset(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def length(self):
        return len(self._data)

    def get_element(self, index):
        if 0 <= index < len(self._data):
            return self._data[index]
        else:
            raise IndexError("Index out of range")

    def insert(self, index, element):
        if index < 0 or index > len(self._data):
            raise IndexError("Index out of range")
        self._data.insert(index, element)

    def find(self, element):
        try:
            self._data.index(element)
            return True
        except ValueError:
            return False

    def remove_value(self, element):
        try:
            self._data.remove(element)
        except ValueError:
            print("Element not found")

    def remove_at(self, index):
        if 0 <= index < len(self._data):
            return self._data.pop(index)
        else:
            raise IndexError("Index out of range")

    def traverse(self):
        for element in self._data:
            yield element

# 使用示例
seq_list = SequentialList()

# 构造初始表
seq_list._data = [1, 2, 3, 4, 5]

# 插入元素
seq_list.insert(2, 10)  # 插入10到索引2的位置

# 查找元素
print(seq_list.find(10))  # 输出: True

# 删除元素
seq_list.remove_value(3)  # 删除值为3的元素

# 删除指定位置的元素
print(seq_list.remove_at(1))  # 输出: 10

# 遍历线性表
for element in seq_list.traverse():
    print(element, end=' ')  # 输出: 1 10 4 5

# 判断线性表是否为空
print(seq_list.is_empty())  # 输出: False

# 获取线性表的长度
print(seq_list.length())  # 输出: 4

# 访问线性表中的某个元素
print(seq_list.get_element(0))  # 输出: 1

# 销毁线性表
seq_list.destroy()  # 销毁线性表后，线性表为空
print(seq_list.is_empty())  # 输出: True