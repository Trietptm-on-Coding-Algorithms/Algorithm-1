#!/usr/bin/python
#-*- coding:utf-8 -*-
#选择排序递归版和迭代版
#第一次递归前，针对整个序列，设置max_j，与所有数比较找出最大值，并将最大值放在最右边
#之后递归调用，寻找前i-1个数中的最大值，并放在最右边，持续递归，直到检测序列变为1，即第一个数

#递归版
def sel_sort_rec(seq,i):
    if i==0:return
    max_j=i
    for j in range(i):
        if seq[j]>seq[max_j]:max_j=j
    seq[i],seq[max_j]=seq[max_j],seq[i]
    sel_sort_rec(seq,i-1)

#迭代版
def sel_sort(seq):
    for i in range(len(seq)-1,0,-1):
    #从seq长度开始，每步减少1，直至为0
        max_j=i
        #开始针对前i个数执行排序，找出最大值放在最右边
        for j in range(i):
            if seq[j]>seq[max_j]:max_j=i
        seq[i],seq[max_j]=seq[max_j],seq[i]

sel_sort_rec([123,5346,657,89,435,65],5)
