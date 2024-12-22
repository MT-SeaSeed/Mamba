from dataset import VNPlant200Dataset
from visualizer import DatasetVisualizer

def main():
    # Initialize datasets
    train_dataset = VNPlant200Dataset("Dataset", is_train=True)
    test_dataset = VNPlant200Dataset("Dataset", is_train=False)
    
    # Create visualizers
    train_vis = DatasetVisualizer(train_dataset)
    test_vis = DatasetVisualizer(test_dataset)
    
    # Print dataset information
    print("\n=== Train Dataset Information ===")
    train_meta = train_dataset.load_metadata()
    print(f"Total images: {train_meta['total_images']}")
    print(f"Number of classes: {train_meta['num_classes']}")
    
    print("\n=== Test Dataset Information ===")
    test_meta = test_dataset.load_metadata()
    print(f"Total images: {test_meta['total_images']}")
    print(f"Number of classes: {test_meta['num_classes']}")
    
    # Visualize datasets
    train_vis.plot_class_distribution()
    train_vis.show_sample_images()
    train_vis.analyze_image_sizes()

if __name__ == "__main__":
    main()
