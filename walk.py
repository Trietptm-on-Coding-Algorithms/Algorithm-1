#!/usr/bin/python
#-*- coding:utf-8 -*-
#遍历一个表示为邻接集的图结构的连通分量
#从某一个节点开始，添加其邻居，迭代邻居，重复步骤，遍历连通分量

def walk(G,s,S=set()):
    #从节点s开始
    P,Q=dict().set()
    P=None
    Q.add(s)
    #Q为需要遍历的节点
    while Q:
        u=Q.pop()
        #取出节点
        for v in G[u].difference(P,S):
        #u的邻居与访问过的节点列表求差，即存在G[u]中不存在P中的，此为可以添加构成连通分量的节点
            Q.add(v)
            #将该节点加入Q，之后会遍历此节点
            P[v]=u
            #记录前趋节点
    return P
