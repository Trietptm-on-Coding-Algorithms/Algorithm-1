#!/usr/bin/python
#-*- coding:utf-8 -*-
#���������㷨
#���㷨���ĳһ�Ѿ����������
def bisect_right(a,x,lo=0,hi=None):
    if hi in None:
        hi=len(a)
    while lo<hi:
        mid=(lo+hi)/2
        #��Ҫ���бȽϵ��м�ֵ
        if x<a[mid]:hi=mid
        #���xС���м�ֵ������Ҫ��Ѱ��벿��
        else:lo=mid+1
    return lo
