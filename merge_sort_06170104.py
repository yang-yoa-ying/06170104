#!/usr/bin/env python
# coding: utf-8

# In[136]:


def cut(a):
    if len(a)<=1:
        return a
    else:
        left = a[:round(len(a)/2+0.01)]
        right = a[round(len(a)/2+0.01):]
        return cut(left),cut(right)


# In[126]:


test = [8,2,4,3,5,9,7,11,4,5,66]


# In[127]:


cut(test)


# 一看到要做merge sort 就會想要先做切割，一開始想要用list切前半段和後半段，但只能切一次，之後想到用函數裡再包函數達到迴圈切割的效果

# In[13]:


c =[2,4,9,3,8]
a = [2,4,9] 
b = [3,8]
k = 0


# In[14]:


while len(a) != False and len(b) != False:
    if a[0] < b[0]:
        c[k] = a[0]
        del a[0]
        k = k+1
    elif a[0] > b[0]:
        c[k] = b[0]
        del b[0]
        k = k+1
while len(a) != False:
    c[k] = a[0]
    k = k+1
    del a[0]
while len(b) != False:
    c[k] = b[0]
    k = k+1
    del b[0]


# In[15]:


c


# In[81]:


k


# 想試試看切割完左右的list比大小後合併

# In[8]:


def mergetool(w):
    c = w
    a = cut(w)[0]
    b = cut(w)[1]
    k = 0
    while len(a) != False and len(b) != False:
        if a[0] < b[0]:
            c[k] = a[0]
            del a[0]
            k = k+1
        elif a[0] > b[0]:
            c[k] = b[0]
            del b[0]
            k = k+1
    while len(a) != False:
        c[k] = a[0]
        k = k+1
        del a[0]
    while len(b) != False:
        c[k] = b[0]
        k = k+1
        del b[0]
    return c


# In[25]:


def cut(a):
    if len(a)<=1:
        return 
    else:
        left = a[:round(len(a)/2+0.01)]
        right = a[round(len(a)/2+0.01):]
        return left,right


# In[33]:


a = cut([5,4,3,2,1])


# In[34]:


a


# In[39]:


cut(a)[1][0]


# In[49]:


def mergetool(w):
    c = w
    print(c)
    a = cut(w)[0]
    b = cut(w)[1]
    print(a)
    print(b)
    k = 0
    while len(a) != False and len(b) != False:
        if a[0] < b[0]:
            c[k] = a[0]
            del a[0]
            k = k+1
        elif a[0] > b[0]:
            c[k] = b[0]
            del b[0]
            k = k+1
    while len(a) != False:
        c[k] = a[0]
        k = k+1
        del a[0]
    while len(b) != False:
        c[k] = b[0]
        k = k+1
        del b[0]
    print(c)
    return c


# In[50]:


a =mergetool([5,4,3,2,1])


# 想將cut完的內容帶入比大小內，但發現無法教出正確的位置比大小，只能先用cut一次的方式製作一次排序比大小

# In[70]:


def mergetool(w):
    if len(w) > 1:
        c = w
        print(c)
        a = cut(w)[0]
        b = cut(w)[1]
        print(a)
        print(b)
        mergetool(a)
        mergetool(b)
        k = 0
        while len(a) != False and len(b) != False:
            if a[0] < b[0]:
                c[k] = a[0]
                del a[0]
                k = k+1
            elif a[0] > b[0]:
                c[k] = b[0]
                del b[0]
                k = k+1
        while len(a) != False:
            c[k] = a[0]
            k = k+1
            del a[0]
        while len(b) != False:
            c[k] = b[0]
            k = k+1
            del b[0]
        print(c)
        return c


# In[77]:


a =mergetool([9,8,7,6,5,4,3,2,1])


# In[7]:


test = [8,2,4,3,5,9,7,11,4,5,66]


# In[71]:


mergetool(test)


# 突然想到那我就在mergetool裡重複跑cut就可以達到我要的效果，在開心應該成功後十冊卻發現有失敗，原來是比大小時忘了=的情況

# In[8]:


def mergetool(w):
    if len(w) > 1:
        c = w
        print(c)
        a = cut(w)[0]
        b = cut(w)[1]
        print(a)
        print(b)
        mergetool(a)
        mergetool(b)
        k = 0
        while len(a) != False and len(b) != False:
            if a[0] < b[0]:
                c[k] = a[0]
                del a[0]
                k = k+1
            elif a[0] >= b[0]:
                c[k] = b[0]
                del b[0]
                k = k+1
        while len(a) != False:
            c[k] = a[0]
            k = k+1
            del a[0]
        while len(b) != False:
            c[k] = b[0]
            k = k+1
            del b[0]
        print(c)
        return c


# In[9]:


mergetool(test)


# 終於完成mergesort

# In[13]:


def cut(a):
    if len(a)<=1:
        return 
    else:
        left = a[:round(len(a)/2+0.01)]
        right = a[round(len(a)/2+0.01):]
        return left,right
def mergetool(w):
    if len(w) > 1:
        c = w
        a = cut(w)[0]
        b = cut(w)[1]
        mergetool(a)
        mergetool(b)
        k = 0
        while len(a) != False and len(b) != False:
            if a[0] < b[0]:
                c[k] = a[0]
                del a[0]
                k = k+1
            elif a[0] >= b[0]:
                c[k] = b[0]
                del b[0]
                k = k+1
        while len(a) != False:
            c[k] = a[0]
            k = k+1
            del a[0]
        while len(b) != False:
            c[k] = b[0]
            k = k+1
            del b[0]
        return c


# In[14]:


mergetool([8,2,5,4,3,1,9])


# 將mergesort整理再一起

# In[4]:


class Solution(object):
    def cut(self ,a):
        if len(a)<=1:
            return 
        else:
            left = a[:round(len(a)/2+0.01)]
            right = a[round(len(a)/2+0.01):]
            return left,right
    def merge_sort(self , w):
        if len(w) > 1:
            c = w
            a = Solution().cut(w)[0]
            b = Solution().cut(w)[1]
            Solution().merge_sort(a)
            Solution().merge_sort(b)
            k = 0
            while len(a) != False and len(b) != False:
                if a[0] < b[0]:
                    c[k] = a[0]
                    del a[0]
                    k = k+1
                elif a[0] >= b[0]:
                    c[k] = b[0]
                    del b[0]
                    k = k+1
            while len(a) != False:
                c[k] = a[0]
                k = k+1
                del a[0]
            while len(b) != False:
                c[k] = b[0]
                k = k+1
                del b[0]
            return c
    


# In[13]:


a = Solution().merge_sort([-0.5,-1,-1,9,7,5,3])
a


# In[14]:


a


# 用class包裝後大功告成

# 參考資料:
# 1. http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html
# 2. https://www.geeksforgeeks.org/merge-sort/

# In[ ]:




