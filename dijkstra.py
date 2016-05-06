#!/usr/bin/python
#-*- coding:utf-8 -*-
#Dijkstra�㷨Ѱ�����·��
#��s��ʼ���������ھӵľ��뼰�ھӶ�Ԫ�������
#ÿ��ѡ����С�Ľڵ��ɳ��������ھӣ�����ѣ��ظ�����
#����ѡ���ܱ�֤ѡ��ڵ�ʱ�ڵ��Ѿ������Ż�
#��Ϊѡ����ʱ����������·������̣���ʱ��Ľڵ�·������ȷ��
#��Ϊ����ͨ����·��ȥ���ڵ��·�����̣������ɳڣ���������ȴ������
#ÿ��ѡ����С�ģ��ܱ�֤���ɳ����

from heapq import heappush,heappop

def dijkstra(G,s):
    D,P,Q,S = {s:0},{},[(0,s)],set()
    #D��¼�ڵ㵽���ľ��룬P��¼ǰ���ڵ㣬QΪ�ڵ�ѣ�S��¼���ʹ��Ľڵ�
    while Q:
        _,u=heappop(Q)
        if u in S:continue
        S.add(u)
        for v in G[u]:
        #�ɳ�u���г���
            relax(G,u,v,D,P)
            heappush(Q,(D[v],v))
            #�����
    return D,P

#��������������yiled�������������ʵ��˫���㷨
def bidir_dijkstra(G,s,t):
    Ds,Dt={},{}
    forw,back=idijkstra(G,s),idijkstra(G,t)
    dirs=(Ds,Dt,forw),(Dt,Ds,back)
    try:
        for D,other,step in cycle(dirs):
            v,d=next(step)
            D[v]=d
            if v in other:break
    except StopIteration:return inf
    m=inf
    #���ܴ��ڸ��̵�·������Ҫ���
    for u in Ds:
        for v in G[u]:
            if not v in Dt:continue
            m=min(m,Ds[u]+G[u][v]+Dt[v])
    return m
