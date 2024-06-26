import sys

def main():
    if len(sys.argv) < 2:
        print("Error: call must have an argument")
        sys.exit(1)
    book_path = sys.argv[1]

    try:
        text = get_file_text(book_path)
    except Exception as e:
        print(f"Error: {e.args[1]}")
        sys.exit(1)
    
    num_words = count_words(text)
    chars = count_characters(text)
    alphs = sort_dict(get_alphs_dict(chars))

    print(f"----- Begin report of {book_path} -----")
    print(f"{num_words} words found in the document")
    print()

    print("Character - count in text")
    for letter, count in alphs.items():
        print(f"        {letter} - {count}")

    print("----- End report -----")

def get_file_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

    
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chars_dict = dict()
    for char in text:
        char = char.lower()
        if char not in chars_dict:
            chars_dict[char] = 1
            continue
        chars_dict[char]+=1
    return chars_dict

def get_alphs_dict(d:dict):
    alphs_dict = dict()
    for k, v in d.items():
        if k.isalpha():
            alphs_dict[k] = v
    return alphs_dict

def sort_dict(d:dict):
    tupled_dict = list(d.items())
    tupled_dict.sort(reverse=True, key=lambda e: e[1])
    return dict(tupled_dict)

main()