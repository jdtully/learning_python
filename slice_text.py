
text = "X-DSPAM-Confidence:    0.8475"
while True: 
    atpos=text.find("0")
    print(float(text[atpos:]))
    break