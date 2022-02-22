# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        elements=[]
        while(head!=None):
            elements.append(head)
            head=head.next
        x=len(elements)//2
        return elements[x]
        