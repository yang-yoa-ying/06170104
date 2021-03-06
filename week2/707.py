class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None                      #初始化資料
        self.next = None


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.val == None:             #如果val等於空值返回-1
            return -1
        if index == 0:                   #如果index等於0,回傳self.val，這裡是將index當作pointer，若pointer為0代表指向第一個memory所存的值
            return self.val              #故回傳self.val                            
        p = self.next                    
        i = 1                            #因為將第0個給用掉了，i由1開始
        while p != None:                 #利用while迴圈判斷若index尚未指向空值，則回傳值並由下一個值指向下下一個值，直到空值則回傳-1
            if i == index:
                return p.val
            p = p.next
            i += 1
        return -1
        
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.val == None:
            self.val = val                #如果self.value為空值，則將val代入
            return                        #return後不加數值或參數，後不加數值或參數，代表返回None值(用於表示功能已成功結束)
        temp = self.val
        self.val = val                    #為了在前方加一個val所有東西必須往後移一個，因此self.val = self.val ,self.next.next = self.next
        tempnode = self.next
        self.next = MyLinkedList()         #新的node of value
        self.next.val = temp
        self.next.next = tempnode
        return

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.val == None:               #如果self.value為空值，則將val代入
            self.val = val
            return
        p = self
        while p.next != None:           #如果self.value為不空值，則將self = self.next，直到沒有self.next
            p = p.next
        p.next = MyLinkedList()         
        p.next.val = val                #新的node of value
        return
        
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        i = 0
        p = self
        pre = p
        if index <= 0:                          #如果index<=0代表加到最前方故用addAtHead()
            self.addAtHead(val)
            return
        while i < index:
            i += 1                              #找出index所指到的pointer
            pre = p
            if p != None and p.val != None:
                p = p.next
            else:
                return
        pre.next = MyLinkedList()               
        pre.next.val = val                      
        pre.next.next = p                       
        return

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        i = 0
        p = self
        if index < 0:
            return
        if index == 0:
            if self.val == None:
                return
            if self.next == None:
                self = None
                return
            self.val = self.next.val
            self.next = self.next.next
        pre = p
        while i < index:
            i += 1
            pre = p
            if pre == None:
                return
            p = p.next
        if p != None:
            pre.next = p.next
        else:
            pre.next = None
        return 

        
        
  
