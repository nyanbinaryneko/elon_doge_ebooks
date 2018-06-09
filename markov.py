import random
import re
from doge_enums import *


class MarkovChainer(object):
    def __init__(self, order):
        self.order = order
        self.beginnings = []
        self.freq = {}

    # pass a string with a terminator to the function to add it to the markov lists.
    def add_sentence(self, string, terminator):
        data = "".join(string)
        words = data.split()
        buf = []
        if len(words) > self.order:
            words.append(terminator)
            self.beginnings.append(words[0:self.order])
        else:
            pass

        for word in words:
            buf.append(word)
            if len(buf) == self.order + 1:
                mykey = (buf[0], buf[-2])
                if mykey in self.freq:
                    self.freq[mykey].append(buf[-1])
                else:
                    self.freq[mykey] = [buf[-1]]
                buf.pop(0)
            else:
                continue
        return

    def add_text(self, text):
        text = re.sub(r'\n\s*\n/m', ".", text)
        seps = '([.!?;:])'
        pieces = re.split(seps, text)
        sentence = ""
        for piece in pieces:
            if piece != "":
                if re.search(seps, piece):
                    self.add_sentence(sentence, piece)
                    sentence = ""
                else:
                    sentence = piece

    # Generate the goofy sentences that become your tweet.
    # edited to replace elon companies with doge equivalents

    def generate_sentence(self):
        res = random.choice(self.beginnings)
        res = res[:]
        print(len(res))
        if len(res) == self.order:
            nw = True
            while nw is not None:
                restup = (res[-2], res[-1])
                try:
                    nw = self.next_word_for(restup)
                    if nw is not None:
                        res.append(nw)
                    else:
                        continue
                except Exception:
                    nw = False
            new_res = res[0:-2]
            if new_res[0].istitle() or new_res[0].isupper():
                pass
            else:
                new_res[0] = new_res[0].capitalize()
            sentence = ""
            for word in new_res:
                self.barklonifier(word)
                #print(word)
                sentence += word + " "
            sentence += res[-2] + ("" if res[-1] in ".!?;:" else " ") + res[-1]

        else:
            sentence = None
        return sentence

    def next_word_for(self, words):
        try:
            arr = self.freq[words]
            next_words = random.choice(arr)
            return next_words
        except Exception:
            return None
    
    def barklonifier(self, word):
        elon = Elon()
        barklon = Barklon()
        updated_word = {
             elon.TESLA : barklon.FURSLA,
             elon.SPACE_X : barklon.DOGE_X,
             elon.HYPERLOOP : barklon.HYPERSCOOP,
             elon.MARS : barklon.MOON,
             elon.DRAGON : barklon.DARGON,
             elon.FALCON : barklon.FALKOR,
             elon.ELON : barklon.BARKLON,
             elon.MUSK : barklon.HUSK,
             elon.PAYPAL : barklon.PAYPAW
         }.get(word.lower(), word)

        return updated_word




if __name__ == "__main__":
    print("Try running ebooks.py first")
