#!/usr/bin/python
#-*- coding:utf-8 -*-
#ѡ������ݹ��͵�����
#��һ�εݹ�ǰ������������У�����max_j�����������Ƚ��ҳ����ֵ���������ֵ�������ұ�
#֮��ݹ���ã�Ѱ��ǰi-1�����е����ֵ�����������ұߣ������ݹ飬ֱ��������б�Ϊ1������һ����

#�ݹ��
def sel_sort_rec(seq,i):
    if i==0:return
    max_j=i
    for j in range(i):
        if seq[j]>seq[max_j]:max_j=j
    seq[i],seq[max_j]=seq[max_j],seq[i]
    sel_sort_rec(seq,i-1)

#������
def sel_sort(seq):
    for i in range(len(seq)-1,0,-1):
    #��seq���ȿ�ʼ��ÿ������1��ֱ��Ϊ0
        max_j=i
        #��ʼ���ǰi����ִ�������ҳ����ֵ�������ұ�
        for j in range(i):
            if seq[j]>seq[max_j]:max_j=i
        seq[i],seq[max_j]=seq[max_j],seq[i]

sel_sort_rec([123,5346,657,89,435,65],5)
