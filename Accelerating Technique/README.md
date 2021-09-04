# Accelerating Technique

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