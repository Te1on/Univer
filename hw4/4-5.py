class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None

    def __repr__(self):
        printval = self.headval
        res = ""
        while printval is not None:
            res += str(printval.dataval)
            printval = printval.nextval
            if printval is not None:
                res += ' -> '
        return res


if __name__ == "__main__":
    ll = LinkedList()
    ll.headval = Node(1)
    e2 = Node(2)
    e3 = Node(3)

    ll.headval.nextval = e2
    e2.nextval = e3
    print(ll)

    ll.headval = Node(4)
    ll.headval.nextval = e2
    print(ll)
