import tfci
from PIL import Image 
from IPython.display import display
import gen_sizes
import pandas as pd
import time
import os

models = ['hific-lo', 'hific-mi', 'hific-hi', 'mbt2018-mean-mse-1', 'mbt2018-mean-mse-2', 'mbt2018-mean-mse-3', 'mbt2018-mean-mse-4', 'mbt2018-mean-mse-5', 'mbt2018-mean-mse-6', 'mbt2018-mean-mse-7', 'mbt2018-mean-mse-8', 'mbt2018-mean-msssim-1', 'mbt2018-mean-msssim-2', 'mbt2018-mean-msssim-3', 'mbt2018-mean-msssim-4', 'mbt2018-mean-msssim-5', 'mbt2018-mean-msssim-6', 'mbt2018-mean-msssim-7', 'mbt2018-mean-msssim-8', 'bmshj2018-factorized-mse-1', 'bmshj2018-factorized-mse-2', 'bmshj2018-factorized-mse-3', 'bmshj2018-factorized-mse-4', 'bmshj2018-factorized-mse-5', 'bmshj2018-factorized-mse-6', 'bmshj2018-factorized-mse-7', 'bmshj2018-factorized-mse-8', 'bmshj2018-factorized-msssim-1', 'bmshj2018-factorized-msssim-2', 'bmshj2018-factorized-msssim-3', 'bmshj2018-factorized-msssim-4', 'bmshj2018-factorized-msssim-5', 'bmshj2018-factorized-msssim-6', 'bmshj2018-factorized-msssim-7', 'bmshj2018-factorized-msssim-8', 'bmshj2018-hyperprior-mse-1', 'bmshj2018-hyperprior-mse-2', 'bmshj2018-hyperprior-mse-3', 'bmshj2018-hyperprior-mse-4', 'bmshj2018-hyperprior-mse-5', 'bmshj2018-hyperprior-mse-6', 'bmshj2018-hyperprior-mse-7', 'bmshj2018-hyperprior-mse-8', 'bmshj2018-hyperprior-msssim-1', 'bmshj2018-hyperprior-msssim-2', 'bmshj2018-hyperprior-msssim-3', 'bmshj2018-hyperprior-msssim-4', 'bmshj2018-hyperprior-msssim-5', 'bmshj2018-hyperprior-msssim-6', 'bmshj2018-hyperprior-msssim-7', 'bmshj2018-hyperprior-msssim-8', 'b2018-leaky_relu-128-1', 'b2018-leaky_relu-128-2', 'b2018-leaky_relu-128-3', 'b2018-leaky_relu-128-4', 'b2018-leaky_relu-192-1', 'b2018-leaky_relu-192-2', 'b2018-leaky_relu-192-3', 'b2018-leaky_relu-192-4', 'b2018-gdn-128-1', 'b2018-gdn-128-2', 'b2018-gdn-128-3', 'b2018-gdn-128-4', 'b2018-gdn-192-1', 'b2018-gdn-192-2', 'b2018-gdn-192-3', 'b2018-gdn-192-4']

imo = Image.open('images/ori.png')
width, height = imo.size

sizes = gen_sizes.generate_videos(width, height, [(16,9)], 1000000000000, 30000, 2)

columns = ['Size', 'Model', 'Compress Success', 'Time to Compress', 'File Size Change', 'Decompress Success', 'Time to Decompress']
df = pd.DataFrame(columns=columns)

for i in reversed(sizes['16:9']):
    s = i[1]
    if i[1] != 2160:
        left = width - i[0]
        top = height - i[1]
        right = width
        bottom = height
        im = imo.crop((left, top, right, bottom))
        impath = 'images/' + str(i[1]) + '.png'
        im.save(impath)
    else:
        impath = 'images/' + str(i[1]) + '.png'
        imo.save(impath)

    for model in models:
        m = model
        c = 'N'
        d = 'N'
        file_size = 0
        cpath = "compressed/" + model + '_' + str(i[1]) + '.tfci'
        dpath = "decompressed/" + model + '_' + str(i[1]) + '.png'
        tfci.compress(model, impath, cpath)
        try:
            t0 = time.time()
            tfci.compress(model, impath, cpath)
            t1 = time.time()
            c = 'Y'
            file_size = os.path.getsize(impath) - os.path.getsize(cpath)
        except:
            print(':(')
        try:
            t2 = time.time()
            tfci.decompress(cpath, dpath)
            t3 = time.time()
            d = 'Y'
        except:
            print(':(')
        df1 = pd.DataFrame([[s, m, c, t1-t0, file_size, d, t3-t2]], columns=columns)
        df = df.append(df1)
        df.to_csv('results.csv')