# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node pointing to the head to handle edge cases (like deleting the head node)
        temp = ListNode(0)
        temp.next = head
        
        # Initialize pointers: `prev` starts at the dummy node, `curr` starts at the head
        prev, curr = temp, head
        
        # Traverse the linked list until the end
        while curr:
            # Check if the current node's value matches the target value
            if curr.val == val:
                # If it matches, bypass the current node by linking `prev.next` to `curr.next`
                prev.next = curr.next
            else:
                # If it doesn't match, move `prev` pointer to the current node
                prev = curr
            
            # Move to the next node in the list
            curr = curr.next
        
        # Return the modified list, starting from the original head or a new head if the first nodes were removed
        return temp.next

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head
        prev, curr = temp, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return temp.next