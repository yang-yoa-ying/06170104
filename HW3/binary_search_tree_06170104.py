#!/usr/bin/env python
# coding: utf-8

# In[1]:


class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def insert(self,root,val):
        if root:
            if root.val >= val:
                if root.left:
                    self.insert(root.left,val)
                else:
                    root = TreeNode(val)
                    return root
            if root.val < val:
                if root.right:
                    self.insert(root.right,val)
                else:
                    root = TreeNode(val)
                    return root
        else:
            root = TreeNode(val)
            return root
    def search(self,root,target):
        if root:
            if root.val == target:
                return root
            elif root.val > target:
                return self.search(root.left,target)
            elif root.val < target:
                return self.search(root.right,target)
        else:
            return None
    
    def gotoleft(self,root):
        if root:
            if root.left != None:
                root = root.left
                return self.gotoleft(root)
            else:
                return root
            
    def gotoright(self,root):
        if root:
            if root.right != None:
                root = root.right
                return self.gotoright(root)
            else:
                return root
            
    def delete(self,root,target):
        if root:
            if self.search(root,target):
                a = self.search(root,target)
                if a.right:
                    if a.right.left:
                        b = self.gotoleft(a.right)
                        a.val = b.val
                        b = None
                        return self.delete(root,target)
                    elif a.right.right:
                        b = self.gotoright(a.right)
                        while a.right:
                            a.val = a.right.val
                            a.right= a.right.right
                        b = None
                        return self.delete(root,target)
                    else:
                        a.val = a.right.val
                        a.right = None
                        return self.delete(root,target)
                elif a.left:
                    if a.left.right:
                        b = self.gotoright(a.left)
                        a.val = b.val
                        b = None
                        return self.delete(root,target)
                    elif a.left.left:
                        b = self.gotoleft(a.left)
                        while a.left:
                            a.val = a.left.val
                            a.left = a.left.left
                        b = None
                        return self.delete(root,target)
                    else:
                        a.val = a.left.val
                        a.left = None
                        return self.delete(root,target)
                
                
                
            else:
                return root
        else:
            return root
    
    
    def modify(self,root,target,new_val):
        if root:
            if self.search(root,target):
                a = self.delete(root,target)
                self.insert(a,new_val)
                return root
            else:
                return root
        else:
            return root
    
    
    def printest(self,root):
        if root:
            print(root.val)

            self.printest(root.left)

            self.printest(root.right)

                

                


# In[2]:


root  = TreeNode(5)
Node1 = TreeNode(3)
Node2 = TreeNode(3)
Node3 = TreeNode(-5)
Node4 = TreeNode(8)
Node5 = TreeNode(7)
Node6 = TreeNode(6)
Node7 = TreeNode(10)
root.left=Node1
root.right=Node4
Node1.left=Node2
Node2.left=Node3
Node4.left=Node5
Node4.right=Node7
Node5.left=Node6
root1 = root
root2 = root
root3 = root
root4 = root
print("insert")
print(Solution().insert(root1,4) ==root1.left.right)
Solution().printest(root1)
print("------------------")
print("delete")
root2 = Solution().delete(root2,3)
print(root2.val == 5 and root2.left.val == -5 and root2.left.left == None and root2.left.right == None)
print(root2.right.right.val == 10 and root2.right.left.val == 7 and root2.right.left.left.val == 6)
print(root2.right.right.right == None and root2.right.right.left ==None and root2.right.left.right == None)
print(root2.right.left.left.left == None and root2.right.left.left.right == None and root2.right.val ==8)
print("------------------")
print("search")
print(Solution().search(root3,10) ==root3.right.right)
print("------------------")
print("modify")
print(root4.left.val)
root4 = Solution().modify(root4,7,4)
print(root4.left.val)


# In[3]:


root  = TreeNode(5)
Node1 = TreeNode(3)
Node2 = TreeNode(3)
Node3 = TreeNode(-5)
Node4 = TreeNode(8)
Node5 = TreeNode(7)
Node6 = TreeNode(6)
Node7 = TreeNode(10)
root.left=Node1
root.right=Node4
Node1.left=Node2
Node2.left=Node3
Node4.left=Node5
Node4.right=Node7
Node5.left=Node6
root1 = root
root2 = root
root3 = root
root4 = root


# In[4]:


print("insert")
print(Solution().insert(root1,4) ==root1.left.right)
print("------------------")
print("delete")
root2 = Solution().delete(root2,3)
print(root2.val == 5 and root2.left.val == -5 and root2.left.left == None and root2.left.right == None)
print(root2.right.right.val == 10 and root2.right.left.val == 7 and root2.right.left.left.val == 6)
print(root2.right.right.right == None and root2.right.right.left ==None and root2.right.left.right == None)
print(root2.right.left.left.left == None and root2.right.left.left.right == None and root2.right.val ==8)
print("------------------")
print("search")
print(Solution().search(root3,10) ==root3.right.right)
print("------------------")
print("modify")
print(root4.left.val)
root4 = Solution().modify(root4,7,4)
print(root4.left.val)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




