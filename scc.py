#!/usr/bin/python
#-*- coding:utf-8 -*-
#Kosaraju查找强连通分量算法
#强连通分量间有单方向边线相连，分量之间也可视为某种依赖关系，如果在一节点中使用之前的walk函数遍历连通分量
#则可以到达它指向的另一分量，而无法到达它前面的分量，可以设想一种方法，就是从将各分量间的边线翻转，从最前面的分量开始遍历
#这样就不会到达下一个分量，然后在遍历下一个分量，每次都只遍历完一个分量，可以对原始图使用之前基于深度优先搜索的拓扑排序
#虽然这里的图有环，但是各分量间的边线关系不变，根据遍历的顺序，可得到图的伪拓朴排序

#翻转图所有边线
def tr(G):
    GT={}
    for u in G:GT[u]=set()
    for u in G:
        for v in G[u]:
            GT[v].add(u)
        return GT

#Kosaraju查找强连通分量算法
def scc(G):
    GT=tr(G)
    #翻转所有边线
    sccs,seen=[],set()
    for u in dfs_topsort(G):
    #进行拓扑排序，迭代最前面的分量
    #无论从最前面分量的哪个节点开始，都可以遍历分量中的所有节点，因为其强连通
        if u in seen:continue
        #如果该分量中节点已经遍历过，则跳过
        C=walk(GT,u.seen)
        seen.update(C)
        #记录遍历完的节点
        sccs.append(C)
        #添加强连通分量
    return sccs
