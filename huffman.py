#!/usr/bin/python
#-*- coding:utf-8 -*-
#�������㷨
from heapq import heapify,heappush,heappop
from itertools import count

def huffman(seq,frq):
    num=count()
    #�������޵���������0��ʼһֱ��ȥ
    #��ɭ������������������ͬʱ���������˲�ȷ���Ƚϣ��������������һ���ֶ�num���������������ж���
    trees=list(zip(frq,num,seq))
    #zip������Ԫ��
    heapify(trees)
    #��list��ɶ�
    while len(trees)>1:
        fa,_,a=heappop(trees)
        #ѡ��������С��Ԫ��
        fb,_,b=heappop(trees)
        n=next(num)
        #��ȡ��һ������ֵ
        heappush(trees,(fa+fb,n,[a,b]))
        #���ϲ��ڵ��������
    return trees[0][-1]

#�ӹ�����������ȡ����������
def codes(tree,prefix=""):
    if len(tree)==1:
        yield (tree,prefix)
        #��������tree����Ϊ�㣬��ôΪҶ�ڵ㣬���ر��뼰ǰ׺��
        return
    for bit,child in zip("01",tree):
        for pair in codes(child,prefix+bit):
            yield pair
