# Smart_Counting_Contest_for_Drone_Flying_Vehicles
AI CUP 2022
  
Private Rank: 9th
## TEAM_2189: [Hong-Wei Fan](https://github.com/fan1071221)

- [**無人機飛行載具之智慧計數競賽**](https://tbrain.trendmicro.com.tw/Competitions/Details/25)  


<a href="https://tbrain.trendmicro.com.tw/Competitions/Details/25"><img src="https://i.ibb.co/6PtWBSV/competition-image.png" title="#source: imgur.com" /></a>  

## Installation
<pre><code> 
!git clone https://github.com/fan1071221/Smart_Counting_Contest_for_Drone_Flying_Vehicles.git
!pip install -r requirements.txt
</code></pre>


## Dataset  
You can refer the [**README.md**](dataset/README.md) to prepare the dataset.  

## Train each classifier  
Set hyperparameters and revelent training path in [**train.yaml**](train.yaml) and simply run [**train.py**](train.py).  

## Predict via each trained classifier  
You can download our pretrained model from [**pretrained**](./pretrained).  
To predict the orchid images by single classifier, see [**predict.py**](predict.py) and run:  
```
!python detect.py --weights best_1920.pt weight/e6e-best.pt --img 1920 --source /content/drive/MyDrive/public --augment
```
## Model and Weights
The models save to the google driver, then you can download
名稱|圖片大小|Jupyter Notebook|權重檔|模型預測結果|
--|--|--|--|--|
model_640|640*640|[YOLOv7-PRB-640.ipynb](https://github.com/fan1071221/Smart_Counting_Contest_for_Drone_Flying_Vehicles/blob/main/YOLOv7_PRB_640.ipynb)|[model_640.pt](https://drive.google.com/file/d/1MosJhlmaTHV15oxcR8AjtaLLAaIQuph4/view?usp=share_link)|[模型一結果](https://github.comesin.zip)|
model_1280|1280*1280|[YOLOv7-PRB-1280.ipynb](https://github.com/fan1071221/Smart_Counting_Contest_for_Drone_Flying_Vehicles/blob/main/YOLOv7_PRB_1280.ipynb)|[model_640.pt](https://drive.google.com/file/d/11e78nhtlcH_nhVLBI9tkTpt6ixQUnJI6/view?usp=share_link)|[模型二結果](https://github.com/main/Result/tu-eca_nfnet_l2_in.zip)|
model_1920|1920*1920|[YOLOv7-PRB-1920.ipynb](https://github.com/fan1071221/Smart_Counting_Contest_for_Drone_Flying_Vehicles/blob/main/YOLOv7_PRB_1920.ipynb)|[tu.pt](https://drive.google.com/file/d/1Zrun1Ek_8xsNdzaJT2BdX651vhNT1T4Y/view?usp=share_link)|[模型三結果](https://github.n/blob/msorigin.zip)
YOLOv7_E6E|1920*1920|[YOLOv7_E6E.ipynb](https://github.com/fan1071221/Smart_Counting_Contest_for_Drone_Flying_Vehicles/blob/main/YOLOv7_E6E.ipynb)|[tu.pt](https://drive.google.com/file/d/1Zrun1Ek_8xsNdzaJT2BdX651vhNT1T4Y/view?usp=share_link)|[模型三結果](https://github.n/blob/msorigin.zip)
Ensemble|1920*1920|[Ensemble.ipynb](https://github.com/fan1071221/Smart_Counting_Contest_for_Drone_Flying_Vehicles/blob/main/Ensemble.ipynb)|-|[最後結果](https://github.le.zip)|

## Final result  
  
- Score (accuracy) 

Public Score|Private Score
-------|-------
0.7356|0.753994
  

- (TEAM_2189) final rank: 9th
     
  

## Reference  
- https://github.com/pingyang1117/PRBNet_PyTorch
- https://github.com/WongKinYiu/yolov7


## Contact us  
- Hong-Wei Fan : q36111257@gs.ncku.edu.tw  
  


