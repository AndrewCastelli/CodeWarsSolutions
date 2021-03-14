def spin_words(sentence):
    if len(sentence) == 0:
        return None

    words = sentence.split(" ")
    for ind, word in enumerate(words):
        if len(word) >= 5:
            word_len = len(word)
            mt_string = ""

            for i in range(1, word_len + 1):
                mt_string += word[-i]
                words[ind] = mt_string

    return " ".join(word for word in words)
