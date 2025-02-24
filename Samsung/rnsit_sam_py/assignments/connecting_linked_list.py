class Solution:
    headA = None #given
    headB = None #given
    class ListNode:
        pass

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) :
        lista = headA
        listb = headB

        while lista != listb:
            lista = lista.next if lista else headB
            listb = listb.next if listb else headA

        return listb