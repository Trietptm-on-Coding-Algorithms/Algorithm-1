#!/usr/bin/python
#-*- coding:utf-8 -*-
#Kruskal算法求最小生成树

#找到指向的节点
def find(C,u):
    if C[u]!=u:
        #如果不指向节点自己
        C[u]=find(C,C[u])
        #递归查找
    return C[u]

#合并两个子图
def union(C,R,u,v):
    u,v=find(C,u),find(C,v)
    if R[u]>R[v]:
    #比较规模大小
        C[v]=u
    else:
        C[u]=v
    if R[u]==R[v]:
    #两个同规模子图合并，v规模增加
        R[v]+=1

def kruskal(G):
    E=[(G[u][v],u,v) for u in G for v in G[u]]
    #权重列表
    T=set()
    C,R={u:u for u in G},{U:0 for u in G}
    #C记录指向的节点，R记录子图规模级别
    for _,u,v in sorted(E):
        #按权重大小迭代所有边
        if find(C,u)!=find(C,v):
            T.add((u,v))
            union(C,R,u,v)
    return T
