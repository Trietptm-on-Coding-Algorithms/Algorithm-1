#!/usr/bin/python
#-*- coding:utf-8 -*-
#�����������
#BFS�㷨������IDDFS���׵öֻ࣬��Ҫ�����Ƚ��ȳ��Ķ������ͼ���
#��ʵ�ϣ���DFSΨһ������������ǽ�LIFO�Ƚ�����滻��FIFO�Ƚ��ȳ����ȷ��ʵ��Ľڵ���������

def bfs(G,s):
    P,Q={s:None},deque([s])
    #P��¼���ʹ��Ľڵ㣬dequeΪ˫����У��Ƚ��ȳ�̽���ڵ�
    while Q:
        u=Q.popleft()
        #ȡ���ڵ�
        for v in G[u]:
            #�������ھ�
            if v in P:continue
            P[v]=u
            #��¼ǰ���Ӵ���
            Q.append(v)
            #��ӵ���������
        return P
