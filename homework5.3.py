text = input("Write your text " )
cleaned_text = ''.join(char for char in text if char.isalpha() or char.isspace())
words = cleaned_text.split()
capital_letters = [item.title() for item in words]
hashtag = "#" + "".join(capital_letters)
if len(hashtag) > 140:
    hashtag = hashtag[:140]
print(hashtag)
