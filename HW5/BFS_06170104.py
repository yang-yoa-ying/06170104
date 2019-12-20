#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict


# In[2]:


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def test(self,s):
        return self.graph[s]
    
    def test2(self,s):
        return self.graph
    
    def yesno(self,a,b):
        for i in range(len(a)):
            if a[i] == b:
                return False
        return True
    
    def BFS(self,s):
        ans = []
        ans.append(s)
        b = self.test(s)
        c = []
        for i in self.graph:
            if b != []:
                for j in range(len(b)):
                    ans.append(b[j])        #b增加
                    
                for j in range(len(b)):
                    for k in range(len(self.test(b[j]))):
                        if self.yesno(ans,self.test(b[j])[k]) == True:
                            if self.yesno(b,self.test(b[j])[k]) == True:
                                c.append(self.test(b[j])[k]) 
                            
                b = c
                c = []
        
        return ans
                
    def DFS(self , s):
        ans = []
        ans.append(s)
        b = self.test(s)
        c = []
        for i in self.graph:
            if b != []:
                ans.append(b[-1])
                for k in range(len(self.test(b[-1]))):
                    if self.yesno(ans,self.test(b[-1])[k]) == True:
                        if self.yesno(b,self.test(b[-1])[k]) == True:
                            c.append(self.test(b[-1])[k])
                            
                b.pop()
                for w in range(len(c)):
                    b.append(c[w])
                c = []
        return ans


# In[3]:


g = Graph()


# In[4]:


g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)


# In[5]:


print(g.BFS(2))


# In[6]:


print(g.DFS(2))


# 參考資料:
# https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html
# https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html
# https://docs.google.com/presentation/d/e/2PACX-1vSYJYXUXvGAeTZ5fknxj_-EPm3zxgy4ITdImrXzy63Y-iZgs8uwVNmOaZlnx9fUNzsbo8kphvMTa0c4/pub?start=false&loop=false&delayms=3000&slide=id.p
# https://docs.google.com/presentation/d/e/2PACX-1vTma_vOZyE70O23KWw4I4Y78aAaT5fJSTq7Mae912kCwka_u5ZMWPoo14D86-x-57kZPbb6hAGktSW4/pub?start=false&loop=false&delayms=3000&slide=id.p

# In[ ]:




