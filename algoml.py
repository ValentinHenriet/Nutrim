import torch, matplotlib
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor


batch = 64
epochs = 3

def downloadDataset():
    food_training_data=datasets.Food101(
        root="data",
        split = "train",
        download=True,
        transform=ToTensor()
    )

    food_test_data = datasets.Food101(
        root="data",
        split = "test",
        download=True,
        transform=ToTensor()
    )

    return food_training_data, food_test_data

food_trainset,food_testset = downloadDataset() 
print("Training set size: ", len(food_trainset))
print("Testing set size : ", len(food_testset))

# we define a loader and an iterator to process the training set
trainloader = torch.utils.data.DataLoader(food_trainset, batch_size=64, shuffle=True)
testloader = torch.utils.data.DataLoader(food_testset, batch_size=64, shuffle=False)
