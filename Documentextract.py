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
    def RemoveStopWords(content):
        stopwords = array("a", "about", "above", "above", "across", "after", "afterwards", "again",
                          "against", "all", "almost", "alone", "along", "already", "also","although",
                          "always","am","among", "amongst", "amoungst", "amount",  "an", "and",
                          "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", 
                          "around", "as",  "at", "back","be","became", "because","become","becomes", 
                          "becoming", "been", "before", "beforehand", "behind", "being", "below", 
                          "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", 
                          "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", 
                          "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", 
                          "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", 
                          "enough", "etc", "even", "ever", "every", "everyone", "everything", 
                          "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", 
                          "first", "five", "for", "former", "formerly", "forty", "found", "four", 
                          "from", "front", "full", "further", "get", "give", "go", "had", "has", 
                          "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", 
                          "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", 
                          "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", 
                          "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", 
                          "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", 
                          "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", 
                          "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", 
                          "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", 
                          "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", 
                          "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", 
                          "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", 
                          "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", 
                          "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", 
                          "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", 
                          "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", 
                          "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", 
                          "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", 
                          "though", "three", "through", "throughout", "thru", "thus", "to", "together", 
                          "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", 
                          "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", 
                          "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", 
                          "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", 
                          "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", 
                          "within", "without", "would", "yet", "you", "your", "yours", "yourself", 
                          "yourselves", "the");
        return words
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
