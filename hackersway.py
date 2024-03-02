print("Thanks to the hackers!")

"""
Dear ghost hacker; 
My manager asked me to find all vows ( a special character getting generated form a file, not vowels) .
I wrote this following piece of code. 

Please see if my code is correct. 


"""


def vow_count(sentence):
    vows = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for x in sentence:
        if x in vows:
            count += 1
    print(count)


vow_count("abracadabra")
vow_count("bcdfghjklmnpqrstvwxz y")