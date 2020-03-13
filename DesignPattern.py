class Logo:
    #This function lets user to enter a sentence
    def enterSentence(self):
        enteredSentence = input("Enter the sentence for the logo: ")
        return enteredSentence
    
    #This function will split the sentence into words and will return all the words in a list
    def splitSentence(self, sentence):
        splitlist = sentence.split()
        return splitlist
    
    #This function will return the first letters of the elements in the list
    def getLogoString(self, sentenceList):
        logo = [x[0] for x in sentenceList]
        return logo
    
    #This function will print the logo by combining all the letters
    def printLogo(self, logoString):
        print("".join(logoString))
        
class LogoFacade():
    def __init__(self):
        self.logo = Logo()

    def start(self):
        userInput = self.logo.enterSentence()
        splitListOfInput = self.logo.splitSentence(userInput)
        stringLetters = self.logo.getLogoString(splitListOfInput)
        self.logo.printLogo(stringLetters)
        
    
logo_facade = LogoFacade()
logo_facade.start()
