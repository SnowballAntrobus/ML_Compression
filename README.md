# Autoencoder for Video Compression

The literature indicates that this is an active and fruitful area of research. However, the technology is not yet mature enough that this would be easy to implement with effective results. In particular the issue is that no one is thinking about 4k image compression (or even 1080p). I will try some experiements with the basic and [open source model](https://github.com/tensorflow/models/tree/2390974a/compression) in this area. I found this all very interesting!

### The Problem with Basic Auto Encoding

1. Models are trained with a fixed size input image
2. Very low quality for large frames (ie non MINST 28x28 images)
3. No pretrained models found
4. Most ignore 4k or even 1080p

### Literature

- [Full Resolution Image Compression with Recurrent Neural Networks](https://arxiv.org/pdf/1608.05148v2.pdf) 

  In this paper from 2017, the authors use Recurrent Neural Networks to provide an architecture that works with images of variable sizes for mixed results. This only partially solves problems **1** and **2** because their dataset was Kodak Photo CD dataset (768×512).  Most importantly, the group open sourced their [best prefroming model](https://github.com/tensorflow/models/tree/master/comp res- sion.) which would be ideal to **3**. However, the link is dead. This [link](https://github.com/tensorflow/models/tree/2390974a/compression) is alive.

- [LOSSY IMAGE COMPRESSION WITH COMPRESSIVE AUTOENCODERS](https://arxiv.org/pdf/1703.00395v1.pdf)

  In this paper from 2017, the authors use Autoencoders with tweaked loss functions in order to provide an architecture that works with variable sized images for competitive results when compared with JPEG2000 and RNN solutions. They use >1080p images which is encouraging for a true solution to problems **1** and **2** and **4**. Critically, there is no released model so **3** is not met.

- [LEARNED VARIABLE-RATE IMAGE COMPRESSION WITH RESIDUAL DIVISIVE NORMALIZATION](https://arxiv.org/pdf/1912.05688v1.pdf) 

  From 2019, a more complex architecture is introduced with better results than previous models. However, these improvements seem marginal and no model is provided. Morevover, this was also tested on the Kodak Photo CD dataset (768×512) so it does not meet **4**. 

- [Deep Generative Video Compression](https://studios.disneyresearch.com/wp-content/uploads/2020/03/Deep-Generative-Video-Compression.pdf)

  A 2019/2020 paper, the authors decide to devise a whole new paradigm for using deep learning for video compression. This claims to be quite different from the other papers and promisses much better (albeit speciallized) results. However, this approach is very much in its infancy not really solving any of the problems listed at this time. It is very interesting though (or maybe its hype). 
