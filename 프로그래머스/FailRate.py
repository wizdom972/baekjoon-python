def solution(N, stages):
    answer = []
    
    peopleNum = len(stages)
    failRate = [(0, 0)] * (N+1)
    
    for i in range(1, N+1):
        challenger = stages.count(i)
        
        if peopleNum != 0:
            failRate[i] = (i, challenger / peopleNum)
            peopleNum -= challenger
        else:
            failRate[i] = (i, 0)
        
    failRate = failRate[1:]
    
    failRate.sort(key=lambda x: x[1], reverse=True)
    for r in failRate:
        answer.append(r[0])
    
    return answer