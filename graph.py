


class graph:

    def __init__(self, isDirected):
        self.isDirected = isDirected
        self.size = 0
        self.vertices = {}
        self.edges = [()]

    def createVertex(self, name):
        self.vertices[name] = graph.vertex()

    def deleteVertex(self, name):
        self.vertices.pop(name)

    def addEdge(self, name1, name2):
        self.edges.append((name1, name2))

        if(self.isDirected):
            self.vertices[name1].addEdgeTo(self.vertices[name2])
        else:
            self.vertices[name1].addEdge(self.vertices[name2])

    def removeEdge(self, name1, name2):
        
        if(self.isDirected):
            self.vertices[name1].removeEdgeTo(self.vertices[name2])
        else:
            self.vertices[name1].removeEdge(self.vertices[name2])


    class vertex:

        def __init__(self):
            self.pred = []
            self.succ = []
            self.adj = []

        def addEdge(self, v2):
            self.adj.append(v2)
            v2.adj.append(self)

        def removeEdge(self, v2):
            self.adj.remove(v2)
            v2.adj.remove(self)

        def addEdgeTo(self, v2):
            self.adj.append(v2)
            self.succ.append(v2)
            v2.adj.append(self)
            v2.pred.append(self)

        def removeEdgeTo(self, v2):
            self.adj.remove(v2)
            self.succ.remove(v2)
            v2.adj.remove(self)
            v2.pred.remove(self)