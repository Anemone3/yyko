

def camel_case(text:str):
    clear_text = text.replace("-", "_").split("_")
    
    if not clear_text:
        return ""
    
    max_length = len(clear_text)

    for i in range(1,max_length):
        clear_text[i] = clear_text[i].capitalize()

        if len(clear_text[0]) == 1 and clear_text[max_length - 1 ] == 1:
                    clear_text[0] = clear_text[0].upper()
            

    return "".join(clear_text)


r = camel_case("A-B-C")

print(r)