import unittest

def count_words(text):
    words = text.split()
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count


 
if __name__ == '__main__':
    unittest.main()