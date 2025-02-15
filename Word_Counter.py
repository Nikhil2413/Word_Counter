def word_counter():
    print("Enter your text (Press Enter on an empty line to finish):\n")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    text = " ".join(lines)
    words = text.split()
    word_count = len(words)
    print(f"\nTotal word count: {word_count}")
    
word_counter()
