#!/usr/bin/python
#-*- coding:utf-8 -*-
#�۰�����

#�ָ��
def parttion(seq):
    pi,seq=seq[0],seq[1:]
    #ѡȡ��һ��Ϊ�м�ֵ
    lo=[x for x in seq if x<=pi]
    hi=[x for x in seq if x>pi]
    #�����м�ֵ�ָ��������
    return lo,pi,hi

def select(seq,k):
    lo,pi,hi=parttion(seq)
    #�ָ�����
    m=len(lo)
    #ǰ�벿�ֳ���
    if m==k:return pi
    #Ѱ��ǰkС��������m=k�򷵻�
    elif m<k:
        #���m<k��˵��ǰkС���Ұ벿��
        return select(hi,k-m-1)
        #���ǲ������С����Ϊ����ֻȡ��벿��
    else:
        return select(lo,k)
