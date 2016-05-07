#!/usr/bin/python
#-*- coding:utf-8 -*-
from collections import deque
inf=float('inf')

#Â·¾¶Ñ°ÕÒº¯Êý
def bfs_aug(G,H,s,t,f):
    P,Q,F={s:None},deque([s]),{s:inf}
    def label(inc):
        if v in P or inc<=0:return
        F[v],P[v]=min(F[u],inc),u
        Q.append(v)
    while Q:
        u=Q.popleft()
        if u==t:return P,F[t]
        for v in G[u]:label(G[u][v]-f[u,v])
        #Ñ°ÕÒÇ°½ø±ß
        for v in H[u]:label(f[v,u])
        #ºóÍË±ß
    return None,0

from collections import defaultdict

def ford_fulkerson(G,s,t,aug=bfs_aug):
    H,f=tr(G),defaultdict(int)
    while True:
        P,c=aug(G,H,s,t,f)
        if c==0:return f
        u=t
        while u!=s:
            u,v=P[u],u
            if v in G[u]:f[u,v]+=c
            else:f[v,u]-=c
