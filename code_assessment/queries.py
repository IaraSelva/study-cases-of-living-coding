def solution(queries, diff):
    response = []
    curr_count = 0
    count_num = {}
    
    for q in queries:
        op = q[0]
        num = int(q[1:])

        if op == "+":
            if num - diff in count_num:
                curr_count += count_num.get(num-diff)
            if num + diff in count_num:
                curr_count += count_num.get(num+diff)
            
            count_num[num] = count_num.get(num, 0) + 1
        
        if op == "-":
            if num - diff in count_num:
                curr_count -= count_num.get(num-diff)
            if num + diff in count_num:
                curr_count -= count_num.get(num+diff)

            count_num[num] = count_num.get(num, 0) -1
            if count_num.get(num) <= 0:
                del count_num[num]
        
        response.append(curr_count)
        
    return response



queries = ["+4", "+5", "+2", "-4"]
diff = 1
print(solution(queries, diff))

