# Smart_Counting_Contest_for_Drone_Flying_Vehicles
AI CUP 2022
  
Private Rank: 9th
## TEAM_2189: [Hong-Wei Fan](https://github.com/fan1071221)

- [**無人機飛行載具之智慧計數競賽**](https://tbrain.trendmicro.com.tw/Competitions/Details/25)  


<a href="https://tbrain.trendmicro.com.tw/Competitions/Details/25"><img width="800" height="200" src="https://i.ibb.co/6PtWBSV/competition-image.png" title="#source: imgur.com" /></a>  
## Architecture Diagram
- Training Model Architecture
<img width="650" height="250" src="https://github.com/fan1071221/Smart_Counting_Contest_for_Drone_Flying_Vehicles/blob/main/Architecture_Diagram/Training_Architecture.png" title="#source: imgur.com" />  

- Ensemble Two Models
<img width="650" height="175" src="https://github.com/fan1071221/Smart_Counting_Contest_for_Drone_Flying_Vehicles/blob/main/Architecture_Diagram/Ensemble_Detect.png" title="#source: imgur.com" />


## How to use
You can refer to followiing ipynb, I have already described in detail.  
 - [**AICUP_Drone.ipynb**](https://github.com/fan1071221/Smart_Counting_Contest_for_Drone_Flying_Vehicles/blob/main/AICUP_Drone.ipynb)
## Installation
<pre><code> 
!git clone https://github.com/fan1071221/Smart_Counting_Contest_for_Drone_Flying_Vehicles.git
!pip install -r requirements.txt
</code></pre>


## Dataset  
You can refer to the [**Data_Processing**](https://github.com/fan1071221/Smart_Counting_Contest_for_Drone_Flying_Vehicles/tree/main/Data_Processing) to processing the dataset.  

## Train each classifier  
Set hyperparameters and revelent training path in [**TWStreet.yaml**](https://github.com/fan1071221/Smart_Counting_Contest_for_Drone_Flying_Vehicles/blob/main/prb/data/TWStreet.yaml) and run [**train.py**](https://github.com/fan1071221/Smart_Counting_Contest_for_Drone_Flying_Vehicles/blob/main/prb/train.py).  
```
!python train.py --batch-size 2 --data data/TWStreet.yaml --epochs 600 --img 1920 --cfg cfg/training/PRB_Series/yolov7-PRB.yaml --weights 'yolov7-prb.pt' --name yolov7-prb-custom --hyp data/hyp.scratch.custom.yaml
```

## Predict via each trained classifier  
You can download our pretrained model from [**pretrained**](https://drive.google.com/drive/folders/1EchhQHj8jSsg1SAR4GpvZw_OJaNTsT8o?usp=sharing).  
To predict the images by two classifier, see [**detect.py**](https://github.com/fan1071221/Smart_Counting_Contest_for_Drone_Flying_Vehicles/blob/main/prb/detect.py) and run:  
```
!python detect.py --weights weight/best_1920.pt weight/e6e-best.pt --img 1920 --source /content/drive/MyDrive/public --augment
```
## Model and Weights
The models save to the google driver, then you can download
Name|Image Size|Jupyter Notebook|Model|
--|--|--|--|
model_640|640*640|[YOLOv7-PRB-640.ipynb](https://github.com/fan1071221/Smart_Counting_Contest_for_Drone_Flying_Vehicles/blob/main/YOLOv7_PRB_640.ipynb)|[best_640.pt](https://drive.google.com/file/d/1MosJhlmaTHV15oxcR8AjtaLLAaIQuph4/view?usp=sharing)|
model_1280|1280*1280|[YOLOv7-PRB-1280.ipynb](https://github.com/fan1071221/Smart_Counting_Contest_for_Drone_Flying_Vehicles/blob/main/YOLOv7_PRB_1280.ipynb)|[best_1280.pt](https://drive.google.com/file/d/11e78nhtlcH_nhVLBI9tkTpt6ixQUnJI6/view?usp=sharing)|
model_1920|1920*1920|[YOLOv7-PRB-1920.ipynb](https://github.com/fan1071221/Smart_Counting_Contest_for_Drone_Flying_Vehicles/blob/main/YOLOv7_PRB_1920.ipynb)|[best_1920.pt](https://drive.google.com/file/d/1Zrun1Ek_8xsNdzaJT2BdX651vhNT1T4Y/view?usp=sharing)|
YOLOv7_E6E|1920*1920|[YOLOv7_E6E.ipynb](https://github.com/fan1071221/Smart_Counting_Contest_for_Drone_Flying_Vehicles/blob/main/YOLOv7_E6E.ipynb)|[e6e-best.pt](https://drive.google.com/file/d/13IKYlxlzy7zieYJwqqf9Z1Tp-x7xaHUr/view?usp=sharing)|
Ensemble|1920*1920|[Ensemble.ipynb](https://github.com/fan1071221/Smart_Counting_Contest_for_Drone_Flying_Vehicles/blob/main/Ensemble.ipynb)|----

## Final result  
  
- Score (accuracy) 

Public Score|Private Score
-------|-------
0.7356|0.753994
  

- (TEAM_2189) final rank: 9th
     
  

## Reference  
- https://github.com/pingyang1117/PRBNet_PyTorch
- https://github.com/WongKinYiu/yolov7
- https://github.com/ultralytics/yolov5
- https://github.com/EricArazo/PseudoLabeling

## Contact us  
- Hong-Wei Fan : q36111257@gs.ncku.edu.tw  
  


