
class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingLeLinkList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        # 定义游标来遍历链表
        cur = self.__head
        # 定义长度
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next

    def add(self, item):
        """链表头部添加元素(头插法)"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
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
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    ll = SingLeLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())



    ll.append(2)

    ll.insert(2, 30)
    ll.insert(10, 200)
    ll.remove(200)
    ll.insert(-1, 20)
    #ll.add(8)
    ll.append(3)
    ll.travel()
