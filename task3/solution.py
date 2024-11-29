def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_interval = intervals['lesson']
    pupil_intervals = intervals['pupil']
    tutor_intervals = intervals['tutor']

    pupil_intervals = [(pupil_intervals[i], pupil_intervals[i+1]) for i in range(0, len(pupil_intervals), 2)]
    tutor_intervals = [(tutor_intervals[i], tutor_intervals[i+1]) for i in range(0, len(tutor_intervals), 2)]

    def merge_intervals(intervals):
        intervals.sort()
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            last = merged[-1]
            last_end = last[1]
            
            if start > last_end:
                merged.append(intervals[i])
            else:
                merged[-1] = (last[0], max(last_end, end))
        
        return merged

    pupil_intervals = merge_intervals(pupil_intervals)
    tutor_intervals = merge_intervals(tutor_intervals)

    i = j = total = 0
    while i < len(pupil_intervals) and j < len(tutor_intervals):
        start = max(pupil_intervals[i][0], tutor_intervals[j][0], lesson_interval[0])
        end = min(pupil_intervals[i][1], tutor_intervals[j][1], lesson_interval[1])
        total += (end - start) if (end - start) > 0 else 0
        if pupil_intervals[i][1] > tutor_intervals[j][1]:
            j += 1
        elif pupil_intervals[i][1] < tutor_intervals[j][1]:
            i += 1
        else:
            i += 1
            j += 1
    return total

tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 
                       1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 
                       1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 
                       1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'