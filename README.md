## Google Home Speaker
Google HOME/NEST に好きな言葉を発話してもらうフォームです。

以下の記事を参考にしました。

[Google Homeを喋らせたい人のメモ](https://qiita.com/kiwsdiv/items/72d8a80c734e6d3e235b)


### インストール方法
コードをクローンして以下のコマンドを実行します。
```bash
cd google-home-speaker
pip install -r requirements.txt
```

その後、`google-speaker.py` の `SERVER_HOST` のIPアドレスをプログラムを動かすサーバーのIPアドレスに変更します。

### 使い方
以下のコマンドを実行して、サーバーを起動します。
```bash
python google-speaker.py
```
サーバーが起動し、以下のURLでページが表示されればOK。

http://{サーバーのIPアドレス}:8080/form

### 注意点
- python3.7以降の環境が必要です。
- 発話前に動作がとまる不具合が残っています。ページをリロードすると発話します。
- よって、まだ実用的ではありません。