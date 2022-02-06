from textblob import TextBlob
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer

# Sentiment Analysis
from dataClean import Clean
from dataGather import *


class Analysis():
    def percentage(self, part, whole):
        return 100 * float(part) / float(whole)

    def count_values_in_column(self, data, feature):
        total = data.loc[:, feature].value_counts(dropna=False)
        percentage = round(data.loc[:, feature].value_counts(dropna=False, normalize=True) * 100, 2)
        return pd.concat([total, percentage], axis=1, keys=['Total', 'Percentage'])

    def main(self, tweets, noOfTweet):
        tweet_list = pd.read_csv('Clean.csv')
        tw_list = pd.DataFrame(tweet_list[["text"]])

        # tw_list["text"] = tw_list["0"]

        positive = 0
        negative = 0
        neutral = 0
        polarity = 0
        neutral_list = []
        negative_list = []
        positive_list = []

        for tweet in tweets:
            analysis = TextBlob(tweet.text)
            score = SentimentIntensityAnalyzer().polarity_scores(tweet.text)

            neg = score['neg']
            neu = score['neu']
            pos = score['pos']
            comp = score['compound']
            polarity += analysis.sentiment.polarity

            if neg > pos:
                negative_list.append(tweet.text)
                negative += 1
            elif pos > neg:
                positive_list.append(tweet.text)
                positive += 1
            elif pos == neg:
                neutral_list.append(tweet.text)
                neutral += 1

        positive = self.percentage(positive, noOfTweet)
        negative = self.percentage(negative, noOfTweet)
        neutral = self.percentage(neutral, noOfTweet)
        polarity = self.percentage(polarity, noOfTweet)
        positive = format(positive, '.1f')
        negative = format(negative, '.1f')
        neutral = format(neutral, '.1f')

        # Number of Tweets (Total, Positive, Negative, Neutral)
        neutral_list = pd.DataFrame(neutral_list)
        negative_list = pd.DataFrame(negative_list)
        positive_list = pd.DataFrame(positive_list)
        print("positive number: ", len(positive_list))
        print("negative number: ", len(negative_list))
        print("neutral number: ", len(neutral_list))

        # Calculating Negative, Positive, Neutral and Compound values
        tw_list[['polarity', 'subjectivity']] = tw_list["text"].apply(lambda Text: pd.Series(TextBlob(Text).sentiment))

        for index, row in tw_list['text'].iteritems():
            score = SentimentIntensityAnalyzer().polarity_scores(row)
            neg = score['neg']
            neu = score['neu']
            pos = score['pos']
            comp = score['compound']
            if neg > pos:
                tw_list.loc[index, 'sentiment'] = "negative"
            elif pos > neg:
                tw_list.loc[index, 'sentiment'] = "positive"
            else:
                tw_list.loc[index, 'sentiment'] = "neutral"
            tw_list.loc[index, 'neg'] = neg
            tw_list.loc[index, 'neu'] = neu
            tw_list.loc[index, 'pos'] = pos
            tw_list.loc[index, 'compound'] = comp


        tw_list.head(10)
        # print(tw_list.head(10))
        # Creating new data frames for all sentiments (positive, negative and neutral)
        tw_list_negative = tw_list[tw_list["sentiment"] == "negative"]
        tw_list_positive = tw_list[tw_list["sentiment"] == "positive"]
        tw_list_neutral = tw_list[tw_list["sentiment"] == "neutral"]

        # Count_values for sentiment
        self.count_values_in_column(tw_list, "sentiment")

        # Calculating tweet’s lenght and word count
        tw_list['text_len'] = tw_list['text'].astype(str).apply(len)
        tw_list['text_word_count'] = tw_list['text'].apply(lambda x: len(str(x).split()))
        round(pd.DataFrame(tw_list.groupby("sentiment").text_len.mean()), 2)
        round(pd.DataFrame(tw_list.groupby("sentiment").text_word_count.mean()), 2)

        # Appliyng Countvectorizer
        cl = Clean()
        countVectorizer = CountVectorizer(analyzer=cl.clean_text)
        countVector = countVectorizer.fit_transform(tw_list['text'])
        print('{} Number of reviews has {} words'.format(countVector.shape[0], countVector.shape[1]))
        count_vect_df = pd.DataFrame(countVector.toarray(), columns=countVectorizer.get_feature_names())

        # Most Used Words
        count = pd.DataFrame(count_vect_df.sum())
        countdf = count.sort_values(0, ascending=False).head(20)


        # Final Dataframe
        power = pd.DataFrame(tw_list[['text', 'compound', 'sentiment']])
        print(power.head(10))
        power.to_csv('Analysed.csv')
