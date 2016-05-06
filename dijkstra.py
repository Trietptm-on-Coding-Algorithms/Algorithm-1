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
