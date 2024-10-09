# Setup Guide for NVIDIA GPU Support on Dataiku DSS with Ubuntu

## Prerequisites

- **VM**: GCP n1-highmem-16
- **GPU**: NVIDIA Tesla T4
- **Google Image**: ubuntu-2004-focal-v20210429
- **OS**: Ubuntu 20.04

## Steps

### 1. Update the system

Update the package lists and upgrade the system:

```sh
sudo apt-get update
sudo apt-get upgrade -y
```
### 2. Install required packages
Install essential packages for building and running the NVIDIA drivers and CUDA:

```sh
sudo apt-get install -y build-essential dkms
```
### 3. Disable Nouveau driver
Create a file to disable the nouveau driver:
```sh
sudo bash -c 'echo "blacklist nouveau" > /etc/modprobe.d/blacklist-nouveau.conf'
sudo bash -c 'echo "options nouveau modeset=0" >> /etc/modprobe.d/blacklist-nouveau.conf'
```
Regenerate the initial RAM filesystem:
```sh
sudo update-initramfs -u
sudo reboot

### 4. Add the NVIDIA package repositories
Add the NVIDIA package repositories:
```sh
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
sudo bash -c 'echo "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /" > /etc/apt/sources.list.d/cuda.list'
sudo bash -c 'echo "deb https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu2004/x86_64/ /" > /etc/apt/sources.list.d/cuda_learn.list'
sudo apt-get update
```
### 5. Install NVIDIA driver
Install the NVIDIA driver:
```sh
sudo apt-get install -y nvidia-driver-460
sudo reboot
```
### 6. Install CUDA Toolkit
Install the CUDA toolkit:
```sh
sudo apt-get install -y cuda
Update the environment variables:

echo 'export PATH=/usr/local/cuda/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc```
### 7. Install cuDNN
Download the cuDNN library tar file from the NVIDIA Developer website.

Extract and install the cuDNN files:
```sh
tar -xzvf cudnn-11.1-linux-x64-v8.0.5.39.tgz
sudo cp cuda/include/cudnn*.h /usr/local/cuda/include
sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda/lib64
sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*
```
### 8. Validate the GPU Setup
Verify the installation:
```sh
nvcc --version
nvidia-smi
```
### 9. Set up Dataiku and Python environment
Prepare a Python virtual environment, then install required deep learning packages:
```sh
python3 -m venv dataiku-dl-env
source dataiku-dl-env/bin/activate
pip install tensorflow-gpu==2.4.1 keras==2.4.3 scikit-learn==0.24.1 scipy==1.6.0 statsmodels==0.12.1 jinja2==2.11.3 flask==1.1.2 h5py==2.10.0 pillow==8.1.0 cloudpickle==1.6.0 matplotlib==3.3.4
```
### 10. Configure Dataiku to use the Python environment
Within Dataiku DSS:

Go to Administration > Settings > Python.
Add a new Python environment pointing to the path of your virtual environment.
Test the environment by running a sample TensorFlow/Keras script to ensure GPU support is working.
