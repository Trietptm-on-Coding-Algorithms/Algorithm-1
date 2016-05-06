#!/usr/bin/python
#-*- coding:utf-8 -*-
#Johnson算法求每对节点最短路径
#Dijkstra算法是个很好的方案，但是不允许负边存在，所以结合Bellman算法
#设法将所有的边都变成非负，设定一个节点s，s到所有节点的距离为0，此时调用Bellman算法
#求出s到各个节点的距离，重新定义u到v的权值，用s到u的距离加u、v权值减去s到v距离
#如果s到v的最短路径经过u，说明结果为零，不经过u，说明d[u]+w(u,v)>d[v]
#否则最短路径就会选择经过u的那条
#如此一来，将所有边权值变为正数，但其之间的相对关系没有变化
#利用Dijkstra算法求最短路径时，得到是新权值的和，类似于套筒结构
#最后的结果需要 +h[v]-h[u]，处理第一个和最后一个式子

from copy import deepcopy

def johnson(G):
    G=deepcopy(G):
    s=object()
    G[s]={v:0 for v in G}
    #添加虚拟节点
    h,_=bellman_ford(G,s)
    #运行Bellman算法，返回各节点到s的距离
    #如果有负边会自动报错
    del G[s]
    #删除节点
    for u in G:
        for v in G[u]:
            G[u][v]+=h[u]-h[v]
            #设定新权值
    D,P={},{}
    for u in G:
        D[u],P[u]=dijkstra(G,u)
        for v in G:
            D[u][v]+=h[v]-h[u]
            #处理最后结果
    return D,P
