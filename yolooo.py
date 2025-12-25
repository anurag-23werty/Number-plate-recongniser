from roboflow import Roboflow

# Initialize Roboflow with your API key
rf = Roboflow(api_key="MaTeJDvpgoiBJUCAei9S")

# Access the project from Roboflow Universe
project = rf.workspace("roboflow-universe-projects").project("license-plate-recognition-rxg4e")

# Choose the version you want
version = project.version(11)

# Download dataset (YOLOv8 format)
dataset = version.download("yolov8")

print("Dataset downloaded successfully!")
