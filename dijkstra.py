#!/usr/bin/python
#-*- coding:utf-8 -*-
#Dijkstra算法寻找最短路径
#从s开始，将其与邻居的距离及邻居二元组推入堆
#每次选择最小的节点松弛其所有邻居，推入堆，重复步骤
#这样选择能保证选择节点时节点已经是最优化
#因为选择它时，它在所有路径中最短，此时别的节点路径还不确定
#因为可能通过该路径去到节点的路径更短，还能松弛，而反过来却不成立
#每次选择最小的，能保证已松弛完毕

from heapq import heappush,heappop

def dijkstra(G,s):
    D,P,Q,S = {s:0},{},[(0,s)],set()
    #D记录节点到起点的距离，P记录前趋节点，Q为节点堆，S记录访问过的节点
    while Q:
        _,u=heappop(Q)
        if u in S:continue
        S.add(u)
        for v in G[u]:
        #松弛u所有出边
            relax(G,u,v,D,P)
            heappush(Q,(D[v],v))
            #推入堆
    return D,P

#将上述代码增加yiled，变成生成器，实现双向算法
def bidir_dijkstra(G,s,t):
    Ds,Dt={},{}
    forw,back=idijkstra(G,s),idijkstra(G,t)
    dirs=(Ds,Dt,forw),(Dt,Ds,back)
    try:
        for D,other,step in cycle(dirs):
            v,d=next(step)
            D[v]=d
            if v in other:break
    except StopIteration:return inf
    m=inf
    #可能存在更短的路径，需要检查
    for u in Ds:
        for v in G[u]:
            if not v in Dt:continue
            m=min(m,Ds[u]+G[u][v]+Dt[v])
    return m
