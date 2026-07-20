def count_elements(lst):
    count = {}

    for i in lst:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for key in count:
        print(key, "=>", count[key])

sample = [10,20,30,30,30,30,20,40]

count_elements(sample)
