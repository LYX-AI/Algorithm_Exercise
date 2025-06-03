class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x:x[0])
        result=[]
        for internal in intervals:
            if not result or result[-1][1]<internal[0]:
                result.append(internal)
            else:
                result[-1][1]=max(result[-1][1],internal[1])
        return result
