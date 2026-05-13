# 交通标志检测实验

本仓库用于记录交通标志检测课程实验的所有内容。

## 项目结构

```
.
├── code/              # 实验代码
│   ├── train_model.py  # 训练脚本
│   ├── run_infer.py    # 推理脚本
│   ├── baseline_infer.py # 基准推理脚本
│   └── data.yaml      # 数据配置文件
├── report/            # 实验报告
│   └── 第四次实验报告.md  # 第四次实验报告
├── results/           # 实验结果
│   ├── results.csv    # 训练结果数据
│   ├── results.png    # 训练结果图表
│   ├── BoxPR_curve.png # PR曲线
│   └── confusion_matrix.png # 混淆矩阵
└── README.md          # 本文件
```

## 实验内容

### 第四次实验
- **任务**: 交通标志目标检测
- **模型**: YOLOv8
- **GPU**: NVIDIA GeForce RTX 4060 Laptop GPU
- **主要指标**:
  - mAP@0.5: 94.43%
  - mAP@0.5-0.95: 81.23%
  - Precision: 94.84%
  - Recall: 87.81%

## 使用说明

### 训练模型
```bash
cd code
python train_model.py
```

### 推理
```bash
cd code
python run_infer.py
```

## 提交文件

比赛提交文件位于: `code/submission.csv`

## Git使用说明

### 初始化仓库
```bash
git init
```

### 提交更改
```bash
git add .
git commit -m "提交说明"
```

### 推送到GitHub
```bash
git remote add origin <你的仓库地址>
git branch -M main
git push -u origin main
```

## 注意事项

- 不要提交大的数据集和模型文件（已在.gitignore中配置）
- 每次实验后及时提交
- 提交说明要清晰明确
