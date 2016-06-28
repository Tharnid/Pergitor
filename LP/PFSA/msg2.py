with open("message.txt", "r") as source:
    for line in source:
        junk1, keyword, size= line.rstrip().partition("Size")
        if keyword != '':
            print( size )
