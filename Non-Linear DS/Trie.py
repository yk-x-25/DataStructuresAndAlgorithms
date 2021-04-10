class TrieNode:

    def __init__(self,char):
        self.Character = char 
        self.NextCharacters =[None for _ in range(200)]
        self.eow=False
        self.wordsAfter = 0

def convertCharacterToArrayIndex(Character):
    return ord(Character)-ord('a')
    
class Trie:

    def __init__(self,IgnoreCase=True):
        self.root=TrieNode("")

    def insert(self,word):
        node= self.root
        for i in word:
            index = convertCharacterToArrayIndex(i)
            if not node.NextCharacters[index] :
                node.NextCharacters[index] = TrieNode(i)
            
            node = node.NextCharacters[index]

        node.eow = True
        node.wordsAfter += 1 

    def dfs(self,node=None ,res=[],searchWord=""):

        if not node:
            node = self.root
        for child in node.NextCharacters:
            if child:
                res.append(child.Character)
                if child.eow:
                    wordAtThisPoint = "".join(res)
                    if wordAtThisPoint.startswith(searchWord):
                        print(wordAtThisPoint)

                
                self.dfs(child,res,searchWord)
                res.pop()

    def searchQueries(self,startingWord):
        node = self.root
        self.dfs(node,[],startingWord)

        

rootNode = Trie()

words = ["Yukesh is a Billionaire","Yukesh is a Coder","Yukesh is a software engineer","Yukesh is a Cricketer","Yukesh is a singer","Yukesh is a Investor","Yukesh's height","Yukesh's weight","Yukesh's inpiration"]
for i in words:
    rootNode.insert(i.lower())



inputUntilNow=""
endLoop = False
while not endLoop:
    inp=input()
    if inp =="exit":
        endLoop =True
    if inp=="clear":
        inputUntilNow=""
        continue
    inputUntilNow+=inp
    rootNode.searchQueries(inputUntilNow.lower())