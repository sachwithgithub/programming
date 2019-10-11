class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add_left(self,left):
        self.left = left
    def add_right(self,right):
        self.right = right

a = Tree("a")
b = Tree("b")
c = Tree("c")
d = Tree("d")
e = Tree("e")
f = Tree("f")
g = Tree("g")
h = Tree("h")
i = Tree("i")
j = Tree("j")

a.add_left(b)
a.add_right(c)
b.add_left(d)
b.add_right(e)
d.add_right(g)
g.add_left(h)
e.add_left(f)
c.add_left(i)
c.add_right(j)

from pythonds import Queue

q = Queue()
q.enqueue(a)

while not q.isEmpty():
    cur = q.dequeue()
    print(cur.data)
    if cur.left:
        q.enqueue(cur.left)
    if cur.right:
        q.enqueue(cur.right)