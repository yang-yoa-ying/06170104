#!/usr/bin/env python
# coding: utf-8

# In[1]:


class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None  
class MyHashSet:
    def __init__(self,capacity = 5):
        self.capacity = capacity
        self.data = [None]*capacity
    
    def add(self,key):
        from Crypto.Hash import MD5
        h  = MD5.new()
        h.update(key.encode("utf-8"))
        changeval = int(h.hexdigest(),16)
        num = changeval % self.capacity
        newnode = ListNode(changeval)
        if self.data[num] == None:
            self.data[num] = newnode
            return 
        node = self.data[num]
        while node.next != None:
            node = node.next
        node.next = ListNode(changeval)
        
        return 
    
    
    def contains(self,key):
        from Crypto.Hash import MD5
        h  = MD5.new()
        h.update(key.encode("utf-8"))
        changeval = int(h.hexdigest(),16)
        num = changeval % self.capacity
        node = self.data[num]
        if self.data[num] == None:
            return False
        else:
            node = self.data[num]
            while node != None:
                if node.val == changeval:
                    return True
                else:
                    node = node.next
            return  False

        
    def findway(self,key):
        from Crypto.Hash import MD5
        h  = MD5.new()
        h.update(key.encode("utf-8"))
        changeval = int(h.hexdigest(),16)
        num = changeval % self.capacity
        node = self.data[num]
        if self.data[num] == None:
            return 
        else:
            node = self.data[num]
            while node != None:
                if node.val == changeval:
                    return node
                else:
                    node = node.next
            return         
        
    
    
    def delete(self,key):
        from Crypto.Hash import MD5
        if self.contains(key):
            h  = MD5.new()
            h.update(key.encode("utf-8"))
            changeval = int(h.hexdigest(),16)
            num = changeval % self.capacity
            node = self.findway(key)
            if node.next:
                predict = node.next
                while node.next != None:
                    predict = node
                    node = node.next
                predict.next = node.next 
                return 
                    
            else:
                self.data[num] = None
                return 
        
        return 
    
    def remove(self,key):
        from Crypto.Hash import MD5
        while self.contains(key) == True:
            self.delete(key)
        return
    
#資料來源:
#https://docs.google.com/presentation/d/e/2PACX-1vT1HO9Nl475k2bR0l1x8_Tr4V5Wzx0BEqp9bpmHckvj8kTeJehhYVlOJUDVPhLQm6kjGCJ_sLMSBUw5/pub?start=false&loop=false&delayms=3000&slide=id.g790b8351ca_0_59
#http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html
#https://medium.com/@fchern/%E8%A8%AD%E8%A8%88%E9%AB%98%E6%95%88%E8%83%BD%E7%9A%84hash-table-%E4%B8%80-303d9713abab
#https://toyo0103.blogspot.com/2018/04/hash-table.html


# In[ ]:




