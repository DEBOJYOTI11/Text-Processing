def gender_features(word):
    return {'last_letter': word[-1]}

from nltk.corpus import names

labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
    [(name, 'female') for name in names.words('female.txt')])

import random
import nltk
random.shuffle(labeled_names)

featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)


print(classifier.classify(gender_features('neo')))
print(nltk.classify.accuracy(classifier, test_set))
print(classifier.show_most_informative_features(5))
