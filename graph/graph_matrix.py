#class GraphError(ValueError):
 #   pass


class Graph:
    def __init__(self, mat, unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError("argument for graph")  # check if a square
        self._mat = [mat[i][:] for i in range(vnum)]  # copy in class
        self._unconn = unconn
        self._vnum = vnum  # number of vertex

    def vertex_num(self):
        return self._vnum

    def _invalid(self, v):
        return 0 > v or v >= self._vnum

    def add_vertex(self):
        raise ValueError("Adj-Matrix does not support 'add_vertex'")

    def add_edge(self, vi, vj, val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError(str(vi) + 'or' + str(vj) + "is not a valid vertex")
        self._mat[vi][vj] = val

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError(str(vi) + 'or' + str(vj) + "is not a valid vertex")
        return self._mat[vi][vj]
