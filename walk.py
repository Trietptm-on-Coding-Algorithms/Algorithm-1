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

#walk函数遍历的只是单个连通分量，由开始节点s决定，所以将其封装在一个涉及所有节点的循环中
#定义一个访问过的节点，包括已找出的连通分量的所有节点，避免重复操作
def components(G):
    comp=[]
    #保存已有连通分量
    seen=set()
    #访问过的节点
    for u in G:
        if u in seen:continue
        #如果该节点已经访问过
        C=walk(G,u)
        #传入节点u，从u开始遍历连通分量
        seen.update(C)
        #将列表C所有元素加入集合seen
        comp.append(C)
        #将该次获得的连通分量添加到comp
    return comp
