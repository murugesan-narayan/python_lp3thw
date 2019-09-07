
dictionary = {
'north': ('direction', 'north'),
'south': ('direction', 'south'),
'east': ('direction', 'east'),
'west': ('direction', 'west'),
'go': ('verb', 'go'),
'kill': ('verb', 'kill'),
'eat': ('verb', 'eat'),
'the': ('stop', 'the'),
'in': ('stop', 'in'),
'of': ('stop', 'of'),
'bear': ('noun', 'bear'),
'princess': ('noun', 'princess'),
'3': ('number', 3),
'91234': ('number', 91234),
'1234': ('number', 1234)
}

def scan(direction):
    words = direction.split()
    ret_list = []
    for word in words:
        ret = dictionary.get(word)
        if ret:
            ret_list.append(dictionary.get(word))
        else:
            ret_list.append(('error', word))
    return ret_list
