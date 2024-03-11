from collections import defaultdict

def learningLanguage():
    graph = defaultdict(list)
    seen = set()
    count = 0

    for i in range(n):
        item = array[i]
        if not item:
            count += 1
        else:
            for k in item:
                for v in item:
                    graph[k].append(v)
                    graph[v].append(k)


    def dfs(node):
        if node in seen:
            return 
        seen.add(node)

        for neigh in graph[node]:  
            dfs(neigh)

    for k in graph:
        if k not in seen:
            dfs(k)
            count += 1

    return count if not seen else count - 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    array = []

    for i in range(n):
        array.append(list(map(int, input().split()))[1:])
    
    print(learningLanguage())

