# Main puts it all togther, take a look at the functions below.
def main():
    book_path = "books/frankenstein.txt"

    text = get_book_text(book_path)
    lowerCased = text.lower()
    count=get_word_count(lowerCased)
    count_characters = get_letter_count(lowerCased)
    sortedDiccy = get_sorted_character_list(count_characters)
    print()
    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document\n")
    for key, value in sortedDiccy.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")


# open the text file and turn it into a string
def get_book_text(path):
    with open(path) as f:
        return f.read()

# get the word total work count by creating a list and spliting it and getting the len
def get_word_count(text):
    words = len(text.split())
    return words

# get the letter count by taking that text from the get_book_text function and going over each letter and adding it into a dictionary. Note that we only wanted the alpha letters no . ! or any of those other symbols
def get_letter_count(text):
    characters = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    for x in text:
        if x in characters.keys():
            characters[x] += 1
    return characters

# sort the dictionary from the highest to the very lowest character count. 
def get_sorted_character_list(dic):
    sortedDic = sorted(dic.items(), key = lambda x:x[1], reverse=True)
    return dict(sortedDic)

main()



