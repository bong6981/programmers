def solution(files):
    print(files)
    new_files = []
    for i, file in enumerate(files):
        to_add = []
        st_n, name = number_first_index_and_make_lower(file)
        to_add.append(name)
        file = file[st_n:]
        to_add.append(get_numger(file))
        to_add.append(i)
        new_files.append(to_add)

    
    print(new_files)
    print(files)

    new_files.sort(key = lambda x: (x[0], x[1], x[2]))
    answer = []
    for new_file in new_files:
        answer.append(files[new_file[2]])
    return answer

def number_first_index_and_make_lower(name):
    head = ''
    for i, c in enumerate(name):
        if c.isdigit():
            return i, head
        if c.isalpha():
            c = c.lower()
        head += c

def get_numger(name):
    number = ''
    cnt = 0
    for i in range(len(name)):
        if not name[i].isdigit():
            break
        number += name[i]
        cnt += 1
        if cnt == 5:
            break
    return int(number)

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))

# arr = [1,2,3]
# arr.sort(key = lambda x: (-arr.index(x)))
# print(arr)


# input = "hello"
# arr = [["hello", 3], ["hello", 2], ["bye", 3]]
# arr.sort(key= lambda x: (x[0], x[1]))
# print(arr) ## [['bye', 3], ['hello', 2], ['hello', 3]]


## 0619
# def solution(files):
#     sort_info = []
#     for k in range(len(files)):
#         f = files[k]
#         info = []
#         idx = 0
#         for i in range(len(f)):
#             if f[i].isdigit():
#                 idx = i
#                 break
#         info.append(f[:idx].lower())
#         num_idx = 0
#         for i in range(idx, idx+5):
#             num_idx = i
#             if not f[i].isdigit() :
#                 num_idx = i-1
#                 break

#         # print(idx, num_idx+1, f, f[idx:num_idx+1])
#         info.append(int(f[idx:num_idx+1]))
#         info.append(k)
#         sort_info.append(info)
    
#     sort_info.sort()
#     answer = []
#     for e1, e2, idx in sort_info:
#         answer.append(files[idx])
#     return answer


# print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))




