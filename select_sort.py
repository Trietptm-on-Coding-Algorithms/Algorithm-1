#!/usr/bin/python
#-*- coding:utf-8 -*-
#折半搜索

#分割函数
def parttion(seq):
    pi,seq=seq[0],seq[1:]
    #选取第一个为中间值
    lo=[x for x in seq if x<=pi]
    hi=[x for x in seq if x>pi]
    #根据中间值分割成两部分
    return lo,pi,hi

def select(seq,k):
    lo,pi,hi=parttion(seq)
    #分割序列
    m=len(lo)
    #前半部分长度
    if m==k:return pi
    #寻找前k小的数，如m=k则返回
    elif m<k:
        #如果m<k，说明前k小在右半部分
        return select(hi,k-m-1)
        #这是参数需减小，因为序列只取后半部分
    else:
        return select(lo,k)
