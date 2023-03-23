     def insertionSortList(self, head):

        temp = ListNode(0)
        temp.next = ins = head
        
        while head and head.next:
            if head.val > head.next.val:
                ins = head.next
                pre = temp
                while pre.next.val < ins.val:
                    pre = pre.next
                    
                head.next = ins.next
                nodeToInsert.next = pre.next
                pre.next = ins
            else:
                head = head.next
            
        return temp.next
