'''
topic:
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 
输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
'''
'''
Train of through:
 Firstly: we need to make ure the number of the loop, and then creat a loop, in this loop to traverse every side of the matrix
the number of the loop we can acount as follow :n//2

The reason:
因为搜索一圈之后，下一圈的上边会往下走，下一圈的下边会往上走，高度就少2;
下一圈的左边会往右走，下一圈的右边会往左走，相当于宽少2了;
每次下一圈都会比上一圈的高度宽度都少2，直到这个没有外圈了，没有外圈就是宽度是和高度都是0的时候（偶数的情况），每次宽，高缩小2，直到宽，高是0。
因为宽，高都一样，而且是一起缩2的，那么就当高缩2到0的时候就结束了，要缩多少次，就是圈。高假设是偶数，偶数-2-2-2一直到0，不就是这个偶数除2吗，就是圈数啦

and in this loop we will have four loop, one loop is uesd to traverse every side of matrix;
and we need to make clear that every side shouled be same to get the message ,we can get the first element and ignore the last element(Close left and open right)

'''
n=4
class Solution:
    def generateMatrix(n: int):
        
        nums=[[0] *n for _ in range(n)] 
       # The coord of the start position 
        startX=0
        startY=0
        loop,middle=n//2,n//2
        count=1

        for offset in range(1,loop+1):
            #最上面一个边(从左至右)
            for i  in range(startY,n-offset):
                nums[startX][i]=count
                count+=1
            #开始右边的一个边(从上到下)
            for i in range(startX,n-offset):
                nums[i][n-offset]=count
                count+=1
            #开始遍历下面的边(从右到左)
            for i in range (n-offset,startY,-1):
                nums[n-offset][i]=count
                count+=1
            #开始遍历左边的边(从下到上)
            for i in range(n-offset,startX,-1):
                nums[i][startY]=count
                count+=1
            #跟新起点
            startX+=1
            startY+=1
        if n%2!=0:
            nums[middle][middle]=count
        return nums
print(Solution.generateMatrix(n=n))



        
