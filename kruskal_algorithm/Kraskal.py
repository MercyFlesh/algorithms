import timsort
import argparse
import re


class Graph:
    def __init__(self):
        self.graph = {}
        self.vertex = set()

    def add_relation(self, weight, vert1, vert2): 
        self.graph.update({(vert1, vert2): weight})
        
    
    def sort(self, graph, vert_edge):
        graph_list = list(graph.items())
        
        if len(graph_list) < 64:
            timsort._insert_sort(graph_list, vert_edge)  #[(('x', 'y'), 15), (('h', 'z'), 18)] the second parameter is set to sort by vertex/edge values 
        else:
            timsort.Timsort(graph_list, vert_edge)
       
        return dict(graph_list)
        

    def bypass(self, value, connected, adjency, edge_list, visited):
        for w in edge_list:
            if visited[w] == False:
                visited[w] = True
                connected[w] = value
                self.bypass(value, connected, adjency, adjency[w], visited)


    
    def find(self, edge, connected, adjency):
        if connected[edge[1]] == 0 and connected[edge[0]] == 0:
            max_con = max(connected.values())
            connected.update({edge[0]: max_con + 1, edge[1]: max_con + 1})
            adjency.update({edge[0]: list(edge[1]), edge[1]: list(edge[0])})
            return True
        elif connected[edge[1]] != connected[edge[0]]:
            visited = dict.fromkeys(self.vertex, False)
            max_con = max(connected[edge[1]], connected[edge[0]])
            
            if edge[0] in adjency:
                adjency[edge[0]].append(edge[1])
            else:
                adjency[edge[0]] = list(edge[1])

            if edge[1] in adjency:
                adjency[edge[1]].append(edge[0])
            else:
                adjency[edge[1]] = list(edge[0])
            
            self.bypass(max_con, connected, adjency, adjency[edge[0]], visited)
            return True
        else:
            return False

    
    def Kruskal(self):
        result = dict()
        adjency_list = dict()
        weight_graph = 0
        self.graph = self.sort(self.graph, 1)
        for vert in self.graph:
            self.vertex.update(vert[0], vert[1])
        connected = dict.fromkeys(self.vertex, 0)
       
        for edge in self.graph:
            if self.find(edge, connected, adjency_list):
                result[edge] = self.graph[edge]
                weight_graph += result[edge]
            if len(result) == len(self.vertex) - 1:
                break

        result = self.sort(result, 0)
        for edge in result:
            print(edge[0], edge[1])
        print(weight_graph)
        

        

if __name__ == "__main__":
    #args_pars = argparse.ArgumentParser()
    #args_pars.add_argument('--path', help='Full path to file .txt')
    #args = args_pars.parse_args()
    path = input("Enter the full file path: ") 
    g = Graph()

    try:
        #if args.path:
            with open(path, 'r') as f:
                for line in f:
                    match_line = re.search(r'(\d+)?\s*([a-zA-Z])\s?([a-zA-Z])\s*(\d+)?', line)
                    if match_line.groups()[0] != None:
                        g.add_relation(int(match_line.groups()[0]), match_line.groups()[1], match_line.groups()[2])
                    elif match_line.groups()[3] != None:
                        g.add_relation(int(match_line.groups()[3]), match_line.groups()[1], match_line.groups()[2])

                    else:
                        raise Exception("Error: incorrect data entry in the file")
                    
                g.Kruskal()
        #else:
        #    raise Exception('Error: incorrect args')
    except IOError as er:
        print(er)
    
    except Exception as ex:
        print(ex)
    
    