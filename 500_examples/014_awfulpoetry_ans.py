import sys
import random

lines = 5
if len(sys.argv) > 1:
    try:
        temp = int(sys.argv[1])
        if 1 <= temp <= 10:
            lines = temp
        else:
            raise Exception('1 <= lines <= 10')
    except Exception as err:
        print(err,'usage: awfulpoetry1_ans.py [lines]', sep='\n')
        sys.exit(0)
    
articles = ["the", "a", "another", "her", "his"]
subjects = ["cat", "dog", "horse", "man", "woman", "boy", "girl"]
verbs    = ["sang", "ran", "jumped", "said", "fought", "swam", "saw"]
adverbs  = ["loudly", "quietly", "quickly", "slowly", "well", "badly"]

while lines:
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    if random.randint(0, 1):
        adverb = random.choice(adverbs)
        print(article, subject, verb, adverb)
    else:
        print(article, subject, verb)
    
    lines -= 1