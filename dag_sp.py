#!/usr/bin/python
#-*- coding:utf-8 -*-
#DAG最短路径算法

#运用递归、记忆体化的方式
def rec_dag_sp(W,s,t):
    @memo
    #d函数计算节点到终点的最短距离
    def d(u):
        if u == t:return 0
        return min(W[u][v]+d(v) for v in W[u])
        #返回当前节点到邻居的距离加邻居到终点的距离的最小值
        #每次递归返回都能保证返回的是节点到终点的最短距离
    return d(s)

#迭代版算法
#先拓扑排序，由此保证使用当前节点的时候，d(u)为u的最短路径
#因为依据拓扑排序，需要走遍所有到u的路径，才会迭代节点u
#通过每条路径遍历所有节点，设定起点离自己的距离为0，首先遍历时会设定距离起点的距离
#之后通过其他路径访问时会比较d(v)与d(u)+w[u][v]，选择更小的更新距离
def dag_sp(W,s,t):
    d={u:float('inf') for u in W}
    #每个节点到起点的距离
    d[s]=0
    for u in topsort(W):
        if u == t:break
        #迭代到了终点t,说明到达t的所有路径都已经被松弛
        for v in W[u]:
            d[v]=min(d[v],d[u]+W[u][v])
            #开始松弛化u的所有邻居
    return d[t]

#当节点没有入边时才会迭代该节点，所以迭代时
#到达其的所有边都被松弛，此时的d肯定为最短距离
