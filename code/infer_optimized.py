import csv
from pathlib import Path
import numpy as np
from ultralytics import YOLO

def main():
    # 设置路径
    model_path = Path("d:/Trae programes/交通标志检测/第4次实验数据及提交格式/runs/detect/train3/weights/best.pt")
    test_dir = Path("d:/Trae programes/交通标志检测/第4次实验数据及提交格式/test/images")
    output_path = Path("d:/Trae programes/交通标志检测/第4次实验数据及提交格式/submission_optimized.csv")
    
    print(f"加载模型: {model_path}")
    model = YOLO(model_path)
    
    # 获取所有图片
    image_paths = sorted([p for p in test_dir.iterdir() if p.is_file()])
    print(f"找到 {len(image_paths)} 张测试图片")
    
    # 进行预测并生成提交文件
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["image_id", "class_id", "x_center", "y_center", "width", "height", "confidence"],
        )
        writer.writeheader()
        
        # 使用TTA (Test Time Augmentation) 和多尺度测试
        for i, img_path in enumerate(image_paths):
            image_id = img_path.name
            if (i + 1) % 10 == 0:
                print(f"处理进度: {i+1}/{len(image_paths)}")
            
            # 多尺度预测
            results = model.predict(
                source=str(img_path),
                conf=0.001,        # 降低置信度阈值
                iou=0.6,           # NMS的IoU阈值
                imgsz=[640, 416],  # 多尺度
                augment=True,      # 测试时增强
                save=False,
                verbose=False
            )
            
            for result in results:
                if result.boxes is None:
                    continue
                for box in result.boxes:
                    x_center, y_center, width, height = box.xywhn[0].tolist()
                    writer.writerow({
                        "image_id": image_id,
                        "class_id": int(box.cls[0].item()),
                        "x_center": x_center,
                        "y_center": y_center,
                        "width": width,
                        "height": height,
                        "confidence": float(box.conf[0].item()),
                    })
    
    print(f"\n优化推理完成！结果已保存到: {output_path}")
    print(f"原始提交文件位置: d:/Trae programes/交通标志检测/第4次实验数据及提交格式/submission.csv")
    print(f"优化后的提交文件位置: {output_path}")

if __name__ == "__main__":
    main()
