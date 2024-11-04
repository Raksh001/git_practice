"""
A function that should do the similar thing as method .split()

usage: my_split(list, delimiter)
       e.g: case1: my_split(' a aa   aaa ')
            case2: my_split(' a aa   aaa ', "")
            case3: my_split(' a aa   aaa ', "b")
            case4a: my_split('   ', " ")
            case4b: my_split(' a aa   aaa ', " ")
            case4c: my_split('Ba aaaB Baaaa ', "aaa")
"""


def my_split(string, delimiter=None):
    """ Split a string into a list where each word is a list item

    Args:
        string: An object of the 'str' class
        delimiter: A char that will used as delimiter

    Returns:
        A new list where each word is a list item

    """
    tmp_string = ''
    new_list = []

    # Case1 - no delimiter. Similar to <list>.split()
    # A special case when an empty delimiter is considered as space (" ").
    # The char " " is removed regardles of the position and lenght in the string.
    if delimiter == None:
        for idx in range(len(string)):
            if string[idx] != ' ':
                tmp_string += string[idx]
            else:
                if tmp_string != '':
                    new_list.append(tmp_string)
                    tmp_string = ''
        return new_list

    # Case2 - delimiter with empty separator
    if delimiter == '':
        print('ValueError: empty separator')
        # Returns None
        return

    # Case3 - delimiter not found in a string
    # Append the empty new_list with the same string that was provided as an argument
    if delimiter not in string:
        new_list.append(string)

    # Case4 - Removing delimiter from the string
    else:
        counter = 0
        for idx in range(len(string)):
            if (idx + counter < len(string)):
                string_to_check = string[idx + counter: idx + counter + len(delimiter)]

                # creating tmp_string from chars that are not delimiter
                if string_to_check != delimiter:
                    tmp_string += string[idx + counter]

                # delimiter was found
                else:
                    # makes a separation by appending new_list with tmp_string
                    # of collected chars and cleaning the temp_string
                    new_list.append(tmp_string)
                    tmp_string = ''

                    # The counter is helping to move the index
                    # to position just after found delimiter.
                    counter += len(delimiter) - 1

                # endif
            # endfor
        # If that was the last char, moves all of the collected
        # chars in tmp_string into the new_list
        new_list.append(tmp_string)

    # endif
    # The end of cases 3and 4 therefore returns new_list
    return new_list


c1 = my_split(' a aa   aaa ')
print("Case1: ", c1)
c2 = my_split(' a aa   aaa ', "")
print("Case2:", c2)
c3 = my_split(' a aa   aaa ', "b")
print("Case3", c3)
c4a = c4b = my_split('   ', " ")
print("Case4a", c4a)
c4b = my_split(' a aa   aaa ', " ")
print("Case4b", c4b)
c4c = my_split('aaaBaaaaaaBaa', "aaa")
print("Case4c", c4c)
