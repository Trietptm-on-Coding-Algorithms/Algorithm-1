#!/usr/bin/python
#-*- coding:utf-8 -*-
#�����������㷨
#����defaultdict���п�������


from collections import defaultdict
def counting_sort(A,key=lambda x:x):
    B,C=[],defaultdict(list)
    #���������б�A������defaultdict(list)�ֵ䣬������벻���ڵ�key���򷵻�[]
    for x in A:
        C[key(x)].append(x)
        #��ÿ���������ֵ䣬key:value��Ϊ�����ֵ
    for k in range(min(C),max(C)+1):
        #����С��key��ʼ���Ի�ȡ�ֵ��ڵ�value�����������key������[]
        B.extend(C[k])
        #����õ�������[]�ϲ���B��������ӵ�˳���Ǵ�С�����
    return B

print counting_sort([1234,3546,657])
