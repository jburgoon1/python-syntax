def print_upper_words(words, must_start_with):
    for word in words:
        for string in must_start_with:

            if word.startswith(string):
                print(word.upper())








print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})