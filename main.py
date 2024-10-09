def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_counter = word_count(text)
    # character_count = char_count(text)
    bookreport = report(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_counter} words found in the text.")
    for entry in bookreport:
        print(f"The character {entry['Character']} was found {entry['Frequency']} times.")
    print("--- End of book report ---")

def get_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    text = text.lower()
    text2 = list(text)
    dict = {}
    for char in text2:
        if char not in dict:
            dict[char] = 1
        elif char in dict:
            dict[char] += 1
    return dict

def report(text):
    dict = char_count(text)
    char_list = []
    for char in dict:
        if char.isalpha() == True:
            dict2 = {}
            dict2["Character"] = char
            dict2["Frequency"] = dict[char]
            char_list.append(dict2)
    char_list.sort(reverse=True,key=sort_on)
    return char_list

def sort_on(dict):
    return dict["Frequency"]
    
if __name__ == "__main__":
    main()