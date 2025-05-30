# gpucontainertest

[![gpucontainer](https://github.com/stvhay/gpucontainertest/actions/workflows/gpucontainer.yml/badge.svg)](https://github.com/stvhay/gpucontainertest/actions/workflows/gpucontainer.yml)

This is just a simple bare project structure for VS Code that includes a CUDA-
enabled Docker image meeting VS Code Dev Container requirements.

## Setting up Docker for GPU Support

Before using this container, ensure Docker is configured to work with your NVIDIA GPU. This typically involves installing the NVIDIA Container Toolkit. Here's a brief overview:

1.  **Install NVIDIA Drivers:** Make sure you have the correct NVIDIA drivers installed for your GPU.
2.  **Install the NVIDIA Container Toolkit:** Follow the installation instructions for your Linux distribution from the official NVIDIA [documentation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html).
3.  Run a quick test:
    ```bash
    docker run --rm --gpus all nvidia/cuda:12.9.0-base-ubuntu24.04 nvidia-smi
    ```

## Build Locally or Use the Repository

Checking out this repo will set up VS Code to build the container locally using
the Dockerfile. If you want to use the prebuilt container, you can make this
change to the docker-compose.yml file:

### Github Registry
```diff
@@ -3,7 +3,8 @@
-    build:
-      context: ..
-      dockerfile: .devcontainer/Dockerfile
+    image: ghcr.io/stvhay/gpucontainer:latest
```

### Docker Registry
```diff
@@ -3,7 +3,8 @@
-    build:
-      context: ..
-      dockerfile: .devcontainer/Dockerfile
+    image: stvhy/gpucontainer:latest
```

## Shell into the Container

If you want to just mess around in the shell a bit:

```bash
docker run --rm --gpus all nvidia/cuda:12.9.0-base-ubuntu24.04 /bin/bash
```
