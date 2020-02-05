# About

[Doki Doki Literature Club!](https://ddlc.moe/)のモニカのデータ解析スクリプトです．

ノベルゲームとしてはかなり斬新的でした．面白いので是非プレイしてみてください．

# Usage

- Python3で動作します．
- monika.chrと同一ファイルで実行してください． 
- 最初に`$ pip3 install pillow`でライブラリをインストールしてください．

```
$ ls -1
decode monika.py
monika.chr

$ python3 "decode monika.py" | nkf -w
```

# 仕組み
ネタバレ注意
```



































































































実はmonika.chrはPNG画像である．拡張子をchrからpngに変換して画像ビューアで開くと，中央に砂嵐の様な模様が描かれている．
砂嵐の白いピクセルを0，黒いピクセルを1とするとテキストデータになる．最後にこれをbase64でデコードするとメッセージが出現する．
```
