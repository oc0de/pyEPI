import heapq
import collections

def find_student_with_highest_best_of_three_scores(name_score_data):
    student_scores = collections.defaultdict(list)
    for line in name_score_data:
        name, score = line.split(',')
        if len(student_scores[name]) < 3:
            heapq.heappush(student_scores[name], int(score))
        else:
            heapq.heappushpop(student_scores[name], int(score))

    return max([(sum(v), k) for k, v in student_scores.items() if len(v) == 3])


txt = ['adnan,100','amit,99','adnan,98','thl,90','adnan,10','amit,100','thl,99','thl,95','dd,100','dd,100','adnan,95']

result = find_student_with_highest_best_of_three_scores(txt)
assert result[1] == 'adnan'
