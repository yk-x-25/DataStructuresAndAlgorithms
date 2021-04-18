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

    def dfs(self,node=None ,res=[],searchWord="",words=[]):

        if not node:
            node = self.root
        for child in node.NextCharacters:
            if child:
                res.append(child.Character)
                if child.eow:
                    wordAtThisPoint = "".join(res)
                    if wordAtThisPoint.startswith(searchWord):
                        words.append(wordAtThisPoint)
                        #print(wordAtThisPoint)

                
                self.dfs(child,res,searchWord,words)
                res.pop()

    def searchQueries(self,startingWord):
        node = self.root
        words = []
        self.dfs(node,[],startingWord,words)
        return words

def BuildTrie():
    rootNode = Trie()

    words = ["Yukesh is a Billionaire ?","Yukesh's codechef rating","is Yukesh a good engineer","Yukesh is a Cricket analyst?","Does Yukesh sing good","Yukesh is an Investor?","Yukesh's height","Yukesh's inpiration","Will Google hire yukesh?", "when did yukesh join grab?","Yukesh's networth","yukesh works for Google or Grab?"]
    for i in words:
        rootNode.insert(i.lower())
    return rootNode


# if __name__=="__main__":
#     root = BuildTrie()
#     print(root.searchQueries("yukesh"))