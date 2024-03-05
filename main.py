#as long as the code base is small, I think I can run this in the main function?
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
main()
