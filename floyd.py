#!/usr/bin/python
#-*- coding:utf-8 -*-
#ȷ������յ�󣬿��Ǿ����Ľڵ�
#�Ƿ񾭹��ڵ������̾���
def rec_floyd_warshall(G):
    @memo
    def d(u,v,k):
        if k==0:return G[u][v]
        return min(d(u,v,k-1),d(u,k,k-1)+d(k,v,k-1))
        #�ݹ�ѡ�������н�С��
    return {(u,v):d(u,v,len(G)) for u in G for v in G}

def floyd_warshall(G):
    D=deepcopy(G)
    for k in G:
    #�����Ľڵ�
        for u in G:
            for v in G:
                D[u][v]=min(D[u][v],D[u][k]+D[k][v])
    return D
