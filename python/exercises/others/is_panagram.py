import re
def is_pangram(st:str):
    st = re.sub(r'[^a-z]', '', st.lower())
    print("transform st:", st)
    return len(set(st)) == 26


print(is_pangram('Pack my box with five dozen liquor jugs.'))