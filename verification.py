from mmseg.apis import inference_segmentor, init_segmentor
import mmcv

config_file = r'z_input\fcn_unet_s5-d16_128x128_10k_LeafDataset_T3.py'
checkpoint_file = r'z_input\fcn_unet_iter_10000.pth'

# build the model from a config file and a checkpoint file
model = init_segmentor(config_file, checkpoint_file, device='cpu')

# test a single image and show the results
img = 'demo\image-1550434545.jpg' #r'demo/Hexa plant 26.10.21.jpg'  # or img = mmcv.imread(img), which will only load it once
result = inference_segmentor(model, img)
# visualize the results in a new window
# model.show_result(img, result, show=True)
# or save the visualization results to image files
# you can change the opacity of the painted segmentation map in (0, 1].
model.show_result(img, result, out_file='result_T5.jpg', opacity=0.5)

# # test a video and show the results
# video = mmcv.VideoReader('video.mp4')
# for frame in video:
#    result = inference_segmentor(model, frame)
#    model.show_result(frame, result, wait_time=1)

'''
Things to fix to train once again.
Add pad and rescale factor, so no confiction in formatting.
Increase the number of iteration.
After training, I should change SyncBN to BN.

'''