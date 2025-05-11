def find_instersection_with_set(nums1,nums2):
    intersection=list(set(nums1)&set(nums2))
    return intersection
def find_instersection_with_set2(nums1,nums2):
    i,j=0,0
    sort_num1=sorted(nums1)
    sort_num2=sorted(nums2)
    finalresult = []
    while i< len(sort_num1) and j<len(sort_num2):
        if sort_num2[i]==sort_num2[j]:
            if not finalresult or sort_num2!=finalresult[-1]:
                finalresult.append(sort_num1[i])
            i+=1
            j+=1
        elif sort_num1[i]<sort_num2[j]:
            i+=1
        else:
            j+=1
    return finalresult



if __name__=="__main__":
    nums1 = [1,2,2,1,3,4]
    nums2 = [2,2,3,5,6]
    print(find_instersection_with_set(nums1,nums2))