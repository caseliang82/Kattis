# we use a breadth-first search to find the shortest path
# than find the most of the items we can collect.
def search(nol,noi,nor,rdwt):
    explored = [[1]]
    goal = nol
    rdwt.sort()
    path = []
    
    for n in range(n):
        
        path = []
        for rdw in rdwt:
            if rdw[0] == expld[-1]:
                path.append(expld+[rdw[1]])
        explored = path
    print(explored)
        
                
    
    
    
def main():
    # prepare input
    nol = int(input()) # number of locations in the city
    noi = [int(n) for n in input().split()] # number of items on each location
    nor = int(input()) # number of roads
    rdwt = []
    for i in range(nor):
        rdwt.append([int(n) for n in input().split()])
    
#     print(rdwt)
    # search all the path
    shortestPath = search(nol,noi,nor,rdwt)

main()

