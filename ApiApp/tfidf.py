import re
from string import punctuation
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pymongo
import math
from collections import defaultdict

# preprocess the query string
stop_words = set(stopwords.words('english'))
def preprocess(sentences, stop=True, stemming=True):
    stem = PorterStemmer()
    sentences = re.sub(f'[{punctuation}]', ' ', sentences)
    tokens = word_tokenize(sentences.lower())
    tokens = [token for token in tokens if token not in stop_words] if stop else tokens
    tokens = [stem.stem(token) for token in tokens] if stemming else tokens

    return tokens


def TFIDF(query):
    query_pro = preprocess(query)

    client = pymongo.MongoClient("mongodb+srv://zhou:0219@cluster0.kwwqk4a.mongodb.net/?retryWrites=true&w=majority")
    db =client['ttds']
    score = defaultdict(float)

    # total_cnt: the number of documents
    total_cnt = 100000

    for term in query_pro:
        departments = db['invertIndex'].find({'token': term})
        result = []

        for department in departments:
            result.append({
                'tokenaa':  department['token'],
                'documentcount': department['docCount'],
                'docposition': department['docPos'],
            })

        # calculate tfidf
        # TF = Frequency of term in document
        # IDF = lg(Total number of docs/ Number of docs in which term appears)
        IDF = math.log(total_cnt / (result[0]['documentcount']+1))
        for key, value in result[0]['docposition'].items():
            # print(key, value, len(value))
            TF = len(value)
            score[key] += TF*IDF

    # sort the document list
    sorted_score = dict(sorted(score.items(), key=lambda x: x[1], reverse=True))
    return list(sorted_score.keys())

def BM25(query):
    query_pro = preprocess(query)

    client = pymongo.MongoClient("mongodb+srv://zhou:0219@cluster0.kwwqk4a.mongodb.net/?retryWrites=true&w=majority")
    db =client['ttds']
    score = defaultdict(float)
    total_cnt = 100000

    for term in query_pro:
        departments = db['invertIndex'].find({'token': term})
        result = []

        for department in departments:
            result.append({
                'tokenaa':  department['token'],
                'documentcount': department['docCount'],
                'docposition': department['docPos'],
            })

        # calculate bm25
        # bm25 = W * R
        W = math.log((total_cnt - result[0]['documentcount'] + 0.5) / (result[0]['documentcount'] + 0.5))
        R = 0.0

        # k1，k2，b为调节因子，超参
        k1 = 1.2
        k2 = 100
        b = 0.75
        # average document length， 文本单词平均数量
        # todo
        avdl = 100000

        # term在Query中的出现频率
        qf = query_pro.count(term)
        
        for key, value in result[0]['docposition'].items():
            # -------todo---------
            # document length， 文本单词数量
            dl = 100000
            # --------------------
            K = k1 * ((1-b) + b * (float(dl)/float(avdl)))
            # term在doc中的出现频率
            f = len(value)
            r1 = ((k1 + 1) * f) / (K + f)
            r2 = ((k2 + 1) * qf) / (k2 + qf)
            R =  r1 * r2
            score[key] += W*R
            

    sorted_score = dict(sorted(score.items(), key=lambda x: x[1], reverse=True))
    return list(sorted_score.keys())

# query = "a ok lord"
# print(TFIDF(query))
# print(BM25(query))