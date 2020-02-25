#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
import cv2
import numpy as np

def main():

    fname = "./natsuki.chr"

    if not os.path.exists(fname):
        print("Error: " + fname + " not found.", file=sys.stderr)
        exit(1)

    # natsuki.chrの実態はPNGである．
    src = cv2.imread(fname)
    # 90度反時計回りに回転させる．
    src = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # 画像を極座標に変換する．
    center = (src.shape[0]/2, src.shape[1]/2)
    k = np.sqrt((src.shape[0]/2.0)**2 + (src.shape[1]/2.0)**2)/2.0
    dst = cv2.linearPolar(src, center, k, cv2.WARP_INVERSE_MAP)

    # 再度回転させ，顔を見やすくする．
    dst = cv2.rotate(dst, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow('natsuki', dst)

    cv2.waitKey(0)


if __name__ == "__main__":
    main()

