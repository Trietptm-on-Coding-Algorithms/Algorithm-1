#!/usr/bin/python
#-*- coding:utf-8 -*-
#二分搜索算法
#该算法针对某一已经排序的序列
def bisect_right(a,x,lo=0,hi=None):
    if hi in None:
        hi=len(a)
    while lo<hi:
        mid=(lo+hi)/2
        #需要进行比较的中间值
        if x<a[mid]:hi=mid
        #如果x小于中间值，就需要搜寻左半部分
        else:lo=mid+1
    return lo
