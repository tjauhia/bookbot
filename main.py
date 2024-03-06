def main():
    path_to_book = "books/frankenstein.txt" #define the path to the book to be used in other functions
    show_text = text_output(path_to_book) #define the use of text_output function. Takes the books path as an input
    num_count = word_counter(show_text) #define the use of word_counter function. Takes the text from text_output function as an input
    print(f"We have {num_count} words in this book")#print the word count from word_counter function
#display the contents of the book. Use with-statement block
def text_output(path_to_book):
    with open(path_to_book) as f:#open the contents and rename the value as f
        return f.read() #return the contents by reading the opened file
#Count the words in the book
def word_counter(show_text):
    words = show_text.split()
    return len(words)

main()
