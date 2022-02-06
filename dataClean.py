import pandas as pd
import nltk
import re
import string

from dataGather import tweet_list

# Appliyng Stemmer
ps = nltk.PorterStemmer()

language = ['arabic',
            'azerbaijani',
            'danish',
            'dutch',
            'english',
            'finnish',
            'french',
            'german',
            'greek',
            'hungarian',
            'indonesian',
            'italian',
            'kazakh',
            'nepali',
            'norwegian',
            'portuguese',
            'romanian',
            'russian',
            'slovene',
            'spanish',
            'swedish',
            'tajik',
            'turkish']
# Removing stopwords
stopword = nltk.corpus.stopwords.words(language)


class Clean():
    def load_data(self):
        data = pd.read_csv('Gather.csv')
        return data

    # Removing Punctuation
    def remove_punct(self, text):
        text = "".join([char for char in text if char not in string.punctuation])
        text = re.sub('[0-9]+', '', text)
        return text

    # Appliyng tokenization
    def tokenization(self, text):
        text = re.split('\W+', text)
        return text

    def remove_stopwords(self, text):
        text = [word for word in text if word not in stopword]
        return text

    def stemming(self, text):
        text = [ps.stem(word) for word in text]
        return text

    # Cleaning Text
    def clean_text(self, text):
        text_lc = "".join([word.lower() for word in text if word not in string.punctuation])  # remove puntuation
        text_rc = re.sub('[0-9]+', '', text_lc)
        tokens = re.split('\W+', text_rc)  # tokenization
        text = [ps.stem(word) for word in tokens if word not in stopword]  # remove stopwords and stemming
        return text

    def main(self):
        # tweet_list = load_data()
        tweet_list = pd.read_csv('Gather.csv')
        tw_list = pd.DataFrame(tweet_list[["0"]])

        tw_list["text"] = tw_list["0"]

        # Removing RT, Punctuation etc
        remove_rt = lambda x: re.sub('RT @\w+: ', " ", x)
        rt = lambda x: re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", x)
        tw_list["text"] = tw_list.text.map(remove_rt).map(rt)
        tw_list["text"] = tw_list.text.str.lower()
        tw_list.head(10)
        # print(tw_list.head())

        """tw_list['punct'] = tw_list['text'].apply(lambda x: remove_punct(x))
        tw_list['tokenized'] = tw_list['punct'].apply(lambda x: tokenization(x.lower()))
        tw_list['nonstop'] = tw_list['tokenized'].apply(lambda x: remove_stopwords(x))
        tw_list['stemmed'] = tw_list['nonstop'].apply(lambda x: stemming(x))
        tw_list['Tweet cleaned'] = tw_list['text'].apply(lambda x: clean_text(x))"""
        # print(tw_list.head())

        dff = pd.DataFrame(tw_list[['text']])
        # print(dff.head(10))
        dff.to_csv('Clean.csv')
