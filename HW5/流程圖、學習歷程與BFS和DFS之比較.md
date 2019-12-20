# BFS
![image](https://github.com/yang-yoa-ying/06170104/blob/master/HW2picture/bfs.jpg)
* 走法:先選定一個點為起點，當作第一層，並尋找與他相聯並不重複的點為第二層，接著依照順序將第二層加入第一層(先進先出)，直到無法找出第二層為止，得出的第一層變為答案。
## 優點
* 解決最短或最小問題特別有效

## 缺點
* 內存耗量大
* 必須遍歷所有分枝

# DFS
![image](https://github.com/yang-yoa-ying/06170104/blob/master/HW2picture/dfs.jpg)
* 走法:先選定一個點為起點，當作第一層，尋找與他相聯並不重複的點為第二層，接著將一個第二層的最後一個加入第一個，並依照那一個點尋找相鄰的不重複點加入第二層(若無此樹則跳過加入的動作一次)，重複此動作，直到第二層無法加入解第一層無法加入為止。
## 優點
* 占內存少
* 能找到最優解（一定條件下）
* 可能不必遍歷所有分枝
## 缺點
* DFS容易爆棧

# DFS　VS BFS
## 時間複雜度
* 一樣O(V+E)[平均]
## 內存比較
* dfs是與遞迴深度成正比的。一般與狀態數相比，遞迴深度並不會太大，所以dfs更加省記憶體
## 耗時
* dfs可以搜尋整個圖形，但是卻很可能繞了很久才找到目標，如果我們想找出到達目標最少的步驟，那麼就可以採用bfs
# 心路歷程
# 參考資料
* https://blog.csdn.net/judyge/article/details/45007337
* https://www.itread01.com/content/1541297601.html
* https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/102866/
* https://magiclen.org/dfs-bfs/
* https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html
* https://docs.google.com/presentation/d/e/2PACX-1vTma_vOZyE70O23KWw4I4Y78aAaT5fJSTq7Mae912kCwka_u5ZMWPoo14D86-x-57kZPbb6hAGktSW4/pub?start=false&loop=false&delayms=3000&slide=id.g7aa022d8bc_2_0
* https://docs.google.com/presentation/d/e/2PACX-1vSYJYXUXvGAeTZ5fknxj_-EPm3zxgy4ITdImrXzy63Y-iZgs8uwVNmOaZlnx9fUNzsbo8kphvMTa0c4/pub?start=false&loop=false&delayms=3000&slide=id.g7a5d8b85ee_0_44
