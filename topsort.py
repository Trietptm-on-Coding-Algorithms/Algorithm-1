#!/usr/bin/python
#-*- coding:utf-8 -*-
#���������㷨
#���ü���������������Ŀ���ҳ�����Ҫ�κ������Ľڵ㣬���޳����������˽ڵ��������Ŀ��1
#�ٴβ�������Ϊ0�Ľڵ㣬��Ϊ������ǻ�·ͼ������ÿ���޳��󶼻����������Ľڵ㣬����ض��ɻ�

def topsort(G):
    count=dict((u,0) for u in G)
    #����������u=0
    for u in G:
        for v in G[u]:
            count[v]+=1
            #��ʼ��������������ÿ���ڵ�������Ŀ
    Q=[u for u in G if count[u]==0]
    #���Ҳ���Ҫ�����Ľڵ�
    S=[]
    while Q:
        u= Q.pop()
        S.append(u)
        #����ڵ�
        for v in G[u]:
            #���������ýڵ�Ľڵ�
            count[v]-=1
            #�����������1
            if count[v]==0:
                #����ڵ��Ϊ����Ҫ����
                Q.append(v)
    return S
