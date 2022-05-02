from itertools import combinations

def solution(orders, course):
    answer = []
    for c_num in course:
        counter = {}
        for order in orders:
            if c_num <= len(order):
                course_combination = list(combinations(sorted(order), c_num))
                for cc in course_combination:
                    str_cc = ''.join(cc)
                    if counter.get(str_cc):
                        counter[str_cc] += 1
                    else:
                        counter[str_cc] = 1
        
        frequent = 2
        frequent_course = []
        for key in counter:
            if frequent < counter[key]:
                frequent = counter[key]
                frequent_course = [key]
            elif frequent == counter[key]:
                frequent_course.append(key)
        answer += frequent_course
    answer.sort()
    
    return answer