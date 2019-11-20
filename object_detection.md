
## deep learning object detection

A paper list of object detection using deep learning.

### Table of Contents
- Paper list from 2014 to now(2019)
- Performance table
- Dataset Papers

### Paper list from 2014 to now(2019)

The part highlighted with red characters means papers that i think **"must-read"**. 

![deep_learning_object_detection_history.png](http://image.jingsnow.com/image/deep_learning_object_detection_history.png)


### Performance table

FPS(Speed) index is related to the hardware spec(e.g. CPU, GPU, RAM, etc), so it is hard to make an equal comparison. The solution is to measure the performance of all models on hardware with equivalent specifications, but it is very difficult and time consuming.

|  Detector  | VOC07(mAP@IoU=0.5)    | VOC12(mAP@IoU=0.5)   | COCO(mAP@IoU=0.5:0.95)      |  Published In |
|:--------|:--------:|:--------:|:--------:|:--------:|
| R-CNN | 58.5 | - | -  | CVPR'14 |
| SPP-Net	| 59.2 |	-  | -	| ECCV'14 |
|MR-CNN	|78.2 (07+12)|	73.9 (07+12)|	-	| ICCV'15 |
| Fast R-CNN |	70.0 (07+12) |	68.4 (07++12)	|19.7 |	ICCV'15 |
| Faster R-CNN |	73.2 (07+12) |	70.4 (07++12)|	21.9 |	NIPS'15 |
| YOLO v1 |	66.4 (07+12) |	57.9 (07++12) |	- |	CVPR'16 |
| G-CNN	| 66.8 |	66.4 (07+12) |	- |	CVPR'16 |
| AZNet	| 70.4 |	- |	22.3 |	CVPR'16 |
| ION	| 80.1 | 	77.9 |	33.1 |	CVPR'16 |
| HyperNet |	76.3 (07+12) |	71.4 (07++12) |	-	 | CVPR'16 |
| OHEM |	78.9 (07+12) |	76.3 (07++12) |	22.4 |	CVPR'16   |
| MPN |	- |	 - |	33.2 |	BMVC'16 |
|SSD|	76.8 (07+12)|	74.9 (07++12)|	31.2|	ECCV'16|
|GBDNet|	77.2| (07+12)|	-|	27.0|	ECCV'16|
|CPF|	76.4 (07+12)|	72.6 (07++12)|	-|	ECCV'16|
|R-FCN	|79.5 (07+12)|	77.6 (07++12)|	29.9|	NIPS'16|
|DeepID-Net|	69.0|	-	|-|	PAMI'16|
|NoC	|71.6 (07+12)	|68.8 (07+12)	|27.2|	TPAMI'16|
|DSSD	|81.5 (07+12)|	80.0 (07++12)|	33.2|	arXiv'17|
|TDM|	-	|-	|37.3	|CVPR'17|
|FPN|	-	|-|	36.2|	CVPR'17|
|YOLO v2|	78.6 (07+12)|	73.4 (07++12)|	-|	CVPR'17|
|RON|	77.6 (07+12)|	75.4 (07++12)|	27.4|	CVPR'17|
|DeNet|	77.1 (07+12)|	73.9 (07++12)|	33.8|	ICCV'17|
|CoupleNet|	82.7 (07+12)|	80.4 (07++12)|	34.4|	ICCV'17|
|RetinaNet|	-	|-	|39.1|	ICCV'17|
|DSOD	|77.7 (07+12)|	76.3 (07++12)	|-|	ICCV'17|
|SMN	|70.0|	-|	-	|ICCV'17|
|Light-Head R-CNN|	-	|-|	41.5|	arXiv'17|
|YOLO v3|	-	|-|	33.0|	arXiv'18|
|SIN|	76.0 (07+12)|	73.1 (07++12)|	23.2|	CVPR'18|
|STDN	|80.9 (07+12)|	-	|-|	CVPR'18|
|RefineDet|	83.8 (07+12)|	83.5 (07++12)|	41.8|	CVPR'18|
|SNIP|	-	|-	|45.7	|CVPR'18|
|elation-Network|	-|	-	|32.5|	CVPR'18|
|Cascade R-CNN|	-	|-|	42.8|	CVPR'18|
|MLKP	|80.6 (07+12)|	77.2 (07++12)|	28.6|	CVPR'18|
|Fitness-NMS|	-	|-|	41.8|	CVPR'18|
|RFBNet|	82.2 (07+12)|	-|	-	|ECCV'18|
|CornerNet|	-	|-|	42.1|	ECCV'18|
|PFPNet|	84.1 (07+12)|	83.7 (07++12)|	39.4|	ECCV'18|
|Pelee|	70.9 (07+12)|	-|	-	|NIPS'18|
|HKRM|	78.8 (07+12)|	-|	37.8|	NIPS'18|
|M2Det|	-|	-|	44.2|	AAAI'19|
|R-DAD|	81.2 (07++12)|	82.0 (07++12)|	43.1|	AAAI'19|

### Dataset Papers
Statistics of commonly used object detection datasets. The Table came from [this survey paper](https://arxiv.org/pdf/1809.02165v1.pdf).

![deep_learning_object_detection_dataset.png](http://image.jingsnow.com/image/deep_learning_object_detection_dataset.png)


reference:https://github.com/hoya012/deep_learning_object_detection
