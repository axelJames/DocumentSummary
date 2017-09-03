
def ExtractDocument(File):
    inputfile = open(File, "r")
    content = inputfile.read()
    paragraph = Paragraph(content)


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
        self.SummeryPhrases()
    def __str__(self):
        ret = "text= {} \nscore= {} \n".format(self.text, self.score)
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
                self.score += 10
    def Updatescore(self, words):
        for word in words.keys():
            if word in self.text:
                self.score += words[word].score
                
class Paragraph(object):
    def __init__(self,content):
        self.text = " ".join(content.splitlines())
        words = self.RemoveStopword()
        self.words = self.repetitionWord(words)
        self.NamedEntity()
        self.sentences = self.FindSentences(self.text)
    def FindSentences(self, text):
        q = find_all(text, ".")
        sentenses = []
        i_prev = 0
        for i in q:
            sentence = Sentence(text[i_prev:i], 5 if (i_prev == 0 or i==(len(text)-1)) else 0)
            sentence.Updatescore(self.words)
            sentenses.append(sentence)
            i_prev = i+1
        print sentenses
        return sentenses
    @staticmethod
    def repetitionWord(words):
        WordsSet = {}
        for word in set(words):
            if word == "-":
                continue
            WordsSet[word] = Word(word)
            WordsSet[word].AddRepeat(words.count(word))
        return WordsSet
    def NamedEntity(self):
        for word in self.words.keys():
            if word[0].isupper():
                self.words[word].Name_Entity = True
                self.words[word].UpdateScore(1.5)
                
    def RemoveStopword(self):
        wordsfile = open("StopWords.txt", "r")
        Stopword = wordsfile.read()
        StopWord = Stopword.splitlines()
        words = self.text.split()
        for i in range(len(words)):
            if words[i].lower() in StopWord:
                words[i] = "-"
        return words

class Word(object):
    def __init__(self, word):
        self.text = word
        self.repeat = 0
        self.score = 0.5
        self.Named_Entity = False
    def UpdateScore(self, score):
        self.score = score * self.repeat
    def AddRepeat(self, count):
        self.repeat += count
        self.UpdateScore(self.score)
if __name__ == "__main__":
    ExtractDocument("Document.txt")
