import os
import cv2
import h5py
import numpy as np
import random
from tqdm import tqdm

def store2hdf5(savepath, data, label):
    """
    Store data and label into hdf5 file.
    """
    hdf5_file = h5py.File(savepath, mode='w')
    hdf5_file.create_dataset("data", data.shape, np.float32)
    hdf5_file["data"][...] = data
    hdf5_file.create_dataset("label", label.shape, np.float32)
    hdf5_file["label"][...] = label
    hdf5_file.close()

def merge_hdf5(filepaths, merged_filepath):
    """
    Merge HDF5 files into one.
    """
    merged_data = []
    merged_label = []

    for filepath in filepaths:
        with h5py.File(filepath, 'r') as f:
            merged_data.append(f['data'][:])
            merged_label.append(f['label'][:])

    # Ensure all arrays have the same number of dimensions
    merged_data = [np.expand_dims(arr, axis=-1) if len(arr.shape) < 4 else arr for arr in merged_data]

    merged_data = np.concatenate(merged_data, axis=0)
    merged_label = np.concatenate(merged_label, axis=0)

    store2hdf5(merged_filepath, merged_data, merged_label)


folder = '91'  # 이미지 폴더 경로
folder2 = '91_h5'
size_input = 41  # 입력 이미지 크기
size_label = 41  # 라벨 이미지 크기
stride = 41  # 이미지 추출 간격

# scale factors
scale = [2, 3, 4]

# downsizing
downsizes = [1, 0.7, 0.5]

# 파일 경로들을 가져옵니다.
filepaths = [f for f in os.listdir(folder) if f.endswith('.jpg') or f.endswith('.bmp')]

# 개별 이미지를 처리하고 HDF5 파일 생성
hdf5_filepaths = []
for filepath in tqdm(filepaths):
    all_data = []
    all_label = []

    image = cv2.imread(os.path.join(folder, filepath))

    for flip in range(1, 4):
        for degree in range(1, 5):
            for s in range(len(scale)):
                for downsize in range(len(downsizes)):
                    processed_image = image.copy()

                    if flip == 1:
                        processed_image = np.flipud(processed_image)
                    elif flip == 2:
                        processed_image = np.fliplr(processed_image)
                    processed_image = np.rot90(processed_image, (degree - 1))

                    processed_image = cv2.resize(processed_image, None, fx=downsizes[downsize], fy=downsizes[downsize], interpolation=cv2.INTER_CUBIC)

                    if processed_image.shape[2] == 3:
                        processed_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2YCrCb)
                        processed_image = processed_image[:, :, 0].astype(float) / 255.0

                        im_label = processed_image[:-(processed_image.shape[0] % scale[s]), :-(processed_image.shape[1] % scale[s])]
                        if im_label.shape[0] == 0 or im_label.shape[1] == 0:
                            continue

                        im_input = cv2.resize(cv2.resize(im_label, None, fx=1/scale[s], fy=1/scale[s], interpolation=cv2.INTER_CUBIC), (im_label.shape[1], im_label.shape[0]), interpolation=cv2.INTER_CUBIC)

                        for x in range(0, im_label.shape[0] - size_label + 1, stride):
                            for y in range(0, im_label.shape[1] - size_label + 1, stride):
                                subim_input = im_input[x:x+size_input, y:y+size_input]
                                subim_label = im_label[x:x+size_label, y:y+size_label]

                                all_data.append(subim_input)
                                all_label.append(subim_label)

    all_data = np.array(all_data)
    all_label = np.array(all_label)

    # HDF5 파일로 저장
    savepath = os.path.join(folder2, f'{os.path.splitext(filepath)[0]}.h5')
    store2hdf5(savepath, all_data, all_label)
    hdf5_filepaths.append(savepath)

# 병합된 HDF5 파일 생성
merged_filepath = 'train_merged.h5'
merge_hdf5(hdf5_filepaths, merged_filepath)
print(f"Merged HDF5 file created: {merged_filepath}")

