#!/usr/bin/python
#-*- coding:utf-8 -*-
#Prim�㷨����С������

from heapq import heappop,heappush

def prim(G,s):
    P,Q={},[(0,None,s)]
    #P���������������еĽڵ㣬QΪ�������нڵ������ھӵĶ�
    while Q:
        _,p,u=heappop(Q)
        #ȡ����������������̵Ľڵ�
        if u in P:continue
        #����ýڵ������������У���������������γɻ�
        P[u]=p
        #��¼����������
        for v,w in G[u].items():
            #��Ӵ˽ڵ������ھӵ�����
            heappush(Q,(w,u,v))
    return P
