# language-similar-api
## URL
https://sentence-similarity-api.herokuapp.com/
## 実行準備
モデルの用意
## 開発環境
* python3.6.9
* UbuntuOS(GoogleColaboratory)  
※WindowsOSで実行時には環境構築時に以下の変更が必要
```text: requirements
mecab-python3==0.996.2
```
を
```text: requirements
mecab-python-windows=0.996.3
```
に変更  
## 送受信データ形式
* request(POSTのみ)
```
{
  'sentence1': '<文章1>',
  'sentence2': '<文章2>'
}
```
* response
```
{
  'similarity': <類似度>
}
```
