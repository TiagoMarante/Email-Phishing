from functionwords import FunctionWords
from lexicalrichness import LexicalRichness
import numpy as np
import joblib

def function_words(text):
    counter_0, counter_1 = 0,0
    fw = FunctionWords(function_words_list='english')
    l1 = fw.transform(text)
    
    for elem in l1:
        if elem == 0:
            counter_0+=1
        
        if elem == 1:
            counter_1+=1
        
    return counter_1/counter_0


def vocabulary_richness(text):
    lex = LexicalRichness(text)
    return lex.Maas


def count_words(text, word):
    counter = 0
    for words in text.split(" "):
        if(words == word):
            counter += 1
    return counter


def count_words_unique(text):
    words = text.split(" ")
    return len(list(set(words)))


def count_character(text):
    counter = 0
    for char in text:
            counter += 1
    return counter


def to_lower_case(text):
    return text.lower()


def email_analysis(text):
    array_to_convert = []

    lower_text = to_lower_case(text)
    

    n_char = count_character(text)
    array_to_convert.append(n_char)

    voc_richness = vocabulary_richness(lower_text)
    array_to_convert.append(voc_richness)

    words = to_lower_case("Account,Access,Bank,Credit,Click,Identity,Inconvenience,Information,Limited,Minutes,Password,Recently,Risk,Social,Security,Service,Suspended")


    for word in words.split(","):
        counter = count_words(lower_text, word)
        array_to_convert.append(counter)

    
    fun_words = function_words(lower_text)
    array_to_convert.append(fun_words)

    unique_words = count_words_unique(lower_text)
    array_to_convert.append(unique_words)

    model = joblib.load("../fastapi-master/app/ML model/trainedForest.joblib")

    is_spam = model.predict_proba(np.array([array_to_convert]))
    print(is_spam)


    print(array_to_convert)
