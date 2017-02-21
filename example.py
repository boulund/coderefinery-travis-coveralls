
def reverse_words(s):
    """
    Reverses order or words in string s.
    """
    words = s.split()
    words_reversed = words[::-1]
    return ' '.join(words_reversed)


def test_reverse_words():
    assert reverse_words('dogs hate cats') == 'cats hate dogs'
    assert reverse_words('dog eat dog') == 'dog eat dog'
    assert reverse_words('one two three four') == 'four three two one'


def get_word_lengths(s):
    """
    Returns a list of integers representing
    the word lengths in string s.
    """
    return [len(word) for word in s.split()]


# uncomment this function in step 6
def test_get_word_lengths():
    text = "Three tomatoes are walking down the street"
    assert get_word_lengths(text) == [5, 8, 3, 7, 4, 3, 6]


def obscure_function():
    """
    Example of a function that is never tested.
    """
    def do_something_strange():
        return 0
    return do_something_strange()

def test_obscure_functio():
    assert(obscure_function() == 0)
