from nltk.corpus import names
import nltk
from nltk.corpus import names
import random
from nltk.classify import apply_features


def gender_features(word):
    return {'last_letter': word[-1]}

def test ():
    labeled_names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
    random.shuffle(labeled_names)
    featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
    train_set = apply_features(gender_features, labeled_names[500:])
    test_set = apply_features(gender_features, labeled_names[:500])
    return train_set
