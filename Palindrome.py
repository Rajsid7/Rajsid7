#SidhuRajpritAsn3b

while True:
    phrase = input("Enter a phrase: ")
    if phrase == "":
        break

    reversed_string, modified = "", ""
    for ab in phrase:
        ab = ab.lower()
        if ab.isalpha():
            reversed_string = ab + reversed_string
            modified += ab

    if modified == reversed_string:
        print("Great! This is a palindrome")

    else:
        print("Sorry, this is not a palindrome")

#end of command
