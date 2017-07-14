import random

noun_list = ["dog", "cat", "giraffe", "computer", "donut", "dress", "cupcake", "television", "car", "phone"]
verb_list = ["hops", "runs", "walks", "moans", "stretched", "watches", "sleeps", "eats", "relaxes", "codes"]
adj_list = ["silly", "hot", "red", "clean", "happy", "pleasant", "dark", "comfortable", "serious", "proud"]
adv_list = ["quickly", "lazily", "angrily", "sadly", "joyfully", "merrily", "joyfully"]
prep_list = ["under", "over", "through", "behind", "next to", "beneath", "beside", "around", "atop", "in front"]
article_list = ["a", "the"]

def noun_phrase():
    return random.choice(article_list) + " " + \
    random.choice(adj_list) + " " + \
    random.choice(noun_list)

def verb_phrase():
    return random.choice(adv_list) + " " + \
    random.choice(verb_list)

def prep_phrase():
    return random.choice(prep_list) + " " + \
    random.choice(article_list) + " " + \
    random.choice(noun_list)

def sentence():
    return noun_phrase() + " " + verb_phrase() + " " + prep_phrase()

print(sentence())

'''
print(noun_phrase())
print(verb_phrase())
print(prep_phrase())
'''
