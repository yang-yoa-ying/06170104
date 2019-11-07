# Heapsort
heapsort可以分為Min Heap與Max Heap兩種
# 流程
以數列[9,8,5,7,6,11,1,2,3]為例，先將資料二元排序，並將下方帶有節點的資料找出(本圖為藍色1,2,3,4)，由大到小數字選節點比大小，將結點與底下代的數字依照順序由後往前比大小，將小的往上排
[!image](https://github.com/yang-yoa-ying/06170104/blob/master/HW2picture/merge1.jpg)
[!image](https://github.com/yang-yoa-ying/06170104/blob/master/HW2picture/merge2.jpg)
[!image](https://github.com/yang-yoa-ying/06170104/blob/master/HW2picture/merge3.jpg)
[!image](https://github.com/yang-yoa-ying/06170104/blob/master/HW2picture/merge4.jpg)
接下來將最上方的數字填入新數列，並將最後一個數補在第一格位置
[!image](https://github.com/yang-yoa-ying/06170104/blob/master/HW2picture/merge5.jpg)
[!image](https://github.com/yang-yoa-ying/06170104/blob/master/HW2picture/merge6.jpg)
重複此動作便可得到排序完成數列[1,2,3,5,6,7,8,9,11]
