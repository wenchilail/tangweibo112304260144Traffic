import os
import sys
from ultralytics import YOLO

# 切换到数据目录
os.chdir("d:/Trae programes/交通标志检测/第4次实验数据及提交格式")

# 使用更大的模型 - YOLOv8m (medium版本)，准确率会大幅提升！
print("=" * 60)
print("开始训练 YOLOv8m 模型...")
print("=" * 60)
model = YOLO('yolov8m.pt')

# 优化的训练参数
results = model.train(
    data='data.yaml',
    epochs=80,             # 训练轮数
    imgsz=640,             # 更大的图像尺寸
    device=0,
    batch=8,               # 根据显存调整batch size
    lr0=0.01,              # 初始学习率
    lrf=0.001,             # 最终学习率因子
    weight_decay=0.0005,   # 权重衰减
    momentum=0.937,        # 动量
    patience=30,           # 早停耐心值
    augment=True,          # 数据增强
    mosaic=1.0,            # 马赛克增强
    mixup=0.1,             # mixup增强
    copy_paste=0.1,        # 复制粘贴增强
    verbose=True,
    project='runs/detect',
    name='train_v8m'
)

# 在验证集上评估
print("\n" + "=" * 60)
print("模型评估")
print("=" * 60)
metrics = model.val()
print(f"mAP@0.5: {metrics.box.map50:.4f}")
print(f"mAP@0.5-0.95: {metrics.box.map:.4f}")

print("\nTraining and evaluation completed!")
