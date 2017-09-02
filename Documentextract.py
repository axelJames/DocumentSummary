import string

def ExtractDocument(File):
    inputfile = open(File, "r")
    content = inputfile.read()
    para = content.splitlines()
    paragraph = []
    for text in para:
        paragraph.append(Paragraph(text))


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            break
        yield start
        start += len(sub)

class Sentence(object):
    def __init__(self, text, score=0):
        self.text = text
        self.score = score
        self.words = self.Filterword(self.text)
    @staticmethod
    def Filterword(content):
        prepositions = ["to", "from", "by", "is", "that", "a", "as", "of", "In" ]
        words = content.split()
        for i in range(len(words)):
            if words[i] in prepositions:
                words[i] = string.upper(words[i])
        return words
    def __str__(self):
        ret = "text= {} \nscore= {} \nwords={}\n".format(self.text, self.score, self.words)
        return ret        
    __repr__ = __str__
    
class Paragraph(object):
    def __init__(self,text):
        self.text = text
        self.sentences = self.FindSentences(text)
    @staticmethod
    def FindSentences(text):
        q = find_all(text, ".")
        sent = []
        i_prev = 0
        for i in q:
            sent.append(Sentence(text[i_prev:i], 10 if i_prev == 0 else 0))
            i_prev = i+1
        return sent

if __name__ == "__main__":
    ExtractDocument("Document.txt")
