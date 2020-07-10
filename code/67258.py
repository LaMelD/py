# 보석 쇼핑

def check_answer(answer_start, answer_end, answer_count, start, end):
    
    return 0

def solution(gems):
    gem_idx = {}
    
    # 보석의 종류를 찾는다.
    for gem in gems:
        if gem not in gem_idx:
            gem_idx[gem] = {}
            gem_idx[gem]['count'] = 0
    
    kind = len(list(gem_idx.keys()))

    # 종류가 한 가지라면 [1,1]을 리턴
    if kind == 1:
        return [1, 1]
    
    # answer의 초기값
    answer_start = -1
    answer_end = -1
    answer_count = -1
    
    # 초기 세팅
    count = 0
    start = 0
    end = 0
    while True:
        if end == len(gems):
            break

        # count 올리는 조건
        if start == end:
            gem_idx[gems[end]]['count'] += 1
            count += 1
            end += 1
            continue
        
        if gem_idx[gems[end]]['count'] == 0:
            count += 1
        gem_idx[gems[end]]['count'] += 1
        
        if gems[start] == gems[end]:
            gem_idx[gems[end]]['count'] -= 1
            gem_idx[gems[start]]['count'] -= 1
            if gem_idx[gems[end]]['count'] == 0:
                count -= 1
            start += 1
            continue
        
        while True:
            if end < start + 1 or gems[start] != gems[start + 1]:
                break
            gem_idx[gems[start]]['count'] -= 1
            start += 1

        if count == kind:
            if answer_count == -1:
                answer_start = start
                answer_end = end
                answer_count = end - start + 1
            elif (end - start + 1) < answer_count:
                answer_start = start
                answer_end = end
                answer_count = end - start + 1
            gem_idx[gems[start]]['count'] -= 1
            if gem_idx[gems[start]]['count'] == 0:
                count -= 1
            start += 1
        else:
            end += 1


    return [answer_start + 1, answer_end + 1]

if __name__ == '__main__':
    # myinput = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    # myinput =	["AA", "AB", "AC", "AA", "AC"]
    # myinput = ["XYZ", "XYZ", "XYZ"]
    # myinput =	["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
    myinput = ['a','b','b','a','a','c','a','b']
    print(solution(myinput))