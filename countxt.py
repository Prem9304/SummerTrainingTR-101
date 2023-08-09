# 15.	Python program to Count the Number of Words in a Text file.
def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print("File not found.")
        return 0

file_path = input("Enter the path of the text file: ")
word_count = count_words(file_path)
print(f"Number of words in the file: {word_count}")
