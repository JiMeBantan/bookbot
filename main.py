def extract_books_text(file_path):
    with open(file_path) as f:
        return f.read()

def count_words(tx:str) :
    return len(tx.split())

def count_characters_occurances(tx:str):
    chrs = {}
    for letter in tx:
        letter_lower = letter.lower()
        if letter_lower in chrs:
            chrs[letter_lower] += 1
        else:
            chrs[letter_lower] = 1
    # sorting by keys
    # return sorted(chrs.items())

    # sorting by values (counts)
    return sorted(chrs.items(), key=lambda x: x[1], reverse=True)

def main():
    # reading and printing the contents of a file
    book_text = extract_books_text('books/frankenstein.txt')
    #print(book_text)

    print(f"--- Begin report of {book_text} ---")
    print(f"{count_words(book_text)} words found in the document \n")
    chr_list = count_characters_occurances(book_text)
    for chrs in chr_list :
        if chrs[0].isalpha() :
            print(f"The '{chrs[0]}' character was found {chrs[1]} times")
    print("--- End report ---")



if __name__ == "__main__":
    main()