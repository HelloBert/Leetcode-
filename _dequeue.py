class Dqueue(object):
    """双端队列"""
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """往队列添加一个itme元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """往队列添加一个itme元素"""
        self.__list.append(item)

    def pod_front(self):
        """删除队列头部一个队列元素"""
        return self.__list.pop(0)

    def pod_rear(self):
        """删除队列头部一个队列元素"""
        return self.__list.pop()

    def is_empty(self):
        """判断队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)
