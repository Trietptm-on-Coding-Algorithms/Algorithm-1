#!/usr/bin/python
#-*- coding:utf-8 -*-
#Bellman-Ford�㷨�����·��
def bellman_ford(G,s):
    D,P={s:0},{}
    for rnd in G:
    #���ѭ��n�ο��ɳ����
        changed=False
        for u in G:
            for v in G[u]:
                #�������нڵ㣬���ÿ���ڵ㣬����relax�������������ھӽ����ɳ�
                if relax(G,u,v,D,P):
                    changed=True
                    #����ɳڳɹ���changed=True
        if not changed:break
        #���û�иı䣬��˵��ͼ�Ѿ��ɳ����
    else:
        raise ValueError
        #��ѭ����n�λ��Ǳ仯����˵�����ڸ���������ִ��else����
    return D,P
