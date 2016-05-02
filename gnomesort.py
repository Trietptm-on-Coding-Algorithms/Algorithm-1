#!/usr/bin/python
#-*- coding:utf-8 -*-
#侏儒排序法
#从序列最左边开始，引索i递增，如发现前一个前一个seq[i-1]比后一个seq[i]大，就将这两个数前后调换
#i减小1，比较前一个数与现在这数的大小，如果还是前面大于后面，则继续调换，一直将该数调到适合的位置
#每次碰到乱序，则将该数一直往前面调，直到找到合适位置，这样每次调整下一个乱序时，总能保证前面已经排好顺序


def gnomesort(seq):
    i=0
    while i<len(seq):
        if  i == 0 or seq[i-1]<=seq[i]:
            i+=1
        else:
            seq[i],seq[i-1]=seq[i-1],seq[i]
            i-=1
