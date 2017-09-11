# Speech Recognition
from _Verbs import *


def speech(userInput):
    keywords = verbs()
    
    sentence = []
    response = userInput.lower()
    try:
        response = response.strip(".")
        rsp_list = response.split (' ')
        sentence = [rsp_list[0], rsp_list[1], rsp_list[-2], rsp_list[-1]]
        #print(sentence)
        
        if check(sentence[0]) in keywords:
            sentence[0] = check(sentence[0])
            del sentence[1]
            #print('1', sentence)
            
        elif check(sentence[0] + sentence[1]) in keywords:
            sentence[0] = check(sentence[0] + sentence[1])
            del sentence[1]
            #print('2', sentence)
            
        else:
            #print('3')
            #print(sentence)
            pass
        
        return sentence
    
    except:
        sentence.append(response)
        return sentence



#print(speech("open the basement door"))
