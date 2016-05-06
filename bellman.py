#!/usr/bin/python
#-*- coding:utf-8 -*-
#Bellman-Ford算法求最短路径
def bellman_ford(G,s):
    D,P={s:0},{}
    for rnd in G:
    #最多循环n次可松弛完毕
        changed=False
        for u in G:
            for v in G[u]:
                #迭代所有节点，针对每个节点，调用relax函数对其所有邻居进行松弛
                if relax(G,u,v,D,P):
                    changed=True
                    #如果松弛成功，changed=True
        if not changed:break
        #如果没有改变，则说明图已经松弛完毕
    else:
        raise ValueError
        #当循环了n次还是变化，就说明存在负环，这是执行else部分
    return D,P
