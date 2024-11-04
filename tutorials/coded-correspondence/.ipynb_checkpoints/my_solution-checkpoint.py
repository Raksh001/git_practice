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
                new_idx = idx - 10
                if new_idx < 0:
                    new_idx = new_idx + len(alphabets)
                new_char = alphabets[new_idx]
                result = result + new_char
    return result

print(decode_message("xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"))


# YOUR SOLUTION
# nke znkxk! znoy oy gt kdgsvrk ul g igkygx iovnkx. ckxk eua ghrk zu jkiujk oz? o nuvk yu! yktj sk g skyygmk hgiq cozn znk ygsk ullykz!

# THEIR SOLUTION
# hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!
