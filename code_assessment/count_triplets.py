def count_triplets(s):
    start = 0
    end = 2
    count = 0
    triplets = []

    while end < len(s):
        if s[start].lower() == s[end].lower():
            triplets.append(s[start:end+1])
            count += 1

        start += 1
        end += 1

    print(triplets)
    return count


string = "abacccdedboldertiTruiwerthiGHg"
print(count_triplets(string))
