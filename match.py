#!/usr/bin/python
#-*- coding:utf-8 -*-
#ͨ������·���㷨Ѱ�����˫��ƥ��
#�������нڵ㣬��ʼ̽�飬��������ұ���ûƥ��ĵ㣬����ֹѭ������ƥ��
#forw���ɿ�ǰ����·����back���ɺ��˵�·��
#��ߵ�������ǰ����·��������ѭ���ѣ�ѭ�����ұ߽ڵ㣬Ѱ�Һ���·��
#ֱ���Ƶ���ߣ��ҵ�һ��δƥ����ұ߽ڵ㣬��ֹѭ������������·���ϵ�����ƥ��

from itertools import chain

def match(G,X,Y):
    H=tr(G)
    S,T,M=set(X),set(Y),set()
    #��߽ڵ㼯���ұ߽ڵ㼯����ƥ�伯��
    while S:
        s=S.pop()
        Q,P={s},{}
        while Q:
            u=Q.pop()
            if u in T:
                #���u��û����T�У�˵��û�б����
                T.remove(u)
                #�Ƴ�u
                break
            forw=(v for v in G[u] if (u,v) not in M)
            back=(v for v in H[u] if (v,u) in M)
            #ǰ��������·��
            for v in chain(forw,back):
            #chian�������б���ϵ���
                if v in P:continue
                P[v]=u
                Q.add(v)
        while u != s:
            u,v=P[u],u
            #����Ѱ�ҵ���·���߼�
            if v in G[u]:
                M.add((u,v))
                #���v����ߣ���ӱߣ������Ƴ���
            else:
                M.remove((v,u))
    return M

#ʹ�ô���ǵı���Ѱ������·�������Բ��ཻ��·�����м���
#����㾭��һ��·�������յ㣬��������1��֮�����һ��·����
#����ĳ��·�ڣ�����·��ǰ������ռ�ã�����forwΪ�գ�����back����·��
#����ǰ��·������һ·�ڣ��緢����forwǰ��·������������·�������յ�
#�ı�����·����·�����Ӽ���
def paths(G,s,t):
    H,M,count=tr(G),set(),0
    while True:
        Q,P={s},{}
        while Q:
            u=Q.pop()
            if u==t:
                count+=1
                break
            forw=(v for v in G[u] if (u,v) not in M)
            back=(v for v in H[u] if (v,u) in M)
            for v in chain(forw,back):
                if v in P:continue
                P[v]=u
                Q.add(v)
        else:
            #ѭ��������Ҳ�����޷����ҵ�����·��
            return count
        while u!=s:
            u,v=P[u],u
            if v in G[u]:
                M.add((u,v))
            else:
                M.remove((v,u))
