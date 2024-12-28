'''

To cacluate the average
'''

'''
Way1:
    tip:
        1. Using the sum() function in the python
'''
scores=[78,82,69,95,83]
average_score=sum(scores)/len(scores)
print(len(scores))
print("the average is",average_score)

'''
way2:
    tip:
        Using the statistics module
        in the statistics can use the mean function to caculate the average
'''
import statistics

average_score2=statistics.mean(scores)
print(average_score2)
