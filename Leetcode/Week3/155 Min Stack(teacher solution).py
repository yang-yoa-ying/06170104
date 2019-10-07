class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append((x, min(x, self.getMin())))

    def pop(self) -> None:
        if len(self.stack)==0:
            return None
        return self.stack.pop()[0]

    def top(self) -> int:
        if len(self.stack)==0:
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack)==0:
            return float('inf')
        return self.stack[-1][1]
 #這種方法是利用stack的方式去儲存資料，由[]變成[(1,1)]再存乘[(1,1),(2,1)]一筆一筆資料增加，因為若不用stack再刪除玩top資料後再找min需再次執行min(),十分耗時
 #ex. [1,2,3,4,5,6,7,8]用找min()最小值等於1再將top刪除變成[1,2,3,4,5,6,7]再用找min()最小值，等於1比了15次大小
 #但若[(1,1),(1,2),(1,2),(1,4),(1,5),(1,6),(1,7),(1,8)]用找min()最小值等於1再將top刪除變成[(1,1),(1,2),(1,2),(1,4),(1,5),(1,6),(1,7)]再找最小值，等於比了8次大小
 
 

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
