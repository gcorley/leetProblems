def longest_task(n: int, logs: list[list[int]]) -> int:
    answer = [0, 0]  # id, duration
    prev = 0
    for log in logs:
        dur = log[1] - prev
        if dur > answer[1] or dur == answer[1] and log[0] < answer[0]:
            answer[0] = log[0]
            answer[1] = log[1] - prev
        prev = log[1]
    return answer[0]
