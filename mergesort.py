#!/usr/bin/python
#-*- coding:utf-8 -*-
#归并排序法
#递归分成两半，lft，rgt如果lft，rgt长度大于1，则还可以分，直到到递归终点，lft，rgt只有一个数
#比较lft，rgt大小，进行排序，然后将排序好的列表上传至上一级的lft，或rgt，上一级再次比较lft，rgt
#进行比较排序，然后上传结果，层层上传，直到回到最顶层
#排序重点是将两个排序好的两个列表合并，可以从两个列表最大的数，即最左边开始比较，较大的数加入res
#直到一个列表为空，说明不为空的那一个列表比res里面的数都小，返回合并列表(lft or rgt) + res


def mergesort(seq):
    mid=len(seq)/2
    lft,rgt=seq[:mid],seq[mid:]
    if len(lft)>1:lft=mergesort(lft)
    if len(rgt)>1:rgt=mergesort(rgt)
    res=[]
    while  lft and rgt:
        if lft[-1]>=rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res
