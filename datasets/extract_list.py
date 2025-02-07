import os
import glob
from tqdm import tqdm
from constants import ROOT_PATH


split_image = f'{ROOT_PATH}/Seenomaly/Rico_Data/split_image'

def main():
  app_list = os.listdir(split_image)
  for app in tqdm(app_list):
    trace_list = glob.glob(os.path.join(split_image, app, 'trace_*'))
    for trace in trace_list:
      image_list = os.listdir(trace)
      with open(os.path.join(f'{ROOT_PATH}/Seenomaly/Rico_Data', 'file_list.txt'), 'a') as list_file: 
        for image in image_list:
          list_file.write(os.path.join(trace, image) + '\n') 
  
if __name__ == '__main__':
  main()
