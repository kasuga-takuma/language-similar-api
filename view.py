# coding: utf-8

from flask import Flask, request
import MeCab
import gensim
import numpy as np

app = Flask(__name__)
# mt = MeCab.Tagger()
# mt.parse('')
# model = gensim.models.Word2Vec.load('./ja/ja.bin')


@app.route('/', methods=['POST'])
def api():
    json = request.get_json()  # Get POST JSON
    vector1 = json['sentence1']
    vector2 = json['sentence2']
    v1 = get_vector(vector1)
    v2 = get_vector(vector2)
    return {'similarity': cos_sim(v1, v2)}


@app.route('/put', methods=['put'])
def put_test():
    json = request.get_json()
    print('==request==')
    print(json)
    print('===========')


def get_vector(text):
    sum_vec = np.zeros(300)
    word_count = 0
    node = mt.parseToNode(text)
    while node:
        fields = node.feature.split(",")
        # 名詞、動詞、形容詞に限定
        if fields[0] == '名詞' or fields[0] == '動詞' or fields[0] == '形容詞' or fields[0] == '副詞':
          try:
            sum_vec += model.wv[node.surface]
            word_count += 1
          except KeyError:
            word_count += 1
        node = node.next
    return sum_vec / word_count


# cos類似度を計算
def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


# メイン関数
if __name__ == '__main__':
    app.run(debug=True)
