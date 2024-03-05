def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        wordCount = printWords(file_contents.split())
        letterCount = countLetters(file_contents.lower().split())
        listOfDict = convertToListOfDict(letterCount)
        listOfDict.sort(reverse=True, key=sort_on)
        printReport(wordCount, listOfDict)

def sort_on(dict):
    return dict["count"]

def printWords(words):
    wordCount = len(words)
    print(wordCount)
    return wordCount

def countLetters(words):
    letters = {}
    for word in words:
        for c in word:
            letters[c] = 1 + letters.get(c, 0)
    
    print(letters) 
    return letters

def convertToListOfDict(letterCount):
    letterList = []
    for letter, count in letterCount.items():
        if letter.isalpha():
            letterList.append({"letter" : letter, "count" : count})
    return letterList
        

def printReport(words, letters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document\n")
    for letter in letters:
        print(f"The '{letter["letter"]}' character was found {letter["count"]} times")
    print("--- End report ---")
    

if __name__ == '__main__':
    main()