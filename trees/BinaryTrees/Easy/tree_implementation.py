
# Implementing Tree Data Structure


class TreeNode :
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix+self.data)
        if self.children :
            for child in self.children:
                child.print_tree()
                
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
        
def build_tree():
    root = TreeNode("A")
    
    B = TreeNode("B")
    B.add_child(TreeNode("E"))
    B.add_child(TreeNode("F"))
    B.add_child(TreeNode("F"))
    
    C = TreeNode("C")
    C.add_child(TreeNode("H"))
    C.add_child(TreeNode("I"))
    C.add_child(TreeNode("J"))
    
    D = TreeNode("D")
    D.add_child(TreeNode("K"))
    D.add_child(TreeNode("L"))
    D.add_child(TreeNode("M"))
    
    root.add_child(B)
    root.add_child(C)
    root.add_child(D)
    
    root.print_tree()
    
if __name__ == '__main__' :
    build_tree()
    