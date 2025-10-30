# DriveSure

## Project Overview

DriveSure aims to be a safety-focused application, although a detailed description is currently unavailable. Based on the included files, it seems to incorporate real-time data analysis, potential image processing, and machine learning models for features such as fog detection, pothole detection, and tire degradation assessment. A Streamlit dashboard is included for visualization and interaction.

## Key Features & Benefits

-   **Real-time Data Analysis:** Potentially analyzes live video or data streams to identify potential hazards.
-   **Fog Detection:** Uses a machine learning model to detect fog conditions.
-   **Pothole Detection:** Employs a deep learning model to identify potholes in real-time.
-   **Tire Degradation Assessment:** Utilizes a neural network to predict tire degradation levels.
-   **Streamlit Dashboard:** Provides a user-friendly interface for visualizing data and interacting with the system.
-   **WebRTC Integration:** Allows integration with webcams to obtain video data for analysis.

## Prerequisites & Dependencies

Before you begin, ensure you have the following installed:

-   **Python:** Version 3.6 or higher is recommended.
-   **pip:** Python package installer (usually included with Python).

You will also need to install the following Python libraries:

-   streamlit
-   tensorflow
-   scikit-learn
-   numpy
-   pandas
-   opencv-python
-   streamlit-lottie
-   streamlit-webrtc

## Installation & Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/LaxmiVarshithaCH/DriveSure.git
    cd DriveSure
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Download necessary models (if not already present):**

    Ensure the following files are in the project directory:
    - `fog_detection_model.pkl`
    - `fog_scaler.pkl`
    - `pothole_model.h5`
    - `scaler-2.pkl`
    - `tire_degradation_nn_model.h5`
    - `car_animation.json`
    - `tire_predictions.csv`

    If these are not included in the repository, contact the owner or check for alternative download locations within the project's documentation (if available).

5.  **Run the Streamlit dashboard:**

    ```bash
    streamlit run dashboard.py
    ```

    This command will launch the Streamlit application in your web browser.

## Usage Examples

The primary entry point for this project is the `dashboard.py` script.  Upon running the application, the Streamlit dashboard will become accessible in your browser. The specific functionality within the dashboard is determined by the code in `dashboard.py`.

The `dashboard.py` file likely implements the following functionalities (based on its imports and included files):

-   **Fog Detection:**  Uses the `fog_detection_model.pkl` and `fog_scaler.pkl` files to predict fog conditions based on input data.
-   **Pothole Detection:** Leverages the `pothole_model.h5` model for pothole detection from video streams.
-   **Tire Degradation Assessment:** Utilizes the `tire_degradation_nn_model.h5` to predict tire wear.
-   **Webcam Integration:** Integrates with your webcam using `streamlit-webrtc`.

*Note:* Without further documentation or a more detailed description, the exact implementation of these features within the dashboard cannot be fully detailed.

## Configuration Options

Currently, there are no specified configuration options. However, the Streamlit dashboard itself may have interactive elements that allow you to modify parameters during runtime. Refer to the dashboard's user interface for any available configuration settings.

## Contributing Guidelines

Contributions are welcome! To contribute to this project, follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix:

    ```bash
    git checkout -b feature/your-feature-name
    ```

3.  Make your changes and commit them with descriptive messages.
4.  Push your branch to your forked repository.
5.  Submit a pull request to the main repository.

Please ensure that your code adheres to the existing style guidelines and includes appropriate tests.

## License Information

No license information is provided in the repository. Please contact the owner, LaxmiVarshithaCH, to clarify the licensing terms.  If no license is specified, the code is implicitly under copyright by the owner, and you are not authorized to distribute, modify, or use it without explicit permission.

## Acknowledgments

The project leverages the following open-source libraries:

-   Streamlit
-   TensorFlow
-   scikit-learn
-   NumPy
-   Pandas
-   OpenCV
-   streamlit-lottie
-   streamlit-webrtc
