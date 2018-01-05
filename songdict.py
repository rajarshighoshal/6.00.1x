def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

sheLovesYou = ['She', 'loves', 'you', 'yeah', 'yeah', 'yeah'
'She', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'She', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'You', 'think', "you've", 'lost', 'your', 'love'
'Well', 'I', 'saw', 'her', 'yesterday-yi-yay',
"It's", 'you', "she's", 'thinking', 'of',
'And', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',
'She', 'says', 'she', 'loves', 'you',
'And', 'you', 'know', 'that', "can't", 'be', 'bad',
'Yes', 'she', 'loves', 'you',
'And', 'you', 'know', 'you', 'should', 'be', 'glad',
'She', 'said', 'you', 'hurt', 'her', 'so',
'She', 'almost', 'lost', 'her', 'mind',
'And', 'now', 'she', 'says', 'she', 'knows',
"You're", 'not', 'the', 'hurting', 'kind',
'She', 'says', 'she', 'loves', 'you',
'And', 'you', 'know', 'that', "can't", 'be', 'bad',
'Yes', 'she', 'loves', 'you',
'And', 'you', 'know', 'you', 'should', 'be', 'glad',
'Oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'She', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'With', 'a', 'love', 'like', 'that',
'You', 'know', 'you', 'should', 'be', 'glad',
'You', 'know', "it's", 'up', 'to', 'you',
'I', 'think', "it's", 'only', 'fair',
'Pride', 'can', 'hurt', 'you', 'too',
'Apologize', 'to', 'her',
'Because', 'she', 'loves', 'you',
'And', 'you', 'know', 'that', "can't", 'be', 'bad',
'Yes', 'she', 'loves', 'you',
'And', 'you', 'know', 'you', 'should', 'be', 'glad',
'Oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'She', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'With', 'a', 'love', 'like', 'that',
'You', 'know', 'you', 'should', 'be', 'glad',
'With', 'a', 'love', 'like', 'that',
'You', 'know', 'you', 'should', 'be', 'glad',
'With', 'a', 'love', 'like', 'that',
'You', 'know', 'you', 'should', 'be', 'glad',
'Yeah', 'yeah', 'yeah',
'Yeah', 'yeah', 'yeah', 'yeah']

beatles = lyrics_to_frequencies(sheLovesYou)

def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    
    words = []
    
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    
    return(words, best)

def words_often(freqs, miniTimes):
    result = []
    done = False
    
    while not done:
        temp  = most_common_words(freqs)
        if temp[1] >= miniTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result

print(words_often(beatles, 5))