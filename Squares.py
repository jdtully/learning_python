def count_char(text, char):
    text="a rat in the house may eat the iced cream"
    count = 0
    for c in text:
        if c == char:
            count += 1
            return (count)
        else:
            print("letter is not in string")
    print(count)
  