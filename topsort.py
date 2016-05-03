#!/usr/bin/python
#-*- coding:utf-8 -*-
#拓扑排序算法
#采用计数器计算依赖数目，找出不需要任何依赖的节点，并剔除，将依赖此节点的依赖数目减1
#再次查找依赖为0的节点，因为是有向非环路图，所以每次剔除后都会有无依赖的节点，否则必定成环

def topsort(G):
    count=dict((u,0) for u in G)
    #创建计数器u=0
    for u in G:
        for v in G[u]:
            count[v]+=1
            #初始化计数器，计算每个节点依赖数目
    Q=[u for u in G if count[u]==0]
    #需找不需要依赖的节点
    S=[]
    while Q:
        u= Q.pop()
        S.append(u)
        #加入节点
        for v in G[u]:
            #迭代依赖该节点的节点
            count[v]-=1
            #将其计数都减1
            if count[v]==0:
                #如果节点变为不需要依赖
                Q.append(v)
    return S
