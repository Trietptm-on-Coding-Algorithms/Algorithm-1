#!/usr/bin/python
#-*- coding:utf-8 -*-
#��������ݹ���������
#�㷨ʵ�ֹ�����٪���㷨���ƣ�Ҳ�Ƿ���ǰһ�����ں�һ�����򽫺��ߵ�����ǰ�����λ��
#����ʽ�ݹ���ã�ÿ��ֻ��עǰi�����֣����ﵽ�յ�Ҳ����i=1ʱ����ʼ���ϼ����ݣ���Ըò��ע��ǰi��������
#��Ȼ�ϲ�����ʱ���²��Ѿ���ǰi-1�������ź�������ֻ��Ƚ�i-1��i
#�ص����ʱ�����е����־��ź�˳��


#�ݹ��
def ins_sort_rec(seq,i):
    if i==0:return
    ins_sort_rec(seq,i-1)
    j=i
    while j>0 and seq[j-1]>seq[j]:
        seq[j-1],seq[j]=seq[j],seq[j-1]
        j-=1
#������
def ins_sort(seq):
    for i in range(1,len(seq)):
        j=i
        while j>0 and seq[j-1]>seq[j]:
            seq[j-1],seq[j]=seq[j],seq[j-1]
            j-=1

ins_sort_rec([123,546,7,897,834,54,5,6,82],8)