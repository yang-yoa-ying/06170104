# 流程圖
![image](https://github.com/yang-yoa-ying/06170104/blob/master/HW2picture/BST.jpg)
# 學習歷程
一開始最難想的一關便是我不太確定Class的語法，雖然在上一次的功課有先看過，但整體而言並不熟練，所以去看了很多class的語法，再來是對將想法畫作成是有所障礙，雖然老師在實習課時有花時間帶我們練習，但由於我技術債欠太多，使得要花更多的時間去補上這塊大洞，想法的部分新增和蟳都相對值觀，但刪除的部分卻困擾我好久，本來是想將刪除資料的下方一個資料依序補上，但要補左補右卻困擾我很久，後來將助教的測值畫在紙上，與一開始的值做比較，才發現原來是找最靠近已被刪除的樹所畫下值線的數來將刪除的值補上，但刪除還有很多細節，讓我花了許多時間去構想，最後是讓我苦惱最久的，便是測值的使用，雖然知道ture or flase ，但無法看到樹的長相，後來在朋友的幫助下，想出了一個一個將樹的數值印出來的方法，實在很感謝他們
# BST原理
## 概念
BST是利用以二元樹的模式進行產生，利用比大小的方式，將小的數字往左大的數字往右(注意:在這裡的依順序是不用先比大小，是跟已經放上去的數做比較)，由流程圖可以看出，我們利用比大小的方式可建出一棵數。
## 好處
* 時間複雜度為O(log(n))
* 空間複雜度O(N)   ->時間複雜度最慘情況為O(N)
* 如果資料夠亂(沒排序)搜尋時間將會大幅縮減
## 缺點
* 若在不夠亂的資料狀況下時間複雜度最慘情況為O(N)
# 參考資料
* http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html
* http://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html
* https://docs.google.com/presentation/d/e/2PACX-1vQgUh73yvSdxAvMH50DHWJ5lsCX8-daMxtoltU9rYW7xCmqYz2A1wOv0Vcx_F9KO5ZUvZBv3IF1TjGi/pub?start=false&loop=false&delayms=3000&slide=id.g659a558647_1_0
* https://matthung0807.blogspot.com/2018/04/binary-search-ologn.html
