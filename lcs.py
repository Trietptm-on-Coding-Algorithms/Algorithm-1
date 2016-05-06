#!/usr/bin/python
#-*- coding:utf-8 -*-

#�ݹ顢��������LCS(�����������)
#���������е����ұ߿�ʼ�Ƚ�������ͬ��Ԫ�أ�����о�һͬȥ��
#����ͽ���Ƚϣ���һ�����е����ұߺ���һ���ĵ����ڶ�������������ݹ飬������©
#��֤ÿ���ݹ鶼���������������
def rec_lcs(a,b):
    @memo
    def L(i,j):
        if min(i,j)<0:return 0
        if a[i]==b[j]:return 1+L(i-1,j-1)
        #����ҵ���ͬԪ�أ���ȥ������Ԫ��
        return max(L(i-1,j),L(i,j-1))
        #�������ͬ����ʼ����ݹ�
    return L(len(a)-1,len(b)-1)

#�������㷨
def lcs(a,b):
    n,m=len(a),len(b)
    pre,cur=[0]*(n+1),[0]*(n+1)
    for j in range(1,m+1):
        #��һ��ѭ��������a��ÿ��Ԫ��
        pre,cur=cur,pre
        #�����ϴ�ѭ��������cur
        for i in range(1,n+1):
            #��������b��ÿ��Ԫ�أ���a��һ��Ԫ�رȽ�
            if a[i-1] == b[j-1]:
                cur[i] = pre[i-1]
                #�ҵ���ͬԪ�أ��������cur[i]+1
            else:
                cur[i] = max(pre[i],cur[i-1])
                #û�ҵ�֮ǰ���Ὣcur��Ԫ��ͬ����pre����Ϊ��ʱpre����
                #�ҵ����ͬ����cur����Ϊ��ʱcur�Ѿ���1
    return cur[n]
