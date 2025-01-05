'''
You are gonna be given a list of lists of string and a source string

Given the source string, you should return the most common word that appears after that string

training_data = [
    ["I", "AM", "GAY"],
    ["SO", "I", "AM"]
    ["I", "LIVE", "HERE"]
]

source = "I"

Given this training data input and the source "I". The words thar appears after "I" are "am" and "live"
But, "am" appears 2 times and live only 1. So, return "am"
'''

def proccess_train_data(training_data, source):
    char_freq = {}
    for sentence in training_data:
            left = 0
            right = 1
            
            while left < right and right < len(sentence):
                print(f"left {left}")
                print(f"right {right}")
                word = sentence[left]
                neighbor = sentence[right]
                
                if word not in char_freq:
                    char_freq[word] = {neighbor : 1}
                elif neighbor not in char_freq[word]:
                    char_freq[word][neighbor] = 1
                else:
                    char_freq[word][neighbor] += 1

                left += 1
                right += 1
    print(char_freq)

    max_value = 0
    char_most_ocur = None
    if source in char_freq:
        for key, value in char_freq[source].items():
            if value > max_value:
                max_value = value
                char_most_ocur = key
        return char_most_ocur
    
    return -1
                 
training_data = [
    ["I", "AM", "GAY"],
    ["SO", "I", "AM"],
    ["I", "LIVE", "HERE"],
    ["I", "LIVE", "NOWHERE"],
    ["I", "LIVE", "NOWHERE"]
]

source = "AM"

print(proccess_train_data(training_data, source))
                
