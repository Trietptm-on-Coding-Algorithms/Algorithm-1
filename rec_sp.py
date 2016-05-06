#!/usr/bin/python
#-*- coding:utf-8 -*-

def rec_dag_sp(W,s,t):
    @memo
    def d(u):
        if u == t:return 0
        return min(W[u][v]+d(v) for v in W[u])
    return d(s)

def dag_sp(W,s,t):
    d={u:float('inf') for u in W}
    d[s]=0
    for u in topsort(W):
        if u == t:break
        for v in W[u]:
            d[v]=min(d[v],d[u]+W[u][v])
    return d[t]
