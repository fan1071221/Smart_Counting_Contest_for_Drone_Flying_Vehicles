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
類別|模型名稱/用途|Jupyter Notebook|權重檔|模型預測結果|
--|--|--|--|--|
model_640|640|[yolov7.ipynb](https://github.com/JulianLee3105214065/AICtation/blob/main/tf_efficientnetv2_m_in21ft1k.ipynb)|[model_640.pt](https://drive.google.com/file/d/1R8ez_bH2H5KsshnWdeA4rcYTcUcqbHhD/view?usp=sharing)|[模型一結果](https://github.comesult/tf_efficientnetv2_m_in21ft1k_origin.zip)|
model_1280|1280|[yolov7.ipynb](https://github.com/Jee3105514065/AICUP_STAS_Segmentation/blob/main/tu-eca_nfnet_l2_DeepLabV3Plus.ipynb)|[model_640.pt](https://drive.google.com/file/d/1Cbgkb0SNsghGo8x0SgHgYPR9kAbOJjLA/view?usp=sharing)|[模型二結果](https://github.com/main/Result/tu-eca_nfnet_l2_DeepLabV3Plus_origin.zip)|
model_1920|1920|[yolov7.ipynb](https://github.com/3410514065/AICUP_STAS_Segmentation/blob/main/tu-tf_efficientnet_b6_ns.ipynb)|[tu.pt](https://drive.google.com/file/d/1lkkzq2SbDvxgvNDKGoGMiRDNEZ7399Cm/view?usp=sharing)|[模型三結果](https://github.n/blob/main/Result/tu-tf_efficientnet_b6_nsorigin.zip)
Ensemble|NMS Ensemble|[Image_ensemble.ipynb](https://github.com/Jue31065/AICUP_STAS_Segmentation/blob/main/Image_ensemble.ipynb)|-|[最後結果](https://github.com/esult/Finall%20ensemble.zip)|

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
  


