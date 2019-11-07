#!/usr/bin/env python
# coding: utf-8

# In[26]:


a = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]


# In[27]:


def level(www):
    count = 1
    while (count < len(a)):
        count = count*2
    return count


# In[28]:


if level(a) != 1:
    c = int(level(a) / 2)
c    


# 想了解一下最下面那一排可以放幾個數字

# In[29]:


for i in range(len(a)-1,c-2,-2):
    print(i)
    print(i-1)
    print(int(c/2)+int((i-c+1)/2)-1)


# In[30]:


for i in range(len(a)-1,c-1,-2):
    print(i)
    print(i-1)
    print(round(float(c)/2+0.01)+int((i-c+1)/2)-1)


# In[31]:


round(2.51)


# In[32]:


a


# In[33]:


for i in range(len(a)-1,c-2,-2):
    if a[i] < a[round(float(c)/2+0.01)+int((i-c+1)/2)-1]:
        a[i] , a[round(float(c)/2+0.01)+int((i-c+1)/2)-1] = a[round(float(c)/2+0.01)+int((i-c+1)/2)-1] ,a[i]
    if a[i-1] < a[round(float(c)/2+0.01)+int((i-c+1)/2)-1]:
        a[i-1] , a[round(float(c)/2+0.01)+int((i-c+1)/2)-1] = a[round(float(c)/2+0.01)+int((i-c+1)/2)-1] ,a[i-1]
a


# 因為在做heapsort時只有最下面那排看起來最複雜，因此先嘗試將他們做交換

# In[34]:


n = 0
m = 1
while (m < c):
    n = n+1
    m = m*2


# In[35]:


c= 8


# In[36]:


c= 8
c = int(c/2)
for k in range(2**n-2,c-2,-2):
    print(k)
    print(k-1)
    print(int(c/2)+int((k-c+1)/2)-1)


# In[37]:


n = 3


# In[38]:


c= 8
c = int(c/2)
for j in range(n,1,-1):
    for k in range(2**j-2,c-2,-2):
        print(k)
        print(k-1)
        print(int(c/2)+int((k-c+1)/2)-1)
    c = int(c/2)


# In[39]:


c= 8
c = int(c/2)
for j in range(n,1,-1):
    for k in range(2**j-2,c-2,-2):
        if a[k] < a[int(c/2)+int((k-c+1)/2)-1]:
            a[k] , a[int(c/2)+int((k-c+1)/2)-1] = a[int(c/2)+int((k-c+1)/2)-1] , a[k]
        if a[k-1] < a[int(c/2)+int((k-c+1)/2)-1]:
            a[k-1] , a[int(c/2)+int((k-c+1)/2)-1] = a[int(c/2)+int((k-c+1)/2)-1] , a[k-1]
    c = int(c/2)
a


# 將剩下來規律的金字塔做交換

# In[40]:


ans = []
a = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
if level(a) != 1:
    c = int(level(a) / 2)
for i in range(len(a)-1,c-1,-2):
    if a[i] < a[round(float(c)/2+0.01)+int((i-c+1)/2)-1]:
        a[i] , a[round(float(c)/2+0.01)+int((i-c+1)/2)-1] = a[round(float(c)/2+0.01)+int((i-c+1)/2)-1] ,a[i]
    if a[i-1] < a[round(float(c)/2+0.01)+int((i-c+1)/2)-1]:
        a[i-1] , a[round(float(c)/2+0.01)+int((i-c+1)/2)-1] = a[round(float(c)/2+0.01)+int((i-c+1)/2)-1] ,a[i-1]
n = 0
m = 1
while (m < c):
    n = n+1
    m = m*2
c = int(c/2)
for j in range(n,1,-1):
    for k in range(2**j-2,c-2,-2):
        if a[k] < a[int(c/2)+int((k-c+1)/2)-1]:
            a[k] , a[int(c/2)+int((k-c+1)/2)-1] = a[int(c/2)+int((k-c+1)/2)-1] , a[k]
        if a[k-1] < a[int(c/2)+int((k-c+1)/2)-1]:
            a[k-1] , a[int(c/2)+int((k-c+1)/2)-1] = a[int(c/2)+int((k-c+1)/2)-1] , a[k-1]
    c = int(c/2)
ans.append(a[0])
ans
del a[0]
a[-1] , a[0] = a[0] , a[-1]


# In[41]:


a


# 嘗試對第一個排序後的數字做提出並存入第一新list，因為list被刪掉後，第一個數會自動由第二個數依序補上，故不用將最後一個術語第一個交換候補上

# In[42]:


