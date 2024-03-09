def main():
    path_to_book = "books/frankenstein.txt" #define the path to the book to be used in other functions
    show_text = text_output(path_to_book) #define the use of text_output function. Takes the books path as an input
    num_count = word_counter(show_text) #define the use of word_counter function. Takes the text from text_output function as an input
    characters = character_count(show_text) #dictionary define
    the_sorted_list = list_counts(characters)
    list_only_alphabet_char = only_alphabet(the_sorted_list)
    print(f"We have {num_count} words in this book")#print the word count from word_counter function
    print("__Lets start the report__")
    print(only_alphabet)
    print("The End")

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
    #create empty dict
    chr_dict = {}
    for chr in show_text:
        lower_chrs = chr.lower()
        if lower_chrs in chr_dict:
            #I wonder if I should have excluded special characters etc...
            chr_dict[lower_chrs] += 1
        else:
            chr_dict[lower_chrs] = 1
    return chr_dict

#function for sorting the number part in the list of dicts
#had to take a peek for this one since I could not figure out how to do this part
def sorttaus(d):
   return d["num"]

def only_alphabet(the_sorted_list):
    alph_list = the_sorted_list
    for i in alph_list:
        if not i["char"].isalpha(): #if character is part of the alphabet, print out the char and the count
            continue
        print(f"The '{i['char']}' character was found {i['num']} times")
    return alph_list

def list_counts(characters):
    sorted_list = []
    sorted_list.sort(reverse=True,key=characters)
    for char in characters:
        sorted_list.append({"char": char, "num": characters[char]})
    sorted_list.sort(reverse=False, key=sorttaus) #I want to count listing in ascending order
    return sorted_list

main()
