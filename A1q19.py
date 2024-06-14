def remove_punctuation(input_string):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in input_string:
        if char not in punctuation:
            no_punct = no_punct + char

    return no_punct
input_string = input("enter a string")
clean_string = remove_punctuation(input_string)
print(clean_string)