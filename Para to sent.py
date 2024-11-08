import re

def segment_text(text):
   
    pattern = r'(\.|\?|\!)(?=(\s|\"|\'|\)|$))'

    
    sentences = re.split(pattern, text)
    
    
    segmented_sentences = []
    current_sentence = ""
    for part in sentences:
        if part and re.match(pattern, part):  
            current_sentence += part
            segmented_sentences.append(current_sentence.strip())
            current_sentence = ""
        elif part:
            current_sentence += part
    
  
    for sentence in segmented_sentences:
        if sentence: 
            print(sentence)


text = input("Enter text: ")


segment_text(text)

