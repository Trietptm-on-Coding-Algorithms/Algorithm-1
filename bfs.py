#!/usr/bin/python
#-*- coding:utf-8 -*-
#广度优先搜索
#BFS算法遍历比IDDFS容易得多，只需要采用先进先出的队列类型即可
#事实上，与DFS唯一显著的区别就是将LIFO先进后出替换成FIFO先进先出，先访问到的节点率先搜索

def bfs(G,s):
    P,Q={s:None},deque([s])
    #P记录访问过的节点，deque为双向队列，先进先出探索节点
    while Q:
        u=Q.popleft()
        #取出节点
        for v in G[u]:
            #迭代其邻居
            if v in P:continue
            P[v]=u
            #记录前趋接待能
            Q.append(v)
            #添加到搜索队列
        return P
