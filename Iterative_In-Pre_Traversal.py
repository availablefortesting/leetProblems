stack = []
preorder, inorder = [],[]

while stack or root:
    while root:
        preorder.append(root.val)
        
        stack.append(root)
        root = root.left
        
    root = stack.pop()
    inorder.append(root.val)
    
    root = root.right
    
print(preorder)
print(inorder)
