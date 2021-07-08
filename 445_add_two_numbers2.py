# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_value = 0
        l2_value = 0
        l3 = ListNode()
        
        while l1 :
            l1_value = l1_value*10 + l1.val
            l1 = l1.next
            
        while l2 : 
            l2_value = l2_value*10 + l2.val
            l2 = l2.next

        l3_value = str(l1_value + l2_value)
        temp = l3
        for i in l3_value :
            temp.next = ListNode(i)
            temp = temp.next
        return l3.next
        
        
        
def main():
    sol = Solution()
    

    head3 = ListNode(3)
    head2 = ListNode(4,head3)
    head1 = ListNode(2,head2)
    l1 = ListNode(7,head1)

    head2 = ListNode(4)
    head1 = ListNode(6,head2)
    l2 = ListNode(5,head1)
    

    output = sol.addTwoNumbers(l1,l2)
    print(output)
    # output = [0,1]

    


if __name__ == "__main__":
    # execute only if run as a script
    main()