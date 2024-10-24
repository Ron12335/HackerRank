import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

def read_training_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    num_of_lines = int(lines[0].strip())
    categories = []
    documents = []
    for line in lines[1:num_of_lines + 1]:
        category, document = line.strip().split(' ', 1)
        categories.append(int(category))
        documents.append(document)
    return documents, categories

def read_input_data():
    T = int(input())  
    documents = []
    for i in range(T):
        document = input().strip()  
        documents.append(document)
    return documents

def classify_documents(training_file):
    
    train_documents, train_categories = read_training_data(training_file)
    
   
    vectorizer = TfidfVectorizer(stop_words='english', max_features=10000)
    X_train = vectorizer.fit_transform(train_documents)
    
   
    classifier = LinearSVC()
    classifier.fit(X_train, train_categories)
    
 
    test_documents = read_input_data()
    X_test = vectorizer.transform(test_documents)
    nt
    predictions = classifier.predict(X_test)
    

    for prediction in predictions:
        print(prediction)

classify_documents('trainingdata.txt')