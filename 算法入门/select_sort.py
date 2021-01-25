# def select_sort_simple(li):
#     li_new = []
#     for i in range(len(li)):
#         min_val = min(li)
#         li_new.append(min_val)
#         li.remove(min_val)
#     return li_new


def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]


li = [3, 2, 4, 1, 5, 6, 7, 8, 9]
print(select_sort_simple(li))
