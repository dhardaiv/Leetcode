class Solution:
    def reverseList(self, head):
        prev = None 
        curr = head 

        while curr: 
            temp = curr.next 
            curr.next = prev 
            prev = curr
            curr = temp
        return prev

# time - O(n)
# space - O(1)
