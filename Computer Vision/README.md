# Computer Vision

[Point-Based Multi-View Stereo Network](https://arxiv.org/pdf/1908.04422v1.pdf)

- [Code](https://github.com/callmeray/PointMVSNet)

- By directly processing the target scene as point clouds through generating a coarse depth map, converting it into a point cloud, and refining the point cloud iteratively, then fusing 3D geometry priors and 2D texture information, Point-MVSNet achieves higher accuracy, more computational efficiency, and more flexibility.

[Point-Voxel CNN for Efficient 3D Deep Learning](https://arxiv.org/pdf/1907.03739.pdf)

- By representing the 3D input data in points and performing the convolutions in voxels, Point-Voxel CNN (PVCNN) is able to reduce the memory consumption and the irregular, sparse data access, and improve the locality, thus obtain more efficient, fast 3D deep learning.

[Searching Efficient 3D Architectures with Sparse Point-Voxel Convolution](https://arxiv.org/pdf/2007.16100.pdf)

- By using Sparse Point-Voxel Convolution (SPVConv) which equips the vanilla Sparse Convolution with the high-resolution point-based branch, and 3D Neural Architecture Search (3D-NAS), SPVNAS is able to preserve the fine details, explore the spectrum of efficient 3D models, and is fast and accurate.

[TSM: Temporal Shift Module for Efficient Video Understanding](https://arxiv.org/pdf/1811.08383.pdf)

- [Code](https://github.com/mit-han-lab/temporal-shift-module)

- By shifting part of the channels along the temporal dimension to facilitate information exchanged among neighboring frames, Temporal Shift Module (TSM) can achieve the performance of 3D CNN but maintain 2D CNN’s complexity that enables real-time low-latency online video recognition and video object detection.