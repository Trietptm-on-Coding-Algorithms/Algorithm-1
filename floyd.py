#!/usr/bin/python
#-*- coding:utf-8 -*-
#确定起点终点后，考虑经过的节点
#是否经过节点能缩短距离
def rec_floyd_warshall(G):
    @memo
    def d(u,v,k):
        if k==0:return G[u][v]
        return min(d(u,v,k-1),d(u,k,k-1)+d(k,v,k-1))
        #递归选择两者中较小的
    return {(u,v):d(u,v,len(G)) for u in G for v in G}

def floyd_warshall(G):
    D=deepcopy(G)
    for k in G:
    #经过的节点
        for u in G:
            for v in G:
                D[u][v]=min(D[u][v],D[u][k]+D[k][v])
    return D
