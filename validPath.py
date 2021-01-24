
def solve(x, y, n, r, cx, cy):
    global circle
    circle=[]
    for i in range(x+1):
        circle.append([0]*(y+1))
    for i in range(n):
        cr,cc=cx[i],cy[i]
        circle[cr][cc]=1
        if(cr>=r):
            strtx=cr-r
        else:
            strtx=0
        if(cc>=r):
            strty=cc-r
        else:
            strty=0
        if(x>=cr+r):
            endx=cr+r
        else:
            endx=x
        if(y>=cc+r):
            endy=cc+r
        else:
            endy=y
        for j in range(strtx,endx+1):
            circle[j][strty:endy+1]=[1]*(endy-strty+1)
    return isPathExists(0,0,x,y)

def isPathExists(strtx,strty,endx,endy):
    
    visited[strtx][strty]=1
    
    if circle[strtx][strty]==1 or circle[endx][endy]==1:
        return False
    if strtx==endx and strty==endy:
        path.append((strtx,strty))
        return True
    #BR    
    if strtx<=endx-1 and strty<=endy-1 and visited[strtx+1][strty+1]==0:
        res=isPathExists(strtx+1,strty+1,endx,endy)
        if res:
            path.append((strtx,strty))
            return res
    #R
    if strty<=endy-1 and visited[strtx][strty+1]==0:
        res=isPathExists(strtx,strty+1,endx,endy)
        if res:
            path.append((strtx,strty))
            return res
    #B
    if strtx<=endx-1 and visited[strtx+1][strty]==0:
        res=isPathExists(strtx+1,strty,endx,endy)
        if res:
            path.append((strtx,strty))
            return res
    #TR
    if strtx>=1 and strty<=endy-1 and visited[strtx-1][strty+1]==0:
        res=isPathExists(strtx-1,strty+1,endx,endy)
        if res:
            path.append((strtx,strty))
            return res
    #T
    if strtx>=1 and visited[strtx-1][strty]==0:
        res=isPathExists(strtx-1,strty,endx,endy)
        if res:
            path.append((strtx,strty))
            return res
    #TL
    if strtx>=1 and strty>=1 and visited[strtx-1][strty-1]==0:
        res=isPathExists(strtx-1,strty-1,endx,endy)
        if res:
            path.append((strtx,strty))
            return res
    #L
    if strty>=1 and visited[strtx][strty-1]==0:
        res=isPathExists(strtx,strty-1,endx,endy)
        if res:
            path.append((strtx,strty))
            return res
    #BL
    if strtx<=endx-1 and strty>=1 and visited[strtx+1][strty-1]==0:
        res=isPathExists(strtx+1,strty-1,endx,endy)
        if res:
            path.append((strtx,strty))
            return res
    
    return False

x,y,N,R=map(int,input().rstrip().split())
A=list(map(int,input().rstrip().split()))
B=list(map(int,input().rstrip().split()))
path=[]
visited=[[0 for j in range(y+1)] for i in range(x+1)]

print(solve(x,y,N,R,A,B))
print(path[::-1])
