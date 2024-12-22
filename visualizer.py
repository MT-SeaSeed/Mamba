import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import numpy as np

class DatasetVisualizer:
    def __init__(self, dataset):
        self.dataset = dataset

    def plot_class_distribution(self, figsize=(15, 5)):
        plt.figure(figsize=figsize)
        class_dist = self.dataset.load_metadata()["class_distribution"]
        plt.bar(range(len(class_dist)), list(class_dist.values()))
        plt.title(f'{"Train" if self.dataset.is_train else "Test"} Dataset Class Distribution')
        plt.xlabel('Class Index')
        plt.ylabel('Number of Images')
        plt.show()

    def show_sample_images(self, num_samples=5, figsize=(15, 3)):
        plt.figure(figsize=figsize)
        images, labels = self.dataset.get_batch(num_samples)
        
        for i in range(num_samples):
            plt.subplot(1, num_samples, i+1)
            plt.imshow(images[i])
            plt.title(f'Class: {self.dataset.classes[labels[i]]}')
            plt.axis('off')
        plt.show()

    def analyze_image_sizes(self, sample_size=100):
        widths, heights = [], []
        for i in range(min(sample_size, len(self.dataset.image_paths))):
            stats = self.dataset.preprocessor.get_image_stats(self.dataset.image_paths[i])
            widths.append(stats["size"][0])
            heights.append(stats["size"][1])

        plt.figure(figsize=(12, 4))
        plt.subplot(1, 2, 1)
        plt.hist(widths, bins=30)
        plt.title('Image Width Distribution')
        plt.subplot(1, 2, 2)
        plt.hist(heights, bins=30)
        plt.title('Image Height Distribution')
        plt.show()
