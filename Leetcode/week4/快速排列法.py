#!/usr/bin/env python
# coding: utf-8

# In[1]:


def quicksort(list):
    if len(list) <= 1:
        return list #如果輸入的list長度<=1，表示數列裡沒有數字，就不需要排列了
    else:
        pivot = list[-1] #基準點就設定為list的最後一個數字
        bigger = [] #放大的數字
        equal = [] #放跟基準點一樣的數字
        smaller = [] #放小的數字
        for num in list:           #將list內所有數字跑過一次                          
            if num > pivot:
                bigger.append(num) #比基準點大就append進去bigger
            elif num == pivot:
                equal.append(num) #跟基準點一樣就append進去equal
            else:
                smaller.append(num) #比基準點小就append進去smaller
    return quicksort(smaller) + equal + quicksort(bigger) #smaller跟bigger繼續排列，equal不必再排列了


# In[2]:


quicksort([1,2,5,6,99,34,56])


# In[ ]:





# In[ ]:




