def bellmanFord(n, adjMatrix):
    def initDistances():    #initialize all node distances at infinity
        return [float('inf')] * n
    
    def printResults(results, n):   #print final distances per node
        for i, distance in enumerate(results):
            if distance is None:
                print(f"Node {i}: {[None] * n}")
            else:
                print(f"Node {i}: {distance}")
    
    results = []

    for node in range(n):
        #initialize distances for node
        distances = initDistances()
        distances[node] = 0

        for _ in range(n-1):    #run relaxation for each node
            for i in range(n):
                for j in range(n):
                    #if adjMatrix and distance is not inf, nodes are directly linked
                    if adjMatrix[i][j]!=float('inf') and distances[i]!=float('inf'):
                        newDistance = distances[i] + adjMatrix[i][j]
                        if newDistance<distances[j]:    #update distance if more efficient (shorter)
                            distances[j] = newDistance
        
        negCycle = False
        for i in range(n):
            for j in range(n):
                if adjMatrix[i][j]!=float('inf') and distances[i]!=float('inf'):
                    if distances[i] + adjMatrix[i][j] < distances[j]:
                        negCycle = True
                        break
            if negCycle:
                break
        
        if negCycle:
            results.append([None] * n)
        else:
            results.append([distance if distance != float('inf') else 'inf' for distance in distances])
        
    printResults(results, n)

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    n = int(data[0])
    
    if n<1 and n>50:
        print(f"Invalid input dimension: {n}. Min: 1\tMax: 50\n")

    adjMatrix = []

    for i in range(1, len(data)):
        value = data[i]
        if value == 'f':
            adjMatrix.append(float('inf'))
        else:
            adjMatrix.append(int(value))
    
    adjMatrix = [adjMatrix[i : i+n] for i in range(0, len(adjMatrix), n)]
    bellmanFord(n, adjMatrix)

if __name__ == '__main__':
    main()

