alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def decode_message(msg):
    result = ''

    for each_letter in msg:
        if each_letter not in alphabets:
            result = result + each_letter
        else:
            idx = alphabets.index(each_letter)
            if idx <= -1:
                result = result + each_letter
            else:
                new_idx = (idx + 10) % 26
                if new_idx < 0:
                    new_idx = new_idx + len(alphabets)
                new_char = alphabets[new_idx]
                result = result + new_char
    return result

print(decode_message("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."))
