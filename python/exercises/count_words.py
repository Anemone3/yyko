def count(s:str):
    h_m = {}
    if s == "" or s == None:
        return h_m

    for letter in s:

        if h_m.get(letter) == None:
            h_m[letter] = 1
            continue

        if h_m[letter] >= 1:
            h_m[letter] = h_m[letter] + 1
    return h_m


print(count("asbb"))
