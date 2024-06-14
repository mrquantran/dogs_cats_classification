import os

# Define the absolute path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# define the path to the images directory
IMAGES_PATH = os.path.join(BASE_DIR, "datasets/train")

# since we do not have a validation set or access to the testing data
# we need to take a number of images from the training data and use them instead
NUM_CLASSES = 2
NUM_VAL_IMAGES = 1250 * NUM_CLASSES
NUM_TEST_IMAGES = 1250 * NUM_CLASSES

# define the path to the output training, validation, and testing HDF5 files
TRAIN_HDF5 = os.path.join(BASE_DIR, "datasets/hdf5/train.hdf5")
VAL_HDF5 = os.path.join(BASE_DIR, "datasets/hdf5/val.hdf5")
TEST_HDF5 = os.path.join(BASE_DIR, "datasets/hdf5/test.hdf5")

# path to the output model file
MODEL_PATH = os.path.join(BASE_DIR, "output/alexnet_dogs_vs_cats.model")

# define the path to the dataset mean
DATASET_MEAN = os.path.join(BASE_DIR, "output/dogs_vs_cats_mean.json")

# define the path to the output directory used for storing plots, classification reports, etc.
OUTPUT_PATH = os.path.join(BASE_DIR, "output")