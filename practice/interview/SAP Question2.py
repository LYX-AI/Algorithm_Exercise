'''
The current selected programming language is Python3. We emphasize the submission of a fully working code over partially correct but efficient code. Use of certain header files are restricted. Once submitted, you cannot review your code again. You can use print to debug your problem. The print may not work in case of syntax/runtime error. The version of Python being used is 3.4.3.

A square matrix A[1..n][1..n] is called palindromic if A[i][j] = A[n + 1 - i][n + 1 - j] for all 1 ≤ i, j ≤ n.

Given a matrix inputMat[1..N][1..M], find the number of elements in its largest palindromic square sub-matrix.

Input
The first line of the input consists of two integers - inputMat_row and inputMat_col, representing the number of rows (N) and the number of columns in the matrix (M), respectively.
The next N lines consist of M space-separated integers - inputMat[i][......][i], inputMat[N][M], representing the elements of the matrix.

Output
Print an integer representing the number of elements in the largest palindromic sub-matrix.

Constraints
1 ≤ inputMat_row, inputMat_col ≤ 50
1 ≤ inputMat[i][j] ≤ 10^4
1 ≤ i ≤ inputMat_row
1 ≤ j ≤ inputMat_col

Note
The sub-matrix should contain an odd number of elements.

Example
Input:
5 4
9 8 7 6
2 3 2 5
7 8 9 7
5 4 3 2
6 7 8 9

Output:
9
'''
#判断是否是回文矩阵：
def is_palindromic(sub_matrix):
    for i in range(len(sub_matrix)):
        for j in range(len(sub_matrix[0])):
            '''
            为什么底下这个判断要这么写：这里有个解释

            这个判断语句是在检查一个子矩阵是否为回文矩阵。在数学和编程中，回文矩阵指的是一个矩阵，当沿着中心对折时，每个元素与其对称位置上的元素相等。在这个上下文中，对于一个矩阵A来说，如果它满足A[i][j] == A[n-i-1][m-j-1]，它就被认为是回文的，这里n和m分别是矩阵的行数和列数。

在 Python 中，负数索引用于从列表的末尾开始倒数，例如 -1 是最后一个元素，-2 是倒数第二个，依此类推。

因此，sub_matrix[-(i + 1)][-(j + 1)]：

-(i + 1) 表示从矩阵底部往上数的第 i+1 个位置。
-(j + 1) 表示从矩阵右边往左数的第 j+1 个位置。
这种写法让我们可以找到与 sub_matrix[i][j] 在矩阵中对称的元素，即矩阵的对角元素。

例如，如果矩阵是 5x5 的，那么元素 sub_matrix[0][0]（即左上角第一个元素）和元素 sub_matrix[4][4]（即右下角最后一个元素）应该是相等的，如果这个子矩阵是回文的。在 Python 的负数索引中，sub_matrix[4][4] 可以通过 sub_matrix[-1][-1] 访问。

当 if sub_matrix[i][j] != sub_matrix[-(i + 1)][-(j + 1)]: 这条语句被执行时，它检查了第 (i, j) 个元素是否与其对称元素不相等，如果这个条件为真，那么子矩阵不是回文的，并且函数可以返回 False。
            '''
            if sub_matrix[i][j] !=sub_matrix[-(i+1)][-(j+1)]:
                return False
        return True
    
    def langest_palindromic(input_mat):
        nrows=len(input_mat)
        ncols=len(input_mat[0])
        max_palindromic_size=0

        # 暴力方法检查每个可能的子矩阵
        for row_start in range(nrows):
            for row_end in range(row_start,nrows):
                for col_start in range(ncols):
                    for col_end in range(col_start,ncols):
                        '''
                        知识点：这里是比获得子举证的方法
                        这行代码是使用 Python 列表推导式（list comprehension）从给定的矩阵 `input_mat` 中提取一个子矩阵 `sub_matrix`。这里的 `input_mat` 是原始的二维列表，我们想要从中提取一个特定的矩形区域，这个区域由行的起始索引 `row_start` 和结束索引 `row_end`，以及列的起始索引 `col_start` 和结束索引 `col_end` 定义。

具体步骤分解如下：

- `input_mat[row_start:row_end+1]`: 这是一个切片操作，用于从 `input_mat` 中选择从第 `row_start` 行到第 `row_end` 行的行。由于 Python 的切片是半开区间，所以我们使用 `row_end+1` 来确保第 `row_end` 行被包含在切片内。

- `for row in input_mat[row_start:row_end+1]`: 这个循环遍历上面切片得到的每一行。

- `row[col_start:col_end+1]`: 对于遍历中的每一行，这是一个更深层次的切片操作，用于从每行中选择从第 `col_start` 列到第 `col_end` 列的元素。同样，使用 `col_end+1` 来确保第 `col_end` 列的元素被包含在切片内。

最终结果 `sub_matrix` 是一个新的二维列表，包含了 `input_mat` 的一个子区域，由行索引 `row_start` 到 `row_end` 和列索引 `col_start` 到 `col_end` 定义的所有元素。

比如说，如果 `input_mat` 如下：

```python
input_mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
```

并且我们的索引是 `row_start=1`, `row_end=2`, `col_start=1`, `col_end=2`，那么这行代码将会提取如下子矩阵：

```python
sub_matrix = [
    [6, 7],
    [10, 11]
]
```

这个子矩阵是 `input_mat` 中第2行和第3行、第2列和第3列的交叉部分。
                        '''
                    sub_matrix=[row[col_start:col_end+1] for row in input_mat[row_start:row_end+1]]
                    if is_palindromic(sub_matrix):
                        max_palindromic_size=max(max_palindromic_size,(row_end-row_start+1)*(col_end-col_start+1))
        return max_palindromic_size
    

    def main():
        input_mat=[]
        input_mat_row,input_mat_cols=map(int,input().split())
        for idx in range(input_mat_row):
            input_mat.append(list(map(int,input().split())))
        
        result=langest_palindromic(input_mat)
        print(result)
    
    if __name__=='main':
        main()