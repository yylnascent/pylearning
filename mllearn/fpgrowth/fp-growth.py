"""
FP-Growth algorithem. FP-->Frequent Pattern
"""

class FPNode(object):
    """
        FPTree Node
    """
    def __init__(self, node_name, parent_node, occur_cn=1):
        self.node_name = node_name
        self.occur_cn = occur_cn
        self.parent_node = parent_node
        self.link = None
        self.children = {}
    
    def inc(self):
        self.occur_cn += 1

    def disp(self, ind=1):
        print(' '*ind, self.node_name, ' ', self.occur_cn)
        for _, child in self.children.items():
            child.disp(ind+1)

    def append_child(self, child):
        if child.node_name in self.children:
            self.children[child.node_name].inc()
        else:
            self.children[child.node_name] = child

class FPRootNode(FPNode):
    """
        FPTree Root Node
    """
    def __init__(self):
        super(FPRootNode, self).__init__('NULL', None, -1)

    def add(self, transaction):
        parent = self
        for node_name in transaction:
            child = FPNode(node_name, parent)
            parent.append_child(child)
            parent = child

class FPTree(object):
    """
    FP Tree
    """
    def __init__(self, transactions, mini_support):
        self.__root = FPRootNode()
        self.__headers = []
        self.__transactions = transactions
        self.__mini_support = mini_support

    def build(self):
        items = {}
        for transaction in self.__transactions:
            for item in transaction:
                if item in items:
                    items[item] += 1
                else:
                    items[item] = 1

        items = dict((item, support) for item, support in items.items() if support >= self.__mini_support)

        self.__header =  sorted(items, key=items.get, reverse=True)

        def clean_transaction(transaction):
            transaction = filter(lambda v: v in items, transaction)
            transaction.sort(key=lambda v: items[v], reverse=True)

            return transaction

        for transaction in map(clean_transaction, self.__transactions):
            self.__root.add(transaction)

    def disp(self):
        self.__root.disp()
    
if __name__ == "__main__":
    transactions = []
    with open('data/test.txt', 'r') as fp:
        for line in fp.readlines():
            transactions.append(line[:-1].split(' '))

    fptree = FPTree(transactions, round(len(transactions) * 0.3))
    fptree.build()
    fptree.disp()

