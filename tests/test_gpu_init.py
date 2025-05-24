import torch


def test_gpu_available():
    assert torch.cuda.is_available(), "No GPU is available for PyTorch"
