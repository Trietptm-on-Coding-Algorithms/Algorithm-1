#!/usr/bin/python
#-*- coding:utf-8 -*-
#������������㷨

#�����塢�ݹ鷽ʽ
def rec_lis(seq):
    @memo
    def L(cur):
        #������Ԫ�أ�����֮ǰС�����Ľڵ���
        res=1
        for pre in range(cur):
        #��������֮ǰ��Ԫ��
            if seq[pre] <= seq[cur]:
                res=max(res,1+L(pre))
        return res
    return max(L(i) for i in range(len(seq)))


def basic_lis(seq):
    L=[1]*len(seq)
    #ԭʼ���У���¼��Ԫ��֮ǰ����������г���
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
