# 功能解說圖
![image](https://github.com/yang-yoa-ying/06170104/blob/master/HW2picture/1574428407960.jpg)
# 新增
* 新增資料的方式是以比大小的方式一路比下去，並找到適合的節點放入，如圖所示，另外在這次的查詢功能中我沿用了上次def包def的想法製作
# 查詢
* 查詢是一層一層向下比較，用比大小的方式決定左右，被捨棄的一邊的下方皆可不用在比，在這次的查詢功能中我沿用了上次def包def的想法製作
# 刪除
* 刪除是尋找最靠近被刪除值的方式呈現，如圖所示，在程式碼中我主要以4種方式呈現:
1. 全都只有右:我會將下方連接的數補上，並將更下方的數放在第二個數的位置，以此類推
2. 全都只有左:我會將下方連接的數補上，並將更下方的數放在第二個數的位置，以此類
3. 先左且有右:我會找先找左然後依值找右直到找到沒有右為止(self.left.right.right.....)(只有left或None)，並將此數代替被刪除值並刪除
4. 先右且有左:我會找先找右然後依值找左直到找到沒有左為止(self.right.left.left.....)(只有right或None)，並將此數代替被刪除值並刪除
# 修改
利用前面寫好的加上和刪除，將值添加並刪除以達到修改的功能
# 參考資料
* https://github.com/yang-yoa-ying/06170104/tree-save/master/HW3/binary_search_tree_06170104.py
* https://docs.google.com/presentation/d/e/2PACX-1vQgUh73yvSdxAvMH50DHWJ5lsCX8-daMxtoltU9rYW7xCmqYz2A1wOv0Vcx_F9KO5ZUvZBv3IF1TjGi/pub?start=false&loop=false&delayms=3000&slide=id.g6aecfee46c_2_11
* http://www.csie.ntnu.edu.tw/~u91029/Order.html
