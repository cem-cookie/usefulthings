"""collection of tiny tools for everyday things"""

class ASCII:
    def dump(sentence):
        """take a sentence and transform into ascii stream"""
        ascii_reps = map(lambda c : str(ord(c)), list(sentence))
        ascii_sentence = " ".join(ascii_reps)
        return ascii_sentence

    def load(ascii_text):
        """take ascii stream and transform into python string"""
        integers = [int(i) for i in ascii_text.split(" ")]
        string_form = "".join(map(chr, integers))
        return string_form

