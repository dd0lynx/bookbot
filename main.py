def character_count(text):
    chr_count = {}
    for character in text.lower():
        if character in chr_count:
            chr_count[character] += 1
        else:
            chr_count[character] = 1
    return dict(sorted(chr_count.items(), key=lambda iteam: iteam[1], reverse=True))
    # return chr_count

def word_count(text):
    words = text.split()
    return(len(words))

def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as book:
        print(f"--- Begin report of {book_path} ---")
        
        text = book.read()
        wc = word_count(text)
        cc = character_count(text)

        print(f"{wc} words found in the document\n")
        for chr, count in cc.items():
            if chr.isalpha():
                print(f"The '{chr}' character was found {count} times")
        
        print("--- End report ---")

main()