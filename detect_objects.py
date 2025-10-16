from jetson_inference import detectNet
from jetson_utils import loadImage

# Load the pre-trained SSD MobileNet V2 model
net = detectNet("ssd-mobilenet-v2", threshold=0.5)

def run_detection(image_path):
    try:
        # Load image from file
        img = loadImage(image_path)

        # Run object detection
        detections = net.Detect(img)

        # Get class labels from detection results
        labels = [net.GetClassDesc(d.ClassID) for d in detections]

        if labels:
            return ", ".join(set(labels))
        else:
            return "None"
    except Exception as e:
        print("❌ Detection failed:", e)
        return "Detection error"


