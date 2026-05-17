import csv
from pathlib import Path
from ultralytics import YOLO

def main():
    # 设置路径
    model_path = Path("d:/Trae programes/交通标志检测/第4次实验数据及提交格式/runs/detect/train3/weights/best.pt")
    test_dir = Path("d:/Trae programes/交通标志检测/第4次实验数据及提交格式/test/images")
    output_path = Path("d:/Trae programes/交通标志检测/第4次实验数据及提交格式/submission_best.csv")
    
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
        
        # 使用更好的推理策略
        for i, img_path in enumerate(image_paths):
            image_id = img_path.name
            if (i + 1) % 20 == 0:
                print(f"处理进度: {i+1}/{len(image_paths)}")
            
            # 优化的预测参数
            results = model.predict(
                source=str(img_path),
                conf=0.0005,       # 非常低的置信度阈值
                iou=0.5,           # 更严格的NMS
                imgsz=640,         # 使用更大的尺寸
                augment=True,      # 测试时增强
                max_det=100,       # 增加最大检测数
                agnostic_nms=False,
                save=False,
                verbose=False
            )
            
            for result in results:
                if result.boxes is None:
                    continue
                for box in result.boxes:
                    x_center, y_center, width, height = box.xywhn[0].tolist()
                    # 只保留置信度比较高的
                    conf = float(box.conf[0].item())
                    if conf > 0.0005:
                        writer.writerow({
                            "image_id": image_id,
                            "class_id": int(box.cls[0].item()),
                            "x_center": x_center,
                            "y_center": y_center,
                            "width": width,
                            "height": height,
                            "confidence": conf,
                        })
    
    print(f"\n优化推理完成！结果已保存到: {output_path}")
    print(f"请将此文件提交到比赛平台！")

if __name__ == "__main__":
    main()
