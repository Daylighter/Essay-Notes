# Optimization

## Dynamic model

[Relay: A New IR for Machine Learning Frameworks](http://dl.acm.org/ft_gateway.cfm?id=3211348&ftid=1979148&dwn=1)

- By designing a purely-functional, statically-typed language, Relay, a new high-level intermediate representation (IR), is efficient, expressive, and portable across an array of heterogeneous hardware devices with the use of the open source NNVM compiler framework, which powers Amazon’s deep learning framework MxNet.

[Cortex: A Compiler for Recursive Deep Learning Models](https://arxiv.org/pdf/2011.01383.pdf)

- By performing high-level graph optimizations such as kernel fusion and low level kernel optimizations such as those found in vendor libraries, Cortex, a compiler-based approach, can generate highly-efficient code for recursive models for low latency inference on end-to-end optimizations.

[Nimble: Efficiently Compiling Dynamic Neural Networks for Model Inference](https://arxiv.org/pdf/2006.03031.pdf)

- By introducing a dynamic type system, a set of dynamism-oriented optimizations, and a light-weight virtual machine runtime, Nimble, a high-performance and flexible system, can optimize, compile, and execute dynamic neural networks on multiple platforms.

## Memory optimization

[AutoTM: Automatic Tensor Movement in Heterogeneous Memory Systems using Integer Linear Programming](https://dl.acm.org/doi/pdf/10.1145/3373376.3378465)

- By taking advantage of DC PMM (persistent memory modules) that promises higher read bandwidth at a lower cost per bit and the static nature of the underlying computational graphs, AutoTM, a profile guided optimization based on Integer Linear Programming (ILP), can minimize the amount of DRAM required and optimally assign and move live tensors to either DRAM or NVDIMMs.

[Capuchin: Tensor-based GPU Memory Management for Deep Learning](https://dl.acm.org/doi/pdf/10.1145/3373376.3378505)

- By tensor eviction/prefetching, recomputation, making memory management decisions based on dynamic tensor access pattern tracked at runtime, Capuchin, a tensor-based GPU memory management module, can reduce the memory footprint.

## Computing graph optimization

[TASO: optimizing deep learning computation with automatic generation of graph substitutions](https://dl.acm.org/doi/pdf/10.1145/3341301.3359630)

- By taking as input a list of operator specifications, generatinjg candidate substitutions using the given operators as basic building blocks, formally verifying against the operator specifications using an automated theorem prover, and performing a cost-based backtracking search, TASO, the first DNN computation graph optimizer, can automatically generates graph substitutions.

[Optimizing DNN computation graph using graph substitutions](http://www.vldb.org/pvldb/vol13/p2734-fang.pdf)

- By the pruning-based algorithm that eliminates the examination of redundant graph substitution sequences, a dynamic programming with pruning algorithm to make use of the explored graph substitutions, and a sampling heuristic, this paper defines the Optimizing Computation Graph using Graph Substitutions (OCGGS) problem, and proves it to be NP-hard and Poly-APX-complete.

## Kernel optimization

[Learning to Optimize Tensor Programs](https://proceedings.neurips.cc/paper/2018/file/8b5700012be65c9da25f49408d959ca0-Paper.pdf)

- By learning domain-specific statistical cost models to guide the search of tensor operator implementations and using effective model transfer across workloads, this paper's design of a learning-based framework can optimize tensor programs for deep learning workloads and supports a wide range of devices including low-power CPUs, mobile GPUs, and server-class GPUs.

[Ansor : Generating High-Performance Tensor Programs for Deep Learning](https://arxiv.org/pdf/2006.06762v2.pdf)

- By sampling programs from a hierarchical representation of the search space, fine-tuning the sampled programs with evolutionary search, using a learned cost model to identify the best programs, and using a scheduler, Ansor, a tensor program generation framework, can find high-performance programs, explore more optimization combinations, and optimize multiple subgraphs.

[AKG: Automatic Kernel Generation for Neural Processing Units using Polyhedral Transformations](https://dl.acm.org/doi/pdf/10.1145/3453483.3454106)

- By lowering the tensor expression language to a polyhedral representation, leveraging polyhedral schedulers, extending the semantics of the polyhedral representation, implementing the domain-specific optimization, and introducing complementary optimizations, AKG, a tensor compiler for NPUs, can obtain superior performance to both manual scheduling and vendor provided libraries.

[Automatic Kernel Generation for Volta Tensor Cores](https://arxiv.org/pdf/2006.12645.pdf)

- By using inline assembly instructions for programming tensor cores on NVIDIA Volta GPUs, this paper's design of a polyhedral approach can generate efficient CUDA kernels for matrix multiplication and pointwise operations.

## Scheduling optimization

[Rammer: Enabling Holistic Deep Learning Compiler Optimizations with rTasks](https://www.usenix.org/system/files/osdi20-ma.pdf)

- By generating an efficient static spatio-temporal schedule, exploiting parallelism through inter- and intra- operator co-scheduling, and proposing several abstractions for the computation tasks and the hardware accelerators, Rammer, a DNN compiler design, can minimize scheduling overhead, maximize hardware utilization, and optimize the execution of DNN workloads.

[A Learned Performance Model for Tensor Processing Units](https://arxiv.org/pdf/2008.01040.pdf)

- By using a corpus of tensor computation graph programs for Tensor Processing Unit (TPU) instances, this paper's design of a method of learning performance models, can outperform a heavily-optimized analytical performance model on tile-size selection and operator fusion, and it helps an autotuner discover faster programs in a setting where access to TPUs is limited or expensive.
