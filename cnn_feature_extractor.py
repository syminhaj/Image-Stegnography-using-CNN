import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt
import os

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, 3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
        self.fc1 = nn.Linear(32 * 64 * 64, 64)
        self.fc2 = nn.Linear(64, 2)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        feature_map1 = x.clone()
        x = torch.relu(self.conv2(x))
        feature_map2 = x.clone()
        x = torch.flatten(x, 1)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x, feature_map1, feature_map2

def visualize_and_save_image(image_path, model, transform, device):
    model.eval()
    image = Image.open(image_path).convert("RGB")
    transformed_image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        _, feature_map1, feature_map2 = model(transformed_image)

    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    axs[0].imshow(image)
    axs[0].set_title("Original Image")
    axs[0].axis("off")

    def plot_feature_map(ax, fmap, idx, title):
        fmap = fmap.squeeze(0).cpu()
        fmap = fmap[idx].detach().numpy()
        ax.imshow(fmap, cmap="viridis")
        ax.set_title(title)
        ax.axis("off")

    plot_feature_map(axs[1], feature_map1, 0, "Feature Map 1 (Conv1)")
    plot_feature_map(axs[2], feature_map2, 0, "Feature Map 2 (Conv2)")

    feature_map_combined = feature_map2.mean(dim=1).squeeze(0).cpu()
    Image.fromarray((feature_map_combined.numpy() * 255).astype('uint8')).save("processed_image.png")

    plt.show()
    print("Processed image saved as 'processed_image.png'")

def main():
    image_path = 'magic.png'
    transform = transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.ToTensor()
    ])

    model = SimpleCNN()
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)

    if os.path.exists("simple_cnn.pth"):
        model.load_state_dict(torch.load("simple_cnn.pth", map_location=device))

    visualize_and_save_image(image_path, model, transform, device)

if __name__ == "__main__":
    main()
