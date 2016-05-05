#!/usr/bin/python
#-*- coding:utf-8 -*-
#Kruskal�㷨����С������

#�ҵ�ָ��Ľڵ�
def find(C,u):
    if C[u]!=u:
        #�����ָ��ڵ��Լ�
        C[u]=find(C,C[u])
        #�ݹ����
    return C[u]

#�ϲ�������ͼ
def union(C,R,u,v):
    u,v=find(C,u),find(C,v)
    if R[u]>R[v]:
    #�ȽϹ�ģ��С
        C[v]=u
    else:
        C[u]=v
    if R[u]==R[v]:
    #����ͬ��ģ��ͼ�ϲ���v��ģ����
        R[v]+=1

def kruskal(G):
    E=[(G[u][v],u,v) for u in G for v in G[u]]
    #Ȩ���б�
    T=set()
    C,R={u:u for u in G},{U:0 for u in G}
    #C��¼ָ��Ľڵ㣬R��¼��ͼ��ģ����
    for _,u,v in sorted(E):
        #��Ȩ�ش�С�������б�
        if find(C,u)!=find(C,v):
            T.add((u,v))
            union(C,R,u,v)
    return T
