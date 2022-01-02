#! python3

import pyinputplus as pyip
import re

sentence = "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."
adjRegex = re.compile(r"ADJECTIVE")
nounRegex = re.compile(r"NOUN")
verbRegex = re.compile(r"VERB")
adj = pyip.inputStr("Enter an adjective:\n")
sentence = adjRegex.sub(adj, sentence)
noun = pyip.inputStr("Enter a noun:\n")
sentence = nounRegex.sub(noun, sentence, count=1)
verb = pyip.inputStr("Enter a verb:\n")
sentence = verbRegex.sub(verb, sentence)
noun1 = pyip.inputStr("Enter a noun:\n")
sentence = nounRegex.sub(noun1, sentence, count=2)

txtFile = open("madLibs.txt", "w+")
txtFile.write(sentence)
txtFile.close()