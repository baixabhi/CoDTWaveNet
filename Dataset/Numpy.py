# Load data from folders
dataset_path = '/kaggle/input/lc2500-colon-numpy-lebel1/colon_image_sets/'  # Update this path
classes = np.array([i.split('/')[-1] for i in glob.glob(dataset_path+'*')])

data_path = []
labels = []

for i in glob.glob(dataset_path+'*/*.npy'):
    data_path.append(i)
    labels.append(np.argmax(classes == i.split('/')[-2]))

# Split the data
train_data, val_data, train_labels, val_labels = train_test_split(data_path, labels, test_size=0.1, stratify=labels, random_state=42)
#val_data, test_data, val_labels, test_labels = train_test_split(temp_data, temp_labels, test_size=2/3, stratify=temp_labels, random_state=42)

class NumpyDataset(Dataset):
    def __init__(self, data, labels, transform=None):
        super(NumpyDataset, self).__init__()
        self.data = data
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        # Assuming data is already in memory as numpy arrays
        image = np.load(self.data[idx])
        label = self.labels[idx]

        if self.transform:
            image = self.transform(image)

        # Convert to tensor
        image = torch.tensor(image, dtype=torch.float32)
        label = torch.tensor(label, dtype=torch.long)

        return image, label
