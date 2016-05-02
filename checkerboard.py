#!/usr/bin/python
#-*- coding:utf-8 -*-

def cover(board,lab=1,top=0,left=0,side=None):
    if side is None:side=len(board)
    s=side/2
    #取传入长度一半
    offsets=(0,-1),(side-1,0)
    for dy_outer,dy_inner in offsets:
        #dy_outer=0 dy_inner=-1    dy_outer=side-1 dy_inner=0
        for dx_outer,dx_inner in offsets:
        #dx_outer=0 dx_inner=-1    dx_outer=side-1 dx_inner=0
            if not board[top+dy_outer][left+dx_outer]:
                #四次迭代，将棋盘从中间分成四个小块，检测哪个角不是缺口（这里设定，如果为0则不为缺口）
                #如果不为缺口，则将四小块中的这一小块的右下角设定为lab，可理解为取出这一块砖头
                #整个过程可以理解为，将拼接好的棋盘，按L型砖取出
                board[top+s+dy_inner][left+s+dx_inner]=lab
    #已经取出来的砖块数加一
    lab+=1
    if s>1:
        for dy in [0,s]:
            for dx in [0,s]:
            #迭代dy，dx，改变传入top+dy,left+dx，分别递归四个方块
                lab=cover(board,lab,top+dy,left+dx,s)
            #递归第一个方块，检测缺口，重复上面步骤，然后而分割四块，进行递归
            #只有递归到最后一层返回后，才会进行上一层dy，dx迭代改变的递归
    return lab

board=[[0]*8 for i in range(8)]
board[7][7]=-1
print cover(board)
for row in board:
    print ("    %2i"*8)%tuple(row)
