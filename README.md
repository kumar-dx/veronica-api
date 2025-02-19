# AGI People Counter

A real-time people counting system using computer vision and deep learning.

## Features

- Real-time person detection using YOLOv8
- RTSP camera stream support
- Local image saving of detected persons
- Optional S3 upload capability
- Configurable detection confidence threshold

## Camera Configuration

Current camera settings:
- IP Address: 0.0.0.0
- Channel: CH05
- RTSP Port: 554
- Stream Paths:
  - Main Stream: /ch05/0
  - Sub Stream: /ch05/1

## Setup Instructions

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file from `.env.sample` and configure:

```bash
# Camera Configuration
CAMERA_IP=192.168.0.193
CAMERA_RTSP_PORT=554
CAMERA_USERNAME=admin
CAMERA_PASSWORD=admin
CAMERA_MAX_RETRIES=3
CAMERA_RETRY_DELAY=5
CAMERA_MAIN_STREAM_PATH=/ch05/0
CAMERA_SUB_STREAM_PATH=/ch05/1
RTSP_ENV_OPTIONS=rtsp_transport;tcp

# Optional S3 Configuration (if using S3 upload)
S3_BUCKET_NAME=your-bucket-name
AWS_ACCESS_KEY=your-access-key
AWS_SECRET_KEY=your-secret-key
AWS_REGION=your-aws-region
```

## Usage

Run the main script:

```bash
python main.py
```

The script will:

1. Connect to the configured camera stream
2. Process frames in real-time using YOLOv8
3. Detect and count people in the video feed
4. Save detection images locally
5. Upload to S3 if configured

Press 'q' to quit the application.

## Project Structure

```
.
├── config/               # Configuration files
│   ├── camera_config.py  # Camera settings
│   ├── model_config.py   # ML model settings
│   └── s3_config.py      # S3 upload settings
├── core/                 # Core functionality
│   ├── detector.py       # Person detection
│   ├── frame_processor.py # Frame processing
│   └── stream_handler.py  # Video stream handling
├── utils/                # Utility functions
│   ├── file_utils.py     # File operations
│   ├── fps_tracker.py    # FPS monitoring
│   ├── s3_utils.py       # S3 upload
│   └── visualization.py  # Display utilities
├── .env                  # Environment variables
├── main.py              # Main entry point
└── requirements.txt      # Dependencies
```

## Hardware Requirements

- Camera with RTSP stream support
- Python 3.8 or higher
- Sufficient CPU/GPU for real-time processing
- PostgreSQL database server

## API Endpoints

The analytics backend provides the following REST API endpoints:

- `GET /api/v1/analytics/records/`: List all detection records
- `POST /api/v1/analytics/visitors/` Create a new detection record
- `GET /api/v1/analytics/stores/metrics/?store_id=<store_id>&date=<date>`: Retrieve a specific detection record (date is an optional parameter)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
