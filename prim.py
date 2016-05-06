#!/usr/bin/python
#-*- coding:utf-8 -*-
#Prim算法求最小生成树

from heapq import heappop,heappush

def prim(G,s):
    P,Q={},[(0,None,s)]
    #P储存生成树中已有的节点，Q为储存现有节点所有邻居的堆
    while Q:
        _,p,u=heappop(Q)
        #取出到现有生成树最短的节点
        if u in P:continue
        #如果该节点已在生成树中，则跳过，否则会形成环
        P[u]=p
        #记录在生成树中
        for v,w in G[u].items():
            #添加此节点所有邻居到堆中
            heappush(Q,(w,u,v))
    return P
