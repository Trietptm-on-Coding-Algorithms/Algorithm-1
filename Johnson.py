#!/usr/bin/python
#-*- coding:utf-8 -*-
#Johnson�㷨��ÿ�Խڵ����·��
#Dijkstra�㷨�Ǹ��ܺõķ��������ǲ������ߴ��ڣ����Խ��Bellman�㷨
#�跨�����еı߶���ɷǸ����趨һ���ڵ�s��s�����нڵ�ľ���Ϊ0����ʱ����Bellman�㷨
#���s�������ڵ�ľ��룬���¶���u��v��Ȩֵ����s��u�ľ����u��vȨֵ��ȥs��v����
#���s��v�����·������u��˵�����Ϊ�㣬������u��˵��d[u]+w(u,v)>d[v]
#�������·���ͻ�ѡ�񾭹�u������
#���һ���������б�Ȩֵ��Ϊ����������֮�����Թ�ϵû�б仯
#����Dijkstra�㷨�����·��ʱ���õ�����Ȩֵ�ĺͣ���������Ͳ�ṹ
#���Ľ����Ҫ +h[v]-h[u]�������һ�������һ��ʽ��

from copy import deepcopy

def johnson(G):
    G=deepcopy(G):
    s=object()
    G[s]={v:0 for v in G}
    #�������ڵ�
    h,_=bellman_ford(G,s)
    #����Bellman�㷨�����ظ��ڵ㵽s�ľ���
    #����и��߻��Զ�����
    del G[s]
    #ɾ���ڵ�
    for u in G:
        for v in G[u]:
            G[u][v]+=h[u]-h[v]
            #�趨��Ȩֵ
    D,P={},{}
    for u in G:
        D[u],P[u]=dijkstra(G,u)
        for v in G:
            D[u][v]+=h[v]-h[u]
            #���������
    return D,P
