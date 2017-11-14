"""
FP-Growth algorithem. FP-->Frequent Pattern
"""

class FPNode(object):
    """
        FPTree Node
    """
    def __init__(self, node_name, occur_cn, parent_node):
        self.__node_name = node_name
        self.__occur_cn = occur_cn
        self.__parent_node = parent_node
        self.__fpheader_link = None
        self.__children = {}
    
    def inc(self, occur_cn=1):
        self.__occur_cn += occur_cn

    def disp(self, ind=1):
        print(' '*ind, self.__node_name, ' ', self.__occur_cn)
        for _, child in self.__children.items():
            child.disp(ind+1)

    @property
    def name(self):
        return self.__node_name

    def append_child(self, child):
        self.__children[child.name] = child

if __name__ == "__main__":
    root  = FPNode('root', 9, None)
    eye  = FPNode('eye', 3, root)
    phoenix  = FPNode('phoenix', 13, root)

    root.append_child(eye)
    root.append_child(phoenix)

    root.disp()

