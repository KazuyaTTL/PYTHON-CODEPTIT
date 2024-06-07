import random
t = int(input())
for _ in range(t):
    lst = list(map(int, input().split()))
    n = int(input())
    uet = []
    for i in range(n):
        a = random.choice(lst)
        uet.append(a)
    def most_common(uet):
        count_dict = {}
        for item in uet:
            if item in count_dict:
                count_dict[item] += 1
            else:
                count_dict[item] = 1
        max_count = max(count_dict.values())
        return [item for item, count in count_dict.items() if count == max_count]
    print(min(most_common(uet)))