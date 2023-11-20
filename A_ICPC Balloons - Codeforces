def icpc_balloons():
    hashmap = {}
 
    for i in range(len(string)):
        if string[i] not in hashmap:
            hashmap[string[i]] = 2
        
        else:
            hashmap[string[i]] += 1
 
    res = 0
 
    for k, v in hashmap.items():
        res += v
 
    return res
 
 
if __name__ == '__main__':
    t = int(input())
 
    for _ in range(t):
        n = int(input())
        string = input()
 
        print(icpc_balloons())
