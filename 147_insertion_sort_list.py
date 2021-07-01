# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        

        root = ListNode()

        
        while head :
            temp =root

            while temp.next and temp.next.val < head.val:
                temp = temp.next

            temp.next = ListNode(head.val,temp.next)
            head = head.next
            
        return root.next
        


def main():
    sol = Solution()
    

    head3 = ListNode(1)
    head2 = ListNode(3,head3)
    head1 = ListNode(2,head2)
    head = ListNode(4,head1)

    output = sol.insertionSortList(head)
    print(output)
    # output = [0,1]

    


if __name__ == "__main__":
    # execute only if run as a script
    main()