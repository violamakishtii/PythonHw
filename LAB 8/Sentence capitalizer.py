def capitalize_sentences(input_str):
    sentences = input_str.split('. ')
    capitalized_sentences = [sentence.capitalize() for sentence in sentences]
    return '. '.join(capitalized_sentences)

def main():
    user_input = input("Enter a string: ")
    modified_string = capitalize_sentences(user_input)
    print("Modified string:")
    print(modified_string)

main()
