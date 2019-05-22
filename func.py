def func(s):
    L = []
    for start in range(len(s)):
        d = {'answer': None, 'lenth': None, 'position': None}
        sL = s[start]
        for i in range(start+1, len(s)):
            if s[i] not in sL:
                sL += s[i]
            else:
                d['answer'] = sL
                d['lenth'] = i - start
                d['position'] = start
                L.append(d)
                break

    lenthL = []    
    for d in L:
        lenthL.append(d['lenth'])
    lenthL =  sorted(lenthL)
    max_lenth = lenthL.pop()

    for d in L:
        if d['lenth'] == max_lenth:
            print(d)

s = input('请输入字符串')
func(s)