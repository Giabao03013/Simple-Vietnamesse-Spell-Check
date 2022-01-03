import re
import os
from tqdm import tqdm
import pickle
def read_data(folder_path):
    data = ''
    dirs = os.listdir(folder_path)
    for path in tqdm(dirs):
        file_paths = os.listdir(os.path.join(folder_path, path))
        for file_path in (file_paths):
            with open(os.path.join(folder_path, path, file_path), 'r',encoding='utf-8') as f:
                text = f.read()
                text = re.sub(r'[{}@_*>()\\#%+=\[\]]', '', text)
                data += '.' + text
    return data

data = read_data('Data')
pickle.dump(data,open('Data/Data.pkl', 'wb'))
print(data)


