import random

#download information will be used from files

commonQuestions = []
commonAnswers = []
questionsWithPattern = []
answersWithPattern = []
invitePhrases = []
byePhrases = []
words = []

isQuestion = lambda sentence: sentence.find("?") != -1
containsPattern = lambda sentence: sentence.find("*") != -1

def downloadPatterns(filename) :
	f = open(filename, "r")
	for text in f:
		if isQuestion(text):
			if containsPattern(text) :
				questionsWithPattern.append(text[:-1])
			else :
				commonQuestions.append(text[:-1])
		else :
			if containsPattern(text) :
				answersWithPattern.append(text[:-1])
			else :
				commonAnswers.append(text[:-1])
	f.close()


def downloadWords(filename) :
	f = open(filename, "r")
	for x in f:
		words.append(x[:-1])
	f.close()
	random.shuffle(words)

def downloadInvitePhrases(filename) :
	f = open(filename, "r")
	for x in f:
		invitePhrases.append(x[:-1])
	f.close()

def downloadByePhrases(filename) :
	f = open(filename, "r")
	for x in f:
		byePhrases.append(x[:-1])
	f.close()

def init():
	downloadWords("nouns.txt")
	downloadPatterns("patterns.txt")
	downloadInvitePhrases("hello.txt")
	downloadByePhrases("bye.txt")

#answer algorithms

def findWordWithMaximalOccurencesNumber(text):
	result = ""
	resultCount = 0
	for word in words:
		count = text.count(word)
		if count != 0 and resultCount < count:
			resultCount = count
			result = word

	return result

lastAnswer = ""

def getCommonAnswer(common):
	answer = random.choice(common)
	while answer == lastAnswer :
		answer = random.choice(common)
	return answer

def match(text, common, withPatterns):
	answer = ""
	keyword = findWordWithMaximalOccurencesNumber(text)
	if keyword == "" or random.randint(0, 10) < 3:
		return getCommonAnswer(common)
	else :
		return random.choice(withPatterns).replace("*", keyword)


isInvitePhrase = lambda s: s.lower().find("hello") != -1 or s.lower().find("hi") != -1 or s.lower().find("hey") != -1

def response(text):
	if lastAnswer == "" and isInvitePhrase(text) :
		return random.choice(invitePhrases)
	if text.lower().find("bye") != -1:
		return random.choice(byePhrases)
	if isQuestion(text):
		return match(text, commonAnswers, answersWithPattern) 
	else:
		return match(text, commonQuestions, questionsWithPattern) 

init()

print(len(words))

print("Hello, Biba, lets talk! Enter what you want to say below.")

while lastAnswer.lower().find("bye") == -1:
	s = input("Biba:")
	answer = response(s)
	print("Boba: " + answer)
	lastAnswer = answer

