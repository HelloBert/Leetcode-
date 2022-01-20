class Queue(object):
    def __init__(self):
        self.__list = []
    """队列"""
    def enqueue(self, item):
        """往队列添加一个itme元素"""
        self.__list.append(item)

    def dequeue(self):
        """删除一个队列元素"""
        return self.__list.pop(0)

    def is_empty(self):
        """判断队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == "__main__":
    que = Queue()
    que.enqueue(8)
    que.enqueue(6)
    que.enqueue(6)
    print(que.dequeue())
    print(que.dequeue())
    print(que.is_empty())
    print(que.size())
