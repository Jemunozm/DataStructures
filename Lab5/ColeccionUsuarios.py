from Usuario import Usuario
from ListDouble import ListDouble

class ColeccionUsuarios:
    def __init__(self):
        self._UsuariosList = ListDouble()

    def splitList(self,head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        if mid:
            mid.prev = None
        return head, mid
    
    def merge(self, first, second):
        if not first:
            return second
        if not second:
            return first
        
        if first.data.id <= second.data.id:
            first.next = self.merge(first.next, second)
            if first.next:
                first.next.prev = first
            first.prev = None
            return first
        else:
            second.next = self.merge(first, second.next)
            if second.next:
                second.next.prev = second
            second.prev = None
            return second

    def mergeSort(self, head):
        if not head or not head.next:
            return head
        
        first, second = self.splitList(head)
        first = self.mergeSort(first)
        second = self.mergeSort(second)

        return self.merge(first, second)
        