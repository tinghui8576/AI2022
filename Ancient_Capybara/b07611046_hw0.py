import sys
class Solution:
    def __init__(self):
        self.graph = dict()
        self.visited = set() # Set to keep track of visited nodes of graph.
        
        N,M = (int(i) for i in sys.stdin.readline().split())

        for i in range(M):
            u, v = (int(i) for i in sys.stdin.readline().split())
            if u in self.graph:
                self.graph[u] += [v]
            else:
                self.graph[u] = [v]
            if v in self.graph:
                self.graph[v] += [u]
            else:
                self.graph[v] = [u]
        #print(self.graph)
    
    #Feel free to define your own member function
    @staticmethod
    def dfs(visited, graph, node):  #function for dfs 
        if node not in visited:
            print node,
            visited.add(node)
                
            if node in graph:
                neighbour = graph[node]
                if neighbour :
                    while min(neighbour) in visited:
                        if graph[node] is not None: 
                            graph[node].remove(min(neighbour))
                            neighbour = graph[node]
                              
                        if not neighbour:
                            break
                    if neighbour :  
                        Solution.dfs(visited, graph, min(neighbour))
                        
                #for neighbour in graph[node]:
                    #print('node' + node + ' mini' + min(neighbour))
    def solve(self):
        
        # Driver Code
        #print("Following is the Depth-First Search")
        Solution.dfs(self.visited, self.graph, 1)


if __name__ == '__main__':
    ans = Solution()
    ans.solve()

    

        

                



