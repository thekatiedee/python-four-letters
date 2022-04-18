# make a program that filters a list of strings and only selects the four-letter words.
# example: input = ['donna', 'josh', 'sam', 'cj', 'toby', 'cat', 'dog', 'bird']
# example: output = ['josh', 'toby', 'bird']
# keep the original order of the words from the input, in the output.

a_list = []

while True:
    thing = input("enter a word or type 'end' to end the program: ")
    if thing.lower() == "end":
        print("the program is ending.")
        break
    else:
        pass
    print("calculating...")
    length = len(thing)
    a_list.append(thing)
    if length != 4:
        a_list.remove(thing)
        print("sorry! that word did not pass the test.")
    else:
        print("this is a list of your four-letter words: ", a_list)
