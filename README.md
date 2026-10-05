# 🏋️ Push-Up Counter

A real-time push-up counter built with **Python, OpenCV, and MediaPipe**.

The application uses a webcam to detect the user's body position and automatically count push-ups based on the movement of the nose relative to the shoulders.

## 📌 Overview

This project uses **MediaPipe Pose** to track body landmarks through a webcam.

The program monitors the position of the nose compared to the average position of both shoulders.

When the user moves down and then returns to the up position, one push-up is counted.

The camera feed is displayed in real time with the current push-up count and movement state.

## ✨ Features

* 🎥 Real-time webcam processing
* 🧍 Human pose detection using MediaPipe
* 🔢 Automatic push-up counting
* 🔄 UP / DOWN movement detection
* 🪞 Mirrored camera display
* 💪 Shoulder tracking visualization
* ⚡ Real-time processing
* ⌨️ Press `Q` to exit

## 🛠️ Technologies

* Python
* OpenCV
* MediaPipe

## 📦 Requirements

Make sure you have Python installed.

The required Python packages are:

```text
opencv-python
mediapipe
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/push-up-counter.git
```

### 2. Enter the project directory

```bash
cd push-up-counter
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the program:

```bash
python main.py
```

A webcam window will open automatically.

Stand in front of the camera and perform push-ups.

The application will display:

```text
Push-ups: 10
UP
```

The counter increases when the detected movement changes from:

```text
DOWN → UP
```

Press:

```text
Q
```

to close the application.

## 🧠 How It Works

The application uses MediaPipe Pose to detect body landmarks.

The main landmarks used by the program are:

* Nose
* Left Shoulder
* Right Shoulder

The average vertical position of the shoulders is calculated:

```python
shoulder = (left.y + right.y) / 2
```

Then the vertical distance between the nose and shoulders is calculated:

```python
movement = nose.y - shoulder
```

The program uses this value to determine whether the user is moving:

* `DOWN`
* `UP`

A push-up is counted when the state changes from:

```text
DOWN → UP
```

A short cooldown is also used to prevent multiple counts from being triggered by the same movement.

## 📊 Detection Logic

The movement thresholds are currently:

```python
if movement > 0.03:
    new_state = "DOWN"

elif movement < -0.01:
    new_state = "UP"
```

These values can be adjusted depending on the camera angle and the user's position.

## 📁 Project Structure

```text
push-up-counter/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

### `main.py`

Contains the main application logic, webcam processing, pose detection, movement detection, and push-up counting.

### `requirements.txt`

Contains the Python dependencies required to run the project.

### `.gitignore`

Prevents unnecessary files such as virtual environments, cache files, and IDE configuration files from being uploaded to GitHub.

## ⚙️ Configuration

The MediaPipe detection settings can be changed in `main.py`.

Current configuration:

```python
min_detection_confidence=0.5
min_tracking_confidence=0.5
```

The push-up movement thresholds can also be adjusted:

```python
movement > 0.03
movement < -0.01
```

The counting cooldown is:

```python
0.25
```

seconds.

## 🎥 Camera

The application uses the default webcam:

```python
cap = cv2.VideoCapture(0)
```

If you have multiple cameras, you may need to change the camera index:

```python
cap = cv2.VideoCapture(1)
```

## ⚠️ Troubleshooting

### Camera does not open

Make sure:

* Your webcam is connected.
* No other application is using the webcam.
* Camera permissions are enabled for Python/PyCharm.

You can also try changing:

```python
cv2.VideoCapture(0)
```

to:

```python
cv2.VideoCapture(1)
```

### Push-ups are not detected correctly

Try changing the movement thresholds:

```python
if movement > 0.03:
```

and:

```python
elif movement < -0.01:
```

The optimal values may depend on camera position, distance, and body posture.

### MediaPipe installation problem

Try upgrading pip:

```bash
python -m pip install --upgrade pip
```

Then reinstall the dependencies:

```bash
pip install -r requirements.txt
```

## 🔮 Future Improvements

Possible improvements for future versions:

* Support different camera angles
* Improve push-up detection accuracy
* Detect body orientation automatically
* Add workout history
* Save workout statistics
* Add a graphical user interface
* Add repetition speed tracking
* Add multiple exercise types
* Add audio feedback
* Store workout data in SQLite

## 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

## 👨‍💻 Author

**itsMohammwd**

Built with Python, OpenCV, and MediaPipe.
