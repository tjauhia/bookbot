from collections import Counter
#Could not figure out any other way to count the charactes in the text so I imported this class
def main():
    path_to_book = "books/frankenstein.txt" #define the path to the book to be used in other functions
    show_text = text_output(path_to_book) #define the use of text_output function. Takes the books path as an input
    num_count = word_counter(show_text) #define the use of word_counter function. Takes the text from text_output function as an input
    characters = character_count(show_text)
    print(f"We have {num_count} words in this book")#print the word count from word_counter function
    print("And below we have a count for each character in the text")
    print(characters)
#display the contents of the book. Use with-statement block
def text_output(path_to_book):
    with open(path_to_book) as f:#open the contents and rename the value as f
        return f.read() #return the contents by reading the opened file
#Count the words in the book
def word_counter(show_text):
    words = show_text.split()
    return len(words)
#function to count each character in the book
def character_count(show_text):
    #first we need to make every character lower case
    lower_chrs = show_text.lower()
    #use the Counter class to count the chars and output them as dictionary
    chr_counter = Counter(lower_chrs)
    return chr_counter
    #cant figure out how the get that effin "Counter"" out of the output though..
main()
