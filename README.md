# Essay Notes

The database of the essays is essays.db, which includes the title, the author, the abstract, and the urls of the papers. The following is a brief list of the important papers.

## Model Compression

[AMC: AutoML for Model Compression and Acceleration on Mobile Devices](https://arxiv.org/pdf/1802.03494.pdf)

- By using reinforcement learning to provide the model compression policy, AutoML for Model Compression (AMC) outperforms conventional rule-based compression policy by having higher compression ratio, better preserving the accuracy and freeing human labor.

[Deep Compression: Compressing Deep Neural Network with Pruning, Trained Quantization and Huffman Coding](https://arxiv.org/pdf/1510.00149.pdf)

- By introducing a three stage pipeline of pruning, trained quantization and Huffman coding, "deep compression" is able to reduce the storage requirement of neural networks without affecting the accuracy. 

[EIE: Efficient Inference Engine on Compressed Deep Neural Network](https://arxiv.org/pdf/1602.01528.pdf)

- By performing inference on the "deep compression" network model and using weight sharing for sparse matrix-vector multiplication, energy efficient inference engine (EIE) obtains better throughput, energy efficiency, and area efficiency.

[ESE: Efficient Speech Recognition Engine with Sparse LSTM on FPGA](https://arxiv.org/pdf/1612.00694.pdf)

- By using a load-balance-aware pruning method of pruning and quantization, a scheduler for parallelism and LSTM data flow, and a hardware architecture called ESE, this paper's design can compress the LSTM model size, maintain prediction accuracy, and achieve high hardware utilization.

[HAQ: Hardware-Aware Automated Quantization With Mixed Precision](https://arxiv.org/pdf/1811.08886.pdf)

- By using reinforcement learning with the feedback from the hardware accelerator, Hardware-Aware Automated Quantization (HAQ) is fully automated and can specialize the quantization policy for different neural network architectures and hardware architectures.

## GAN

[Anycost GANs for Interactive Image Synthesis and Editing](https://arxiv.org/pdf/2103.03243.pdf)

- By running subsets of the full generator with sampling-based multi-resolution training, adaptive-channel training, a generator-conditioned discriminator, new encoder training, and latent code optimization techniques, Anycost GAN can be evaluated at various configurations while achieving better image quality for interactive natural image editing.

[Differentiable Augmentation for Data-Efficient GAN Training](https://arxiv.org/pdf/2006.10738.pdf
https://github.com/mit-han-lab/data-efficient-gans)

- By imposing various types of differentiable augmentations on both real and fake samples, Differentiable Augmentation (DiffAugment) effectively stabilizes training, and leads to better convergence, thus improves the data efficiency of GANs

[GAN Compression: Efficient Architectures for Interactive Conditional GANs](https://arxiv.org/pdf/2003.08936.pdf)

- By transferring knowledge of multiple intermediate representations of the original model to its compressed model, unifying unpaired and paired learning, and finding efficient architectures via NAS with weight sharing, this paper's design reduces the inference time and model size of the generator in cGANs.

## NAS

[APQ: Joint Search for Network Architecture, Pruning and Quantization Policy](https://arxiv.org/pdf/2006.08509.pdf)

- By optimizing the neural architecture, pruning policy, and quantization policy jointly through training a quantization-aware accuracy predictor with full-precision knowledge, APQ is presented for efficient deep learning inference on resource-constrained hardware.

[HAT: Hardware-Aware Transformers for Efficient Natural Language Processing](https://arxiv.org/pdf/2005.14187.pdf)

- By constructing a design space with arbitrary encoder-decoder attention and heterogeneous layers, training a SuperTransformer with weight sharing, and performing evolutionary search with hardware constraints, Hardware-Aware Transformers (HAT) enables low-latency inference on resource-constrained hardware platforms.

[MCUNet: Tiny Deep Learning on IoT Devices](https://arxiv.org/pdf/2007.10319.pdf)

- By jointly designs an efficient neural architecture (TinyNAS) with optimization of the search space and the specialization of the network architecture, and a lightweight inference engine (TinyEngine) with memory scheduling according to the overall network topology, MCUNet reduces the memory usage and accelerates the inference.

[NAAS: Neural Accelerator Architecture Search](https://arxiv.org/pdf/2105.13258.pdf)

- By holistically searching the neural network architecture, accelerator architecture and compiler mapping in one optimization loop, Neural Accelerator Architecture Search (NAAS) composes highly matched architectures together with efficient mapping.

[Neural-Hardware Architecture Search](http://mlforsystems.org/assets/papers/neurips2019/neural_hardware_lin_2019.pdf)

- By using machine learning based design and optimization methodology with evolution strategy based hardware architecture search and one-shot hyper-net based quantized neural architecture search, this paper's design composes highly matched neural-hardware architectures.

[ProxylessNAS: Direct Neural Architecture Search on Target Task and Hardware](https://arxiv.org/pdf/1812.00332.pdf)

- By directly learning the architectures for large-scale target tasks and target hardware platforms, ProxylessNAS is able to deal with high memory consumption, reduce the computational cost, and allow a large candidate set.

## Federated Learning

[Federated Evaluation and Tuning for On-Device Personalization: System Design & Applications](https://arxiv.org/pdf/2102.08503.pdf)

- By creating a federated task processing system, this paper's design supports federated evaluation and tuning of on-device ML systems with personalization at scale to highlight application specific solutions.

[Federated Hyperparameter Tuning: Challenges, Baselines, and Connections to Weight-Sharing]()

- By making connection to NAS technique of weight sharing, FedEx can accelerate federated hyperparameter tuning.

## System Robustness

[Efficient and Robust LiDAR-Based End-to-End Navigation](https://arxiv.org/pdf/2105.09932.pdf)

- By using sparse convolution kernel optimization, hardware-aware model design, and Hybrid Evidential Fusion that estimates the uncertainty of the prediction, Fast-LiDARNet improves robustness and reduces the number of takeovers in the real world.

## Scheduler

[IOS: Inter-operator Scheduler for CNN Acceleration](https://arxiv.org/pdf/2011.01302.pdf)

- By automatically schedule multiple operators’ parallel execution through a novel dynamic programming algorithm,Inter-Operator Scheduler (IOS) outperforms SOTA algorithms on accelerating CNN inference.

## Other accelerating technique

[Learning both Weights and Connections for Efficient Neural Network](https://arxiv.org/pdf/1506.02626.pdf)

- By pruning redundant connections through a three-step method of learning important connections, pruning unimportant connections, and training remaining connections, this paper's design can reduce the storage and computation required.

[Lite Transformer with Long-Short Range Attention](https://arxiv.org/pdf/2004.11886.pdf)

- By using Long-Short Range Attention (LSRA) with local context modeling (by convolution) and long-distance relationship modeling (by attention), together with pruning and quantization, Lite Transformer reduces the computation and compresses the model size to achieve high performance.

[Once-for-All: Train One Network and Specialize it for Efficient Deployment](https://arxiv.org/pdf/1908.09791.pdf)

- By decoupling training of a OFA network and search with selection from the OFA network, and a progressive shrinking algorithm, this paper's design supports diverse architectural settings, reduces the model size, and obtains a large number of subnetworks to fit different hardware platforms and latency constraints with low accuracy loss.

[SpArch: Efficient Architecture for Sparse Matrix Multiplication](https://arxiv.org/pdf/2002.08947.pdf)

- By using a highly parallelized streaming-based merger, a condensed matrix representation, a Huffman tree scheduler, and a row prefetcher with near-optimal buffer replacement policy, the sparse matrix multiplication accelerator architecture, SpArch, has high scalability and energy saving,  and reduces the DRAM access.

[SpAtten: Efficient Sparse Attention Architecture with Cascade Token and Head Pruning](https://arxiv.org/pdf/2012.09852.pdf)

- By leveraging token sparsity to prune away unimportant tokens, head sparsity to remove unessential heads, and quantization opportunities to separate MSB and LSB computation, SpAtten, reduces the attention computation and memory access with no accuracy loss. 

[TinyTL: Reduce Memory, Not Parameters for Efficient On-Device Learning](https://arxiv.org/pdf/2007.11622.pdf)

- By freezing the weights while only learns the bias modules and introducing a new memory-efficient bias module, the lite residual module, to refine the feature extractor, Tiny-Transfer-Learning (TinyTL) saves the memory with little accuracy loss and provides accuracy improvements with little memory overhead.

## Computer Vision

[Point-Based Multi-View Stereo Network](https://arxiv.org/pdf/1908.04422v1.pdf)

- By directly processing the target scene as point clouds through generating a coarse depth map, converting it into a point cloud, and refining the point cloud iteratively, then fusing 3D geometry priors and 2D texture information, Point-MVSNet achieves higher accuracy, more computational efficiency, and more flexibility.

[Point-Voxel CNN for Efficient 3D Deep Learning](https://arxiv.org/pdf/1907.03739.pdf)

- By representing the 3D input data in points and performing the convolutions in voxels, Point-Voxel CNN (PVCNN) is able to reduce the memory consumption and the irregular, sparse data access, and improve the locality, thus obtain more efficient, fast 3D deep learning.

[Searching Efficient 3D Architectures with Sparse Point-Voxel Convolution](https://arxiv.org/pdf/2007.16100.pdf)

- By using Sparse Point-Voxel Convolution (SPVConv) which equips the vanilla Sparse Convolution with the high-resolution point-based branch, and 3D Neural Architecture Search (3D-NAS), SPVNAS is able to preserve the fine details, explore the spectrum of efficient 3D models, and is fast and accurate.

[TSM: Temporal Shift Module for Efficient Video Understanding](https://arxiv.org/pdf/1811.08383.pdf)

- By shifting part of the channels along the temporal dimension to facilitate information exchanged among neighboring frames, Temporal Shift Module (TSM) can achieve the performance of 3D CNN but maintain 2D CNN’s complexity that enables real-time low-latency online video recognition and video object detection.
