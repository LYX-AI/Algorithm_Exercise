def srt_match(text,target):
    n,m=len(text),len(target)
    for i in range(n-m+1):
        if text[i:i+m]==target:
            return i
    return -1