ans = []
a = [1,2,11,4,5,6,7,8,10,9]
for lll in range(len(a)):
    c = int(level(a) / 2)
    for i in range(len(a)-1,c-2,-2):
        if a[i] < a[round(float(c)/2+0.01)+int((i-c+1)/2)-1]:
            a[i] , a[round(float(c)/2+0.01)+int((i-c+1)/2)-1] = a[round(float(c)/2+0.01)+int((i-c+1)/2)-1] ,a[i]
            print(a)
        if a[i-1] < a[round(float(c)/2+0.01)+int((i-c+1)/2)-1]:
            a[i-1] , a[round(float(c)/2+0.01)+int((i-c+1)/2)-1] = a[round(float(c)/2+0.01)+int((i-c+1)/2)-1] ,a[i-1]
            print(a)
    n = 0
    m = 1
    while (m < c):
        n = n+1
        m = m*2
    c = int(c/2)
    for j in range(n,1,-1):
        for k in range(2**j-2,c-2,-2):
            if a[k] < a[int(c/2)+int((k-c+1)/2)-1]:
                a[k] , a[int(c/2)+int((k-c+1)/2)-1] = a[int(c/2)+int((k-c+1)/2)-1] , a[k]
                print(a)
            if a[k-1] < a[int(c/2)+int((k-c+1)/2)-1]:
                a[k-1] , a[int(c/2)+int((k-c+1)/2)-1] = a[int(c/2)+int((k-c+1)/2)-1] , a[k-1]
                print(a)
        c = int(c/2)
    ans.append(a[0])
    del a[0]


# In[43]:


ans


# 嘗試將所有數都做完heapsort,成功!

# In[44]:


def heapSort(a):
    ans = []
    for lll in range(len(a)):
        count = 1
        while (count < len(a)):
            count = count*2
        c = int(count / 2)
        for i in range(len(a)-1,c-2,-2):
            if a[i] < a[round(float(c)/2+0.01)+int((i-c+1)/2)-1]:
                a[i] , a[round(float(c)/2+0.01)+int((i-c+1)/2)-1] = a[round(float(c)/2+0.01)+int((i-c+1)/2)-1] ,a[i]
            if a[i-1] < a[round(float(c)/2+0.01)+int((i-c+1)/2)-1]:
                a[i-1] , a[round(float(c)/2+0.01)+int((i-c+1)/2)-1] = a[round(float(c)/2+0.01)+int((i-c+1)/2)-1] ,a[i-1]
        n = 0
        m = 1
        while (m < c):
            n = n+1
            m = m*2
        c = int(c/2)
        for j in range(n,1,-1):
            for k in range(2**j-2,c-2,-2):
                if a[k] < a[int(c/2)+int((k-c+1)/2)-1]:
                    a[k] , a[int(c/2)+int((k-c+1)/2)-1] = a[int(c/2)+int((k-c+1)/2)-1] , a[k]
                if a[k-1] < a[int(c/2)+int((k-c+1)/2)-1]:
                    a[k-1] , a[int(c/2)+int((k-c+1)/2)-1] = a[int(c/2)+int((k-c+1)/2)-1] , a[k-1]
            c = int(c/2)
        ans.append(a[0])
        del a[0]
    return ans


# In[45]:


heapSort([1,2,11,4,5,6,7,8,10,9])


# In[46]:


import numpy as np


# In[47]:


arr = np.random.randint(100,size=3)


# In[48]:


list1 = arr.tolist()


# In[49]:


list1


# In[50]:


heapSort(list1)


# In[51]:


class Solution(object):
    def heap_sort(self,a):
        ans = []
        for lll in range(len(a)):
            count = 1
            while (count < len(a)):
                count = count*2
            c = int(count / 2)
            for i in range(len(a)-1,c-2,-2):
                if a[i] < a[round(float(c)/2+0.01)+int((i-c+1)/2)-1]:
                    a[i] , a[round(float(c)/2+0.01)+int((i-c+1)/2)-1] = a[round(float(c)/2+0.01)+int((i-c+1)/2)-1] ,a[i]
                if a[i-1] < a[round(float(c)/2+0.01)+int((i-c+1)/2)-1]:
                    a[i-1] , a[round(float(c)/2+0.01)+int((i-c+1)/2)-1] = a[round(float(c)/2+0.01)+int((i-c+1)/2)-1] ,a[i-1]
            n = 0
            m = 1
            while (m < c):
                n = n+1
                m = m*2
            c = int(c/2)
            for j in range(n,1,-1):
                for k in range(2**j-2,c-2,-2):
                    if a[k] < a[int(c/2)+int((k-c+1)/2)-1]:
                        a[k] , a[int(c/2)+int((k-c+1)/2)-1] = a[int(c/2)+int((k-c+1)/2)-1] , a[k]
                    if a[k-1] < a[int(c/2)+int((k-c+1)/2)-1]:
                        a[k-1] , a[int(c/2)+int((k-c+1)/2)-1] = a[int(c/2)+int((k-c+1)/2)-1] , a[k-1]
                c = int(c/2)
            ans.append(a[0])
            del a[0]
        return ans


# In[52]:


a = Solution().heap_sort([9,7,5,3])
a


# 將式子變成def並用class包裝，完成

# 參考資料:
# 1.老師ppt https://docs.google.com/presentation/d/e/2PACX-1vRAGwnUvg6BcXoML5u9f4gO6YKcz0vXf7bDnPho_S7mG5D0SBR78djt91RKUPMxqNfkVIcu3l5WCXPh/pub?start=false&loop=false&delayms=3000&slide=id.g6504c48e6e_0_37

# In[ ]:




