IM920MHz_Module
====
interplan社の920MHz帯モジュール([IM920MHz](http://www.interplan.co.jp/solution/wireless/im920.php))のライブラリ

## Description
interplan社の920MHz帯モジュール([IM920MHz](http://www.interplan.co.jp/solution/wireless/im920.php))をPythonで簡単に使いやすくしたモジュールプログラム

## Requirement
* 動作確認したpython

    python2.7 & 3.5

* install module
    ```bash
    $ pip install pyserial
    ```

## Demo
```bash
$ python sample.py
52C3
```

## Usage
* windowsのみcomポートを確認しなくてもIM920へ接続します

    これに伴い，パソコンにIM920が2台以上接続しているcomポートが小さい数字の方へ接続されます


* 使用できるコマンド
  * Im920.Srid() ：ペアリング

  * Im920.Erid()：ペアリングデバイスの削除

  * Im920.Send()：文字列送信

  * Im920.Reception()：文字列の受信

  * Im920.Repeater()：中継機化

  * Im920.Rdid()：固有IDの表示

  * Im920.Sbrt()：ボーレートの設定

## Install
* IM920.pyをインポート
    ```python
    import IM920
    ```

## Licence
This software is released under the MIT License, see LICENSE.

## Author
[Twitter](https://twitter.com/momijinn_aka)

[Blog](http://www.autumn-color.com/)