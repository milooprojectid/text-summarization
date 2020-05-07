import numpy as np
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import nltk
import re
import os


# nltk.download('punkt')
class Preprocessing(object):

    def __init__(self):
        self.factory = StemmerFactory()
        self.stemmer = self.factory.create_stemmer()
        self.stopwords = [line.rstrip('\n\r') for line in open('/home/alo-tedy/Documents/myProject/summarization/utils/stopwords.txt')]


    def casefolding(self, sentence):
        """
        Transform words from uppercase into lowercase and remove characters other than letters.

        :param sentence: sentence that will be transform
        :return: lowercase sentence and only contain letters
        """
        sentence = sentence.lower()
        sentence = re.sub(r'[^a-z]', ' ', re.sub("’", '', sentence))
        return sentence

    def tokenization(self, sentence):
        """
        Split the sentence into list of token.

        :param sentence: sentence
        :return: list of sentence
        """
        return sentence.split()

    def stopword_removal(self, token):
        """
        Remove stopword in words list using stopword list.

        :param token: list of words
        :return: token that not in stopword list
        """
        temp = []
        for i in range(len(token)):
            if token[i] not in self.stopwords:
                temp.append(token[i])
        return temp

    def stemming(self, tokens):
        """
        Transform words into root words using Nazief-Andriani Stemming algorithm

        :param tokens: list of words
        :return: list of words that has been transform into root words
        """
        for i in range(len(tokens)):
            tokens[i] = self.stemmer.stem(tokens[i])
        return tokens

    def remove_escape(self, d):
        d = d.split('\\')
        d = ' '.join(d)
        return d

    def remove_url(self, d):
        """
        Remove URL in text

        :param d: document
        :return:
        """
        d = d.split()
        i = 0
        while i < len(d):
            if 'https://' in d[i]:
                d.remove(d[i])
                i -= 1
            elif 'http://' in d[i]:
                d.remove(d[i])
                i -= 1
            i += 1

        d = ' '.join(d)
        return d

    def remove_punctuation(self, d):
        d = d.split()
        i = 0
        while i < len(d):
            if len(d) > 0:
                if d[i][0] == 'x' and len(d[i]) == 3:
                    d.remove(d[i])
                    i -= 1
            if len(d) > 0:
                if len(d[i]) == 1:
                    d.remove(d[i])
                    i -= 1
            if len(d) > 0:
                if 'rt' in d[i]:
                    d.remove(d[i])
                    i -= 1
            i += 1
        d = ' '.join(d)
        return d

    def join_input(self, newslist):
        result = ''.join(newslist)
        return result

    # @classmethod
    # def fit():
    #     return "result"



def sentence_split(paragraph):
    """
    Split the paragraph/documents into sentences.

    :param paragraph: text documents
    :return: list of sentences
    """

    return nltk.sent_tokenize(paragraph)


def word_freq(data):
    """
    Count frequency for each words in the documents.

    :param data: text documents
    :return: frequency for each words
    """
    w = []
    for sentence in data:
        for words in sentence:
            w.append(words)
    bag = list(set(w))
    res = {}
    for word in bag:
        res[word] = w.count(word)
    return res


def fit(paragraph):
    """
    Predict Summarization from documents

    :param paragraph : string of news
    :return : sentence of summarization
    """

    pre = Preprocessing()

    sentence_list = sentence_split(paragraph)
    data = []
    for i in range(len(sentence_list)):
        data.append(pre.stemming(pre.stopword_removal(pre.tokenization(pre.casefolding(sentence_list[i])))))
    data = (list(filter(None, data)))

    wordfreq = word_freq(data)

    ranking = []
    for words in data:
        temp = 0
        for word in words:
            temp += wordfreq[word]
        ranking.append(temp)

    sort_list = sorted(range(len(ranking)), key=ranking.__getitem__, reverse=True)
    n = 1
    sentence = ''
    for i in range(n):
        sentence += '{}'.format(sentence_list[sort_list[i]])
    return sentence