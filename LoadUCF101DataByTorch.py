import torchvision.datasets as datasets
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
import torchvision.transforms._transforms_video as v_transform
import torch


TRAIN_BATCH_SIZE = 128
TEST_BATCH_SIZE = 128
FRAME_LENGTH = 16



transform = transforms.Compose([
    v_transform.ToTensorVideo(),
    v_transform.NormalizeVideo(mean=[0.43216, 0.394666, 0.37645], std=[0.22803, 0.22145, 0.216989]),
    v_transform.RandomHorizontalFlipVideo(),
    v_transform.RandomCropVideo(112),
])



def custom_collate(batch):
    filtered_batch = []
    for video, _, label in batch:
        filtered_batch.append((video, label))
    return torch.utils.data.dataloader.default_collate(filtered_batch)



trainset = datasets.UCF101(
    root='data/UCF101/UCF-101',
    annotation_path='data/UCF101TrainTestSplits-RecognitionTask/ucfTrainTestlist',
    frames_per_clip=FRAME_LENGTH,
    num_workers=0,
    transform=transform,
)

trainset_loader = DataLoader(
    trainset,
    batch_size=TRAIN_BATCH_SIZE,
    shuffle=True,
    num_workers=0,
    collate_fn=custom_collate
)



testset = datasets.UCF101(
    root='data/UCF101/UCF-101',
    annotation_path='data/UCF101TrainTestSplits-RecognitionTask/ucfTrainTestlist',
    frames_per_clip=FRAME_LENGTH,
    num_workers=4,
    train=False,
    transform=transform,
)

testset_loader = DataLoader(
    testset,
    batch_size=TEST_BATCH_SIZE,
    shuffle=False,
    num_workers=4,
    collate_fn=custom_collate
)