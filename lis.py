#!/usr/bin/python
#-*- coding:utf-8 -*-
#最长递增子序列算法

#记忆体、递归方式
def rec_lis(seq):
    @memo
    def L(cur):
        #传入与元素，计算之前小于它的节点数
        res=1
        for pre in range(cur):
        #迭代在其之前的元素
            if seq[pre] <= seq[cur]:
                res=max(res,1+L(pre))
        return res
    return max(L(i) for i in range(len(seq)))


def basic_lis(seq):
    L=[1]*len(seq)
    #原始序列，记录各元素之前的最长递增序列长度
    for cur,val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] <= val:
                L[cur]=max(L[cur],1+L[pre])
    return max(L)

from bisect import bisect

def lis(seq):
    end=[]
    for val in seq:
        idx = bisect(end,val)
        if idx==len(end):end.append(val)
        else:
            end[idx]=val
    return len(end)
