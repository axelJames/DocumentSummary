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
    def __init__(self, text, score=0, Named_Entities=None):
        self.text = text
        self.score = score
        self.words = self.RemoveStopword()
        self.SummeryPhrases()
        for word in self.words:
            if word in Named_Entities.keys():
                self.score += Named_Entities[word]
                
    def RemoveStopword(self):
        wordsfile = open("StopWords.txt", "r")
        Stopword = wordsfile.read()
        StopWord = Stopword.splitlines()
        words = self.text.split()
        for i in range(len(words)):
            if words[i].lower() in StopWord:
                words[i] = "-"
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
            
class Paragraph(object):
    def __init__(self,text):
        self.text = text
        self.Named_Entities = self.repetitionWord()
        self.sentences = self.FindSentences(text)
    def FindSentences(self, text):
        q = find_all(text, ".")
        sen = []
        i_prev = 0
        for i in q:
            sen.append(Sentence(text[i_prev:i], 10 if (i_prev == 0 or i==(len(text)-1)) else 0, self.Named_Entities))
            i_prev = i+1
        print sen
        return sen
    def repetitionWord(self):
        words = self.text.split()
        Name_Entities = self.NamedEntity()
        wordset = {}
        for word in words:
            if word in Name_Entities:
                if word in wordset:
                    wordset[word]+=1
                else:
                    wordset[word]=1
        return wordset
    def NamedEntity(self):
        list1 = []
        words = self.text.split()
        for word in words:
            if word[0].isupper():
                list1.append(word)
        return list1
    


if __name__ == "__main__":
    ExtractDocument("Document.txt")
