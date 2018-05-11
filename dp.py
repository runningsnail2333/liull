def match(s1,s2):
    length = len(s2)
    result = ""
    resultMisaamatchCount = length
    seqdict={}
    for index, s in enumerate(s1[:-length]):
        missmatch = 0
        for j,k in zip(s1[index:index+length],s2):
            if j!=k:
                missmatch +=1
        if missmatch <= resultMissmatchCount:
            seqdict[missmatch]=s1[index:index+length]
            resultMissmatchCount = missmatch
    minkey = min(seqdict.key())        
    result = seqdict[minkey]
    return result
