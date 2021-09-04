# GAN

[Anycost GANs for Interactive Image Synthesis and Editing](https://arxiv.org/pdf/2103.03243.pdf)

- By running subsets of the full generator with sampling-based multi-resolution training, adaptive-channel training, a generator-conditioned discriminator, new encoder training, and latent code optimization techniques, Anycost GAN can be evaluated at various configurations while achieving better image quality for interactive natural image editing.

[Differentiable Augmentation for Data-Efficient GAN Training](https://arxiv.org/pdf/2006.10738.pdf
https://github.com/mit-han-lab/data-efficient-gans)

- By imposing various types of differentiable augmentations on both real and fake samples, Differentiable Augmentation (DiffAugment) effectively stabilizes training, and leads to better convergence, thus improves the data efficiency of GANs

[GAN Compression: Efficient Architectures for Interactive Conditional GANs](https://arxiv.org/pdf/2003.08936.pdf)

- By transferring knowledge of multiple intermediate representations of the original model to its compressed model, unifying unpaired and paired learning, and finding efficient architectures via NAS with weight sharing, this paper's design reduces the inference time and model size of the generator in cGANs.