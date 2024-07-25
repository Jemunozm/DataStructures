from Usuario import Usuario
from ListDouble import ListDouble

class ColeccionUsuarios:
    def __init__(self):
        self._UsuariosList = ListDouble()

    def merge(self, L, R):
        i = j = 0
        k = 0
        while k < self._UsuariosList.size:
            if i < L.currentPositionNode() and j < R.currentPositionNode(): 
                if L.get(i).getData().getId() < R.get(j).getData().getId():
                    self.addLast(L.get(i))
                    i += 1
                    k += 1
                else:
                    self.addLast(R.get(j))
                    j += 1
                    k += 1
        return self._UsuariosList

    def mergeSort(self, inicio, final):
        mid = final // 2
        if inicio < mid:
            L = self.mergeSort(0, mid)
            R = self.mergeSort(mid,final)
            return self.merge(L, R)
        else:
            return self._UsuariosList
        