import csv
from pathlib import Path
from ultralytics import YOLO

def main():
    # 设置路径 - 如果您训练了多个模型，可以在这里添加
    model_paths = [
        Path("d:/Trae programes/交通标志检测/第4次实验数据及提交格式/runs/detect/train3/weights/best.pt"),
    ]
    
    # 如果您训练了v8m模型，可以取消下面的注释
    # model_paths.append(Path("d:/Trae programes/交通标志检测/第4次实验数据及提交格式/runs/detect/train_v8m/weights/best.pt"))
    
    test_dir = Path("d:/Trae programes/交通标志检测/第4次实验数据及提交格式/test/images")
    output_path = Path("d:/Trae programes/交通标志检测/第4次实验数据及提交格式/submission_ensemble.csv")
    
    print(f"加载 {len(model_paths)} 个模型...")
    models = [YOLO(path) for path in model_paths]
    
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
        
        for i, img_path in enumerate(image_paths):
            image_id = img_path.name
            if (i + 1) % 20 == 0:
                print(f"处理进度: {i+1}/{len(image_paths)}")
            
            # 用所有模型预测
            all_boxes = []
            for model_idx, model in enumerate(models):
                results = model.predict(
                    source=str(img_path),
                    conf=0.001,
                    iou=0.5,
                    imgsz=640,
                    augment=True,
                    max_det=100,
                    save=False,
                    verbose=False
                )
                
                for result in results:
                    if result.boxes is None:
                        continue
                    for box in result.boxes:
                        x_center, y_center, width, height = box.xywhn[0].tolist()
                        all_boxes.append({
                            "class_id": int(box.cls[0].item()),
                            "x_center": x_center,
                            "y_center": y_center,
                            "width": width,
                            "height": height,
                            "confidence": float(box.conf[0].item()),
                        })
            
            # 写入所有预测
            for box in all_boxes:
                writer.writerow({
                    "image_id": image_id,
                    "class_id": box["class_id"],
                    "x_center": box["x_center"],
                    "y_center": box["y_center"],
                    "width": box["width"],
                    "height": box["height"],
                    "confidence": box["confidence"],
                })
    
    print(f"\n集成推理完成！结果已保存到: {output_path}")
    print(f"请将此文件提交到比赛平台！")

if __name__ == "__main__":
    main()
