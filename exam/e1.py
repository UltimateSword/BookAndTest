mapper = dict()
def handle(w):
    record = []
    ans = []
    n = len(w)
    if n <= 1:
        return w
    if w in mapper:
        return mapper[w]
    i = 0
    while i < n:
        if len(record) == 3:
            if record[-1] == w[i]:
                new_w = ''.join(record) + w[i+1:]  # aabb -> aab+w[i+1]
                ans.append(handle(new_w))
                record.clear()
                break
            else:  # aabc
                ans.append(''.join(record))
                record.clear()
                record.append(w[i])
        elif len(record) == 2:  # aa
            if record[-1] == w[i]:  # aa -> aaa
                new_w = ''.join(record) + w[i+1:]
                ans.append(handle(new_w))
                record.clear()
                break
            else:  # aa -> aab
                record.append(w[i])
        elif len(record) == 1:  # a
            if record[-1] == w[i]:  # aa
                record.append(w[i])
            else:  # ab
                ans.append(''.join(record))
                record.clear()
                record.append(w[i])
        elif len(record) == 0:
            record.append(w[i])
        i += 1
    ans.append(''.join(record))
    mapper[w] = ''.join(ans)
    return mapper[w]


if __name__ == '__main__':
    t = "uhhccceeegggghhha mksluvvvjjjuuueyyjjrrtrrrrrrnnnooyiiiannndddwjjjtppucccmmmvyyziiiniixtttmmm"
    print(handle("jjrrtrrrrrrnnnooyiiiannndddwjjjtppucccmmmvyyziiiniixtttmmm"))
    print("jrrtrrnooyiianndwjjtppuccmvyyziiniixttm")
