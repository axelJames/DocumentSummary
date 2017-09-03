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
        self.SummeryPhrases()
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
    def SummeryPhrases(self):
        summ_phra = ["after all",
                     "all in all",
                     "all things considered",
                     "briefly",
                     "by and large",
                     "in any case",
                     "in any event",
                     "in brief",
                     "in conclusion",
                     "on the whole",
                     "in short",
                     "in summary",
                     "in the final analysis",
                     "in the long run, on balance",
                     "to sum up",
                     "to summarize",
                     "finally"]
        for phrase in summ_phra:
            if phrase in self.text:
                self.score += 5
    def NamedEntity(self):
        list1 = []
        words = self.text.split()
        if ([word[0].isupper() for word in words]):
            list1.append(word)
        return list1
        
            
class Paragraph(object):
    def __init__(self,text):
        self.text = text
        self.sentences = self.FindSentences(text)
        self.wordset = self.repetitionWord()
    @staticmethod
    def FindSentences(text):
        q = find_all(text, ".")
        sen = []
        i_prev = 0
        for i in q:
            sen.append(Sentence(text[i_prev:i], 10 if (i_prev == 0 or i==(len(text)-1)) else 0))
            i_prev = i+1
        print sen
        return sen
    def repetitionWord(self):
        words = self.text.split()
        wordset = {}
        for word in words:
            if word in wordset:
                wordset[word]+=1
            else:
                wordset[word]=1
        return wordset
            


if __name__ == "__main__":
    ExtractDocument("Document.txt")
