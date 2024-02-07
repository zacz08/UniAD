import sys
sys.path.append("/home/zc/UniAD")
import cv2
import argparse
import os
import glob

def to_video(folder_path, out_path, fps=4, downsample=1):
        imgs_path = glob.glob(os.path.join(folder_path, '*.jpg'))
        imgs_path = sorted(imgs_path)
        img_array = []
        for img_path in imgs_path:
            img = cv2.imread(img_path)
            height, width, channel = img.shape
            img = cv2.resize(img, (width//downsample, height //
                             downsample), interpolation=cv2.INTER_AREA)
            height, width, channel = img.shape
            size = (width, height)
            img_array.append(img)
            print("Appending image: ", img_path)
        out = cv2.VideoWriter(
            out_path, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
        for i in range(len(img_array)):
            out.write(img_array[i])
            print("Writing frame: ", i)
        out.release()

def main(args):
    if not os.path.exists(args.out_folder):
        os.makedirs(args.out_folder)

    to_video(args.out_folder, args.demo_video, fps=10, downsample=2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--predroot', default='/home/zc/UniAD/output/results.pkl', help='Path to results.pkl')
    parser.add_argument('--out_folder', default='/home/zc/UniAD/output/v1.0-trainval_10000', help='Output folder path')
    parser.add_argument('--demo_video', default='test_val_final.avi', help='Demo video name')
    parser.add_argument('--project_to_cam', default=True, help='Project to cam (default: True)')
    args = parser.parse_args()
    main(args)
