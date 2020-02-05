#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image
import os, sys
import struct
from base64 import b64decode

# リストのビット列をデータに変更する．
# 例えば，ASCIIのAは0x41 = 0b0100_0001である．
# bits2text([1,0,0,0,0,0,1])
# -> b'A'
def bits2text(bits):
    # 出力データ(1要素にunsigned int型の数値が入る)．
    text = b""
    # 1byteの文字列
    byte = ""
    for i, bit in enumerate(bits):

        # 1byte = 8bit毎に出力データとしてまとめる．
        if i != 0 and i % 8 == 0:
            byte = "0b" + byte
            # 2進数の文字列を数値(unsigned int)にする(e.g. "0b111" -> 7)．
            text += struct.pack("B", int(byte, 2))
            byte = ""

        byte += str(bit)

    # 余り
    byte = "0b" + byte
    text += struct.pack("B", int(byte, 2))

    return text


def main():

    fname = "./monika.chr"

    if not os.path.exists(fname):
        print("Error: " + fname + " not found.", file=sys.stderr)
        exit(1)

    # monika.chrの実態はPNGである．
    img = Image.open(fname)
    # 2値化(閾値: 127)
    img = img.convert("L")
    img = img.point(lambda x: 0 if x <= 127 else x)

    # Windowsに標準で付いてくるPaintを使って座標を調べてある．
    # 日本語版と英語版で違うので適宜切り替える．

    # 日本語の場合
    xstart, ystart = 316, 316
    xend, yend = 482, 482

    # 英語の場合
    xstart, ystart = 330, 330
    xend, yend = 469, 469

    # ピクセルの色を基に0，1のどちらかが入るビット列
    bits = []
    for y in range(ystart, yend+1):
        for x in range(xstart, xend+1):

            # (R, G, B, A)
            color = img.getpixel((x, y))

            if color == 0:
                bits.append(0)
                continue

            if color == 255:
                bits.append(1)
                continue

            print("Error: Cannot read color.", file=sys.stderr)
            print(color, file=sys.stderr)
            exit(1)

    # ビット列を文字列に変換する．
    text = bits2text(bits)
    # base64でデコードする．
    print(b64decode(text).decode())


if __name__ == "__main__":
    main()

