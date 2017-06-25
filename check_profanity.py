from urllib.request import urlopen, pathname2url

def read_text():
    quotes = open("E:\Work\Python\python-code\movie_quotes.txt")
    file_contenets = quotes.read()
    quotes.close()
    check_profanity(file_contenets)

def check_profanity(text_to_check):
    connection = urlopen(u"http://www.wdylike.appspot.com/?q="+pathname2url(text_to_check))
    output = connection.read()
    # print(output)
    if output == b'true':
        print("Profanity spotted!")
    elif output == b'false':
        print("Looks good.")
    else:
        print("Document could not be scanned.")
    connection.close()

read_text()
