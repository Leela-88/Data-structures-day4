class Newnode():
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None

'''inorder traversal of a binary tree '''

def inorder(temp):
    if(not temp):
        return

    inorder(temp.left)
    print(temp.key,end=" ")
    inorder(temp.right)

def insert(temp,key):
    if not temp:
        root=Newnode(key)
        return
    q=[]
    q.append(temp)
    print(type(q))
    print(len(q))
    # do level order travresal untill we find empty space
    while(len(q)):
        print(len(q))
        temp=q[0]
        q.pop(0)

        if (not temp.left):
            temp.left=Newnode(key)
            break
        else:
            q.append(temp.left)
        if (not temp.right):
            temp.right=Newnode(key)
            break
        else:
            q.append(temp.right)

root=Newnode(10)
root.left=Newnode(11)
root.left.left=Newnode(7)
root.right=Newnode(9)
root.right.left=Newnode(15)
root.right.right=Newnode(8)

print("inorder traversal before insertion",end=" ")
inorder(root)
key=12
insert(root,key)
print()
print("inorder traversal after insertion",end=" ")
inorder(root)





    
