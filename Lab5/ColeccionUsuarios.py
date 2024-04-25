from Usuario import Usuario
from ListDouble import ListDouble

class ColeccionUsuarios:
    def __init__(self):
        self._UsuariosList = ListDouble()

    def merge(self, L, R):
            i = j = 0
            if i < L.size() and j < R.size():
                if L.get(i).getData().getId() < R.get(j).getData().getId():
                    self.addLast(L.get(i))
                    i += 1
                else:
                    self.addLast(R.get(j))
                    j += 1
            return self._UsuariosList

    def mergeSort(self):
        if self._UsuariosList.size > 1:
            mid = self._UsuariosList.size // 2
            left = self._UsuariosList.slice(0, mid)
            right = self._UsuariosList.slice(mid, self._UsuariosList.size)

            L = self.mergeSort(left)
            R = self.mergeSort(right)
            return self.merge(L, R)
        else:
            return self._UsuariosList
        