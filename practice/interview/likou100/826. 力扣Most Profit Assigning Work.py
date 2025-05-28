class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        jobs = sorted(zip(difficulty,profit))
        i = 0 #用来遍历jobs的
        result = 0#存放最终结果
        best=0 #每次遍历的结果放到这来
        for ability in sorted(worker):
            #找到每个工人干哪个活收益最大
            while i < len(jobs) and jobs[i][0]<=ability:
                best = max(best,jobs[i][1])
                i+=1
            result+=best
        return result
