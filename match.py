#!/usr/bin/python
#-*- coding:utf-8 -*-
#通过增广路径算法寻找最大双边匹配
#迭代所有节点，开始探查，如果发现右边有没匹配的点，则中止循环进行匹配
#forw生成可前进的路径，back生成后退的路径
#左边迭代所有前进的路径，加入循环堆，循环到右边节点，寻找后退路径
#直到推到左边，找到一个未匹配的右边节点，中止循环，更改这条路径上的所有匹配

from itertools import chain

def match(G,X,Y):
    H=tr(G)
    S,T,M=set(X),set(Y),set()
    #左边节点集，右边节点集，已匹配集合
    while S:
        s=S.pop()
        Q,P={s},{}
        while Q:
            u=Q.pop()
            if u in T:
                #如果u还没有在T中，说明没有被配对
                T.remove(u)
                #移除u
                break
            forw=(v for v in G[u] if (u,v) not in M)
            back=(v for v in H[u] if (v,u) in M)
            #前进及后退路径
            for v in chain(forw,back):
            #chian将两个列表组合迭代
                if v in P:continue
                P[v]=u
                Q.add(v)
        while u != s:
            u,v=P[u],u
            #迭代寻找到的路径边集
            if v in G[u]:
                M.add((u,v))
                #如果v在左边，添加边，否则移除边
            else:
                M.remove((v,u))
    return M

#使用带标记的遍历寻找增广路径，并对不相交的路径进行计数
#从起点经过一条路径到达终点，计数增加1，之后从另一条路出发
#到达某个路口，发现路被前面那条占用，这是forw为空，迭代back返回路径
#返回前面路径的上一路口，如发现有forw前进路径，则沿着新路径到达终点
#改变两条路的线路，增加计数
def paths(G,s,t):
    H,M,count=tr(G),set(),0
    while True:
        Q,P={s},{}
        while Q:
            u=Q.pop()
            if u==t:
                count+=1
                break
            forw=(v for v in G[u] if (u,v) not in M)
            back=(v for v in H[u] if (v,u) in M)
            for v in chain(forw,back):
                if v in P:continue
                P[v]=u
                Q.add(v)
        else:
            #循环结束，也就是无法再找到增广路径
            return count
        while u!=s:
            u,v=P[u],u
            if v in G[u]:
                M.add((u,v))
            else:
                M.remove((v,u))
