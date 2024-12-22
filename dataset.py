import os
from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split
from collections import Counter

class BaseDataset:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.classes = []
        self.image_paths = []
        self.labels = []
        
    def load_metadata(self):
        """Load basic dataset metadata"""
        return {
            "total_images": len(self.image_paths),
            "num_classes": len(self.classes),
            "class_distribution": Counter(self.labels)
        }

class ImagePreprocessor:
    @staticmethod
    def preprocess_image(image_path, target_size=(224, 224)):
        img = Image.open(image_path)
        img = img.convert('RGB')
        img = img.resize(target_size)
        return np.array(img) / 255.0

    @staticmethod
    def get_image_stats(image_path):
        img = Image.open(image_path)
        return {
            "size": img.size,
            "mode": img.mode,
            "format": img.format
        }

class VNPlant200Dataset(BaseDataset):
    def __init__(self, base_dir, is_train=True):
        super().__init__(base_dir)
        self.is_train = is_train
        self.data_dir = os.path.join(base_dir, 'train' if is_train else 'test')
        self.preprocessor = ImagePreprocessor()
        self._load_dataset()
        
    def _load_dataset(self):
        self.classes = sorted(os.listdir(self.data_dir))
        for class_idx, class_name in enumerate(self.classes):
            class_path = os.path.join(self.data_dir, class_name)
            for img_name in os.listdir(class_path):
                img_path = os.path.join(class_path, img_name)
                self.image_paths.append(img_path)
                self.labels.append(class_idx)
                
    def get_batch(self, batch_size=32, target_size=(224, 224)):
        indices = np.random.choice(len(self.image_paths), batch_size)
        batch_images = []
        batch_labels = []
        
        for idx in indices:
            img = self.preprocessor.preprocess_image(
                self.image_paths[idx], 
                target_size
            )
            batch_images.append(img)
            batch_labels.append(self.labels[idx])
            
        return np.array(batch_images), np.array(batch_labels)
