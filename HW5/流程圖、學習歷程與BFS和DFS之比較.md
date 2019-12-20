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
這一次的功課我寫的比較快，大概花6個小時就將功課寫完了，主要花的時間是因為我沒了解清楚助教給的程式碼，才會多花了一點時間，我覺得在寫程式的路上，我學得越來越好，因為我花了很長的時間練習程式碼，所以才變得越來越會寫，但老師在上課時說的話，我非常不認同，我認為我們並沒有抱著敷衍的心態去做事，相反的，正因為我們對於追求卓越才會想要明確的規則，不是每位同學都有足夠的創意來自己想出最卓越的作品，我認為明確的規則對我們來說正是一種對實力衡量的標準，對大部分的人而言是一種安心的象徵，它會讓我們相信有付出必定會有收穫，而不是花一推時間朝一個不確定的未來，我認為老師所說的希望我們變得更卓越的"方法"，實際上只是打擊我們的工具而已，我認為老師想讓我們更加卓越的心態是好的，提早讓我們接受社會洗禮的用意也是好的，但我真心的覺得如果老師希望激起我們對於程式的熱情，應該是在給我們壓力的同時，適時的給予我們舒緩的機會，讓我們在寫程式的壓力得以平衡，增加學習效率(根據職業壓力預防手冊，壓力與工作效率呈現到U的圖)，我認為老師所作的方式，雖然立意良善，但我認為卻重傷我們，不明確的規則已造成我們對未來的不確定，並且認為助教只是憑感覺隨他開心的給分而已，我希望老師了解，大部分同學都希望自己能獲得高分而努力，只有少部分的同學希望有過就好而不加努力，老師的話著實對於我們是重傷。
# 參考資料
* https://blog.csdn.net/judyge/article/details/45007337
* https://www.itread01.com/content/1541297601.html
* https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/102866/
* https://magiclen.org/dfs-bfs/
* https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html
* https://docs.google.com/presentation/d/e/2PACX-1vTma_vOZyE70O23KWw4I4Y78aAaT5fJSTq7Mae912kCwka_u5ZMWPoo14D86-x-57kZPbb6hAGktSW4/pub?start=false&loop=false&delayms=3000&slide=id.g7aa022d8bc_2_0
* https://docs.google.com/presentation/d/e/2PACX-1vSYJYXUXvGAeTZ5fknxj_-EPm3zxgy4ITdImrXzy63Y-iZgs8uwVNmOaZlnx9fUNzsbo8kphvMTa0c4/pub?start=false&loop=false&delayms=3000&slide=id.g7a5d8b85ee_0_44
* http://scc.yuntech.edu.tw/column/AA/c/c_04/c_04_12.htm
