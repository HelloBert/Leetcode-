
class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingLeLinkList(object):
    """单向循环链表"""
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        # 定义游标来遍历链表
        cur = self.__head
        # 定义长度
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next is not self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        print(cur.elem)

    def add(self, item):
        """链表头部添加元素(头插法)"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            # 退出循环，cur指向尾结点
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        node.next = node
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            count = 0
            node = Node(item)
            pre = self.__head
            while count <= (pos-1):
                count += 1
                pre = pre.next
                # 当循环推出后，pre指向pos-1的位置
                node.next = pre.next
                pre.next = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next is not self.__head:
            if cur.elem == item:
                if cur == self.__head:
                    # 头结点
                    # 先找尾结点
                    rear = self.__head
                    while rear.next is not self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间结点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾结点
        if cur.elem == item:
            if cur is self.__head:
                # 链表只有一个结点
                self.__head = None
            else:
                pre.next = cur.next

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next is not self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem is item:
            return True
        return False


if __name__ == "__main__":
    ll = SingLeLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.travel()
    ll.insert(10, 200)
    ll.travel()
