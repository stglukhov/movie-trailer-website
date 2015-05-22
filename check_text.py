import urllib

def read_text():
    quotes = open("/home/sglukhov/curse_words")
    contents_of_file = quotes.read()
    print (contents_of_file)
    quotes.close()
    check_pro(contents_of_file)

def check_pro(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    if "false" in output:
        print"It's all clear!"

    elif "true" in output:
            print "Achtung! Minnen!"

    else:
                print "WTF? It's not working"
    connection.close()
    
read_text()
