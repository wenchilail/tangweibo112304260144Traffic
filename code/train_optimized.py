import os
import sys
from ultralytics import YOLO

# 切换到数据目录
os.chdir("d:/Trae programes/交通标志检测/第4次实验数据及提交格式")

# 使用更大的模型 - YOLOv8s (small版本)，比nano更准确
model = YOLO('yolov8s.pt')

# 优化的训练参数
results = model.train(
    data='data.yaml',
    epochs=100,           # 增加训练轮数
    imgsz=640,            # 更大的图像尺寸
    device=0,
    batch=16,             # 合适的batch size
    lr0=0.01,             # 初始学习率
    lrf=0.01,             # 最终学习率因子
    weight_decay=0.0005,  # 权重衰减
    momentum=0.937,       # 动量
    patience=50,          # 早停耐心值
    augment=True,         # 数据增强
    verbose=True,
    project='runs/detect',
    name='train_optimized'
)

# 在验证集上评估
print("\n--- 模型评估 ---")
metrics = model.val()
print(f"mAP@0.5: {metrics.box.map50:.4f}")
print(f"mAP@0.5-0.95: {metrics.box.map:.4f}")

print("\nTraining and evaluation completed!")
