vertex = list(input('Enter the vertices with a space: ').split())

n, vertices, graph = len(vertex), dict(), []
for i in range(n): vertices[vertex[i]] = i

option = int(input('\n1. Directed Graph\n2.Undirected Graph\nEnter your choice: '))
if option == 1:
    while True:
        ls = input('Enter the vertices of an edge with weight or "done" to break: ').split()
        if ls != ['done']: graph.append([vertices[ls[0]], vertices[ls[1]], int(ls[2])])
        else: break
elif option == 2:
    while True:
        ls = input('Enter the vertices of an edge with weight or "done" to break: ').split()
        if ls != ['done']:
            graph.append([vertices[ls[0]], vertices[ls[1]], int(ls[2])])
            graph.append([vertices[ls[1]], vertices[ls[0]], int(ls[2])])
        else: break

def Bellman_Ford(source):
    nodes = [[float('inf'), ''] for i in range(n)]
    nodes[source][0] = 0

    for i in range(n - 1):
        # [[u, v, w], [u, v, w], [u, v, w]............] 
        for u, v, w in graph:
            if nodes[u][0] != float('inf') and nodes[v][0] > nodes[u][0] + w: nodes[v][0], nodes[v][1] = nodes[u][0] + w, u

    for u, v, w in graph:
        if nodes[u][0] != float('inf') and nodes[v][0] > nodes[u][0] + w:
            print('\n\nFor Node ' + vertex[source] + ':' + '\nNegative Cycle is detected in this Graph!')
            return

    print('\n\nFor Node ' + vertex[source] + ':' + '\n\tNode\tCost\tPath')

    for j, i in enumerate(nodes):
        itr, ls = i[1], [j]
        while(itr != ''):
            ls.append(itr)
            itr = nodes[itr][1]
        print('\t', vertex[j], '\t', i[0], end='\t')
        while(len(ls) > 1): print(vertex[ls.pop()], end=' -> ')
        print(vertex[ls.pop()])

for source in range(n): Bellman_Ford(source)