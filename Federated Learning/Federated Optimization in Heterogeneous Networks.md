# Federated Optimization in Heterogeneous Networks

## Url

https://arxiv.org/pdf/1812.06127v4.pdf

## Brief Description

By generalization and re-parametrization of FedAvg, FedProx guarantees convergence for statistical heterogeneity and adhering to device-level systems constraints for systems heterogeneity, thus demonstrates significantly more stable and accurate convergence.

## Motivation

The previous SOTA algorithms for federated learning is FedAvg, but FedAvg suffers from several issues, especially the setting of the hyper-parameters, like local epochs. The best idea is to adjust the value of local epochs throughout the training of each device.

## Approach

### $\gamma$-inexact-solution

![definition](https://img2020.cnblogs.com/blog/1641771/202006/1641771-20200627221904724-555139622.png)

$\gamma$​-inexact-solution is used to evaluate the computation cost in each epoch of each local solver. $\gamma$​​ can be different for different solver and different epochs.

### $\gamma_{k}^{t}$-inexact-solution

![img](https://img2020.cnblogs.com/blog/1641771/202006/1641771-20200628003040002-1933341147.png)

### Tolerating partial work

FedProx uses different local epoch for different $\gamma$​ and different device.

### Proximal term

- Adding a proximal term to local subproblem to limit the varied local update