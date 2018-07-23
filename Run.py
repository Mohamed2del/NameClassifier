
import nltk
from Train import gender_features
from Train import test

train_set = test()
classifier = nltk.NaiveBayesClassifier.train(train_set)
ok = "y"
while (ok == "y"):
    name = input("Enter Name For The Classification :")
    print(classifier.classify(gender_features(name)))
    ok = input ("\n Again ? (y) or (n)")
