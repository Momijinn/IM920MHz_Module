#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import IM920

#ペアリング
#IM920.Srid(19200,'52C0')

#削除
#IM920.Erid(19200)

#文字列送信
#IM920.Send(19200, 'hoehoge')

#文字列受信
#print(IM920.Reception(19200))

#中継機化
#IM920.Repeater(19200)

#固有ID
IM920.Rdid(19200)

#ボーレート設定
#IM920.Sbrt(19200, '4')
