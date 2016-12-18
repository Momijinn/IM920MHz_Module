# IM920MHz_Module
interplan社の920MHz帯モジュール([IM920MHz](http://www.interplan.co.jp/solution/wireless/im920.php))のライブラリ  
Pythonで動作します

# 必要なモジュール
* serial  
  インストール：pip install pyserial  

# 動作確認した環境
* python 2.7  
* python 3.5  

# 使い方
IM920.pyをインポートしてください  
* Srid() ：ペアリング

* Erid()：ペアリングデバイスの削除

* Send()：文字列送信

* Reception()：文字列の受信

* Repeater()：中継機化

* Rdid()：固有IDの表示

* Sbrt()：ボーレートの設定

詳しい使い方は、sample.pyを参照してください

# その他
リファレンスを見ると、これ以外にも色々使用できるコマンドがありますが、使えそうなのをピックアップしました。