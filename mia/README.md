
install cuda 12.9 no 13
sudo apt-get install -y cuda-runtime-12-9
 e driver nvwidea 355 compatibile 
sudo apt install -y nvidia-driver-535 nvidia-utils-535

insall cuda toolkit


tino@tino-linux-xps:~/dev/sorgente/mia$ lsmod | grep nvidia
nvidia_uvm           1773568  0
nvidia_drm             90112  2
nvidia_modeset       1314816  2 nvidia_drm
nvidia              56897536  82 nvidia_uvm,nvidia_modeset
video                  77824  5 dell_wmi,dell_laptop,xe,i915,nvidia_modeset



nvidia-smi
Failed to initialize NVML: Driver/library version mismatch
NVML library version: 580.65

tino@tino-linux-xps:~/dev/sorgente$ sudo nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2023 NVIDIA Corporation
Built on Fri_Jan__6_16:45:21_PST_2023
Cuda compilation tools, release 12.0, V12.0.140
Build cuda_12.0.r12.0/compiler.32267302_0


sudo docker run --rm --gpus all  --runtime nvidia ubuntu  nvidia-smi
sudo docker run --rm --gpus all  --runtime nvidia nvidia/cuda:13.0.0-devel-ubuntu22.04  nvidia-smi

sudo apt-get install -y cuda-runtime-12-1

sudo nvidia-smi
[sudo] password for tino: 
Thu Sep 11 11:24:50 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 575.57.08              Driver Version: 580.82.07      CUDA Version: 13.0     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4050 ...    On  |   00000000:01:00.0 Off |                  N/A |
| N/A   45C    P3             10W /   40W |      14MiB /   6141MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+


      sudo nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2023 NVIDIA Corporation
Built on Fri_Jan__6_16:45:21_PST_2023
Cuda compilation tools, release 12.0, V12.0.140
Build cuda_12.0.r12.0/compiler.32267302_0


  

nvcc --version



no@xps:~$ sudo -i -u postgres
postgres@xps:~$ psql
psql (16.10 (Ubuntu 16.10-0ubuntu0.24.04.1))
Type "help" for help.

postgres=# ALTER USER postgres PASSWORD 'grandepuffo';
ALTER ROLE
postgres=# CREATE USER sorgente WITH PASSWORD 'sorgente';
CREATE ROLE
postgres=# REATE DATABASE sorgente OWNER sorgente;
ERROR:  syntax error at or near "REATE"
LINE 1: REATE DATABASE sorgente OWNER sorgente;
        ^
postgres=# CREATE DATABASE sorgente OWNER sorgente;
CREATE DATABASE
postgres=# GRANT ALL PRIVILEGES ON DATABASE sorgente TO sorgente;



