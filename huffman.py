#!/usr/bin/python
#-*- coding:utf-8 -*-
#哈夫曼算法
from heapq import heapify,heappush,heappop
from itertools import count

def huffman(seq,frq):
    num=count()
    #创建无限迭代器，从0开始一直下去
    #当森林两棵树发生概率相同时，就遇到了不确定比较，所以我们再添加一个字段num，用它来区分所有对象
    trees=list(zip(frq,num,seq))
    #zip返回三元组
    heapify(trees)
    #将list变成堆
    while len(trees)>1:
        fa,_,a=heappop(trees)
        #选出堆中最小的元素
        fb,_,b=heappop(trees)
        n=next(num)
        #获取下一个计数值
        heappush(trees,(fa+fb,n,[a,b]))
        #将合并节点推入堆中
    return trees[0][-1]

