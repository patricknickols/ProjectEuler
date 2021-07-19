import inflect
p = inflect.engine()

def word(number):
    return p.number_to_words(number)

def letter_count(number):
    text = word(number)
    text = text.replace(" ", "")
    text = text.replace("-", "")
    return len(text)

def main():
    count = 0
    for i in range(1, 1001):
        count += letter_count(i)
    print(count)

if __name__ == "__main__":
    main()
