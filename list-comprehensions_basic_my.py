## 

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    mylist = [x,y,z]
    mylist.sort()
    outlist = []
    finallist = []
    
    
    for i in range(0,mylist[0]+1):
        for j in range(0,mylist[1]+1):
            for k in range(0,mylist[2]+1):
                templist = [i,j,k]
                if sum(templist) !=n:
                    outlist.append(templist)
                templist =[]
    print(outlist)
    
