## PROJECT NAME: 
PYNQ Classification - Python on Zynq FPGA for Convolutional Neural Networks 

## BRIEF DESCRIPTION:
This repository presents a fast prototyping framework, which is an Open Source framework designed to enable fast deployment of embedded Convolutional Neural Network (CNN) applications on PYNQ platforms.

## CITATION:
If you make use of this code, please acknowledge us by citing [our article](https://spiral.imperial.ac.uk/handle/10044/1/57937):

	@inproceedings{Wang_FCCM18,
        author={E. Wang and J. J. Davis and P. Y. K. Cheung},
        booktitle={IEEE Symposium on Field-programmable Custom Computing Machines (FCCM)},
        title={{A PYNQ-based Framework for Rapid CNN Prototyping}},
        year={2018}
    }

## INSTRUCTIONS TO BUILD AND TEST THE PROJECT:

### Repository Organisation

The project demo accepts pre-trained CNN models in either Caffe or Theano syntax, hence the step 1 and 2 introduces how to install Caffe and Theano (with Lasagne) on PYNQ. Step 3 explains how to download and run the demos for LeNet and CIFAR-10 (Caffe "quick" version) models.

### Vivado Project Setup - How to implement more CNN models?

Please go to hw/README.md for guide on regenerating the Vivado and Vivado HLS projects.

### References
    
### 1. BNN-PYNQ

If you find BNN-PYNQ useful, please cite the <a href="https://arxiv.org/abs/1612.07119" target="_blank">FINN paper</a>:

    @inproceedings{finn,
    author = {Umuroglu, Yaman and Fraser, Nicholas J. and Gambardella, Giulio and Blott, Michaela and Leong, Philip and Jahre, Magnus and Vissers, Kees},
    title = {FINN: A Framework for Fast, Scalable Binarized Neural Network Inference},
    booktitle = {Proceedings of the 2017 ACM/SIGDA International Symposium on Field-Programmable Gate Arrays},
    series = {FPGA '17},
    year = {2017},
    pages = {65--74},
    publisher = {ACM}
    }

### 2. Caffe

Caffe is released under the [BSD 2-Clause license](https://github.com/BVLC/caffe/blob/master/LICENSE).
The BAIR/BVLC reference models are released for unrestricted use.

Please cite Caffe in your publications if it helps your research:

    @article{jia2014caffe,
      Author = {Jia, Yangqing and Shelhamer, Evan and Donahue, Jeff and Karayev, Sergey and Long, Jonathan and Girshick, Ross and Guadarrama, Sergio and Darrell, Trevor},
      Journal = {arXiv preprint arXiv:1408.5093},
      Title = {Caffe: Convolutional Architecture for Fast Feature Embedding},
      Year = {2014}
    }
    
### 3. Theano

    @ARTICLE{2016arXiv160502688short,
       author = {{Theano Development Team}},
        title = "{Theano: A {Python} framework for fast computation of mathematical expressions}",
      journal = {arXiv e-prints},
       volume = {abs/1605.02688},
     primaryClass = "cs.SC",
     keywords = {Computer Science - Symbolic Computation, Computer Science - Learning, Computer Science - Mathematical Software},
         year = 2016,
        month = may,
          url = {http://arxiv.org/abs/1605.02688},
    }

### 4. Lasagne 

    @misc{lasagne,
      author       = {Sander Dieleman and
                      Jan Schlüter and
                      Colin Raffel and
                      Eben Olson and
                      Søren Kaae Sønderby and
                      Daniel Nouri and
                      others},
      title        = {Lasagne: First release.},
      month        = aug,
      year         = 2015,
      doi          = {10.5281/zenodo.27878},
      url          = {http://dx.doi.org/10.5281/zenodo.27878}
    }
