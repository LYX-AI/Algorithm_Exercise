def test1(str):
    String_Set = set()
    left=0
    result=0
    for right in range(len(str)):
        while str[right] in String_Set:
            String_Set.remove(str[left])
            left+=1
        String_Set.add(str[right])
        result=max(result,right-left+1)
    return result

if __name__=="__main__":
    s="abcabcbb"
    s2="bbbbb"
    s3="pwwkew"
    print(test1(s))
    print(test1(s2))
    print(test1(s3))
