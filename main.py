def main():
    path_to_book = "books/frankenstein.txt"
    show_text = text_output(path_to_book)
    num_count = word_counter(show_text)
    print(f"We have {num_count} words in this book")

def text_output(path_to_book):
    with open(path_to_book) as f:
        return f.read()

def word_counter(show_text):
    words = show_text.split()
    return len(words)

main()
