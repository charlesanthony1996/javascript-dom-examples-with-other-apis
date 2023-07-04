# from PIL import Image
# import cv2
# import numpy as np
# import pandas as pd
# import tensorflow as tf

# from pdf2image import convert_from_path

# images = convert_from_path('/users/charles/desktop/javascript-dom/Reflections.pdf')

# print("test")

# # conversion
# for i in range(len(images)):
#     images[i].save("pages/page" +str(i)+ ".jpg" , "JPEG")


# # layout
# a = 5

# import cv2
# import layoutparser as lp
# image = cv2.imread("./pages/page0.jpg")



# # for i in range(len(images)):
# #     image = cv2.imread("pages/page" + str(i) + ".jpg")

#     # reverse color channels
# image = image[..., ::-1]
# print("test line 2")

# # load model
# model = lp.PaddleDetectionLayoutModel(config_path="lp://PubLayNet/ppyolov2_r50vd_dcn_365e_publaynet/config", threshold=0.5, label_map={0: "Text", 1:"Title", 2:"List", 4:"Table", 5:"Figure"},
# enforce_cpu=False, enable_mkldnn=True)


# went into some problems with the layoutparser api

from PIL import Image
import cv2
import numpy as np
import pandas as pd
import tensorflow as tf
from pdf2image import convert_from_path
import layoutparser as lp
# from layoutparser import PaddleDetectionLayoutModel
# from layoutparser import Detectron2LayoutModel
from layoutparser import AutoLayoutModel
# from layoutparser import EfficientDetLayoutModel

# convert pdf to image
images = convert_from_path('/users/charles/desktop/javascript-dom/Reflections.pdf')

# conversion
for i in range(len(images)):
    images[i].save("pages/page" + str(i) + ".jpg", "JPEG")


# a = 5

# layout
# import layoutparser as lp
# image = cv2.imread("./pages/page0.jpg")

# for i in range(len(images)):
#     image = cv2.imread("pages/page" + str(i) + ".jpg")

    # reverse color channels
    
    # model = lp.Detectron2LayoutModel(
    #     config_path ="lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config",
    #     label_map = {0: "Text", 1: "Title", 2:"List", 3: "Table", 4:"Figure"},
    #     enforce_cpu=False,
    #     extra_config =["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.8]
    # )

model = lp.PaddleDetectionLayoutModel(config_path="lp://PubLayNet/ppyolov2_r50vd_dcn_365e_publaynet/config", threshold=0.5, label_map={0: "Text", 1:"Title", 2:"List", 4:"Table", 5:"Figure"},
    enforce_cpu=False, enable_mkldnn=True)

# model = lp.AutoLayoutModel(config_path="lp://EfficientDete/PubLayNet")

# model = lp.Detectron2LayoutModel(
#     config_path ="lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config",
#     label_map={0: "Text", 1: "Title", 2:"List", 3:"Table", 4:"Figure"},
#     extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.8]
# )


for i in range(len(images)):
    image_path = "pages/page" + str(i) + ".jpg"

    image = cv2.imread(image_path)

    # reverse color channels
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # load the images
    layout = model.detect(image)



# this tutorial was stopped after hitting some errors
# current python version doesnt seem to support layoutparser'e libraries
