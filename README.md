Project Title: Endanger Detect
--------

This project is a part of the AAI-521 course in the Applied Artificail Intelligence Program at the University of San Diego (USD).

Project Status: Completed 
-----

Installation:
-----
Before running the code use the links and steps below to download the datasets. 
## Large Files for Endanger Detect

Due to GitHub's file size limitations, the following files are hosted on Google Drive. You can download them using the links below:

- **Dataset (marine-animal-images.zip):** [Download here](https://drive.google.com/file/d/1zpF7kedXrpwEz46kcKfMzO1T0YczFRdI/view?usp=share_link)
- **Trained Model (marine_animal_model.h5):** [Download here](https://drive.google.com/file/d/1QQ1w0CzTR1HDmZwTWjPqPgIxT0ygIpmP/view?usp=share_link)

### Instructions

1. Download the files using the links above.
2. Extract the dataset and place it in the `DATASET` directory of the project.
3. Place the trained model file in the root directory of the project or update the code to point to its location.

How is it Used?
Endanger Detect is designed to identify marine animal species from uploaded images and provide their conservation status. The application is aimed at:

Wildlife researchers and conservationists to prioritize endangered species.
Photographers to gain insights into the animals they capture in their photos.
Educators and enthusiasts who want to learn more about marine biodiversity.
Users interact with the application through a simple graphical interface where they can:

Upload an image of a marine animal.
Receive the predicted species name.
View the conservation status of the species (e.g., "Endangered," "Vulnerable," or "Not Endangered").

Installation
Follow these steps to set up the project locally:

Clone the Repository:
  git clone https://github.com/sarahdurrani/AAI-521--Group-9--EndangerDetect.git
  cd AAI-521--Group-9--EndangerDetect
Set Up a Virtual Environment (Optional but Recommended):
  python3 -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Required Libraries: Install the necessary dependencies listed in the requirements.txt file:
  pip install -r requirements.txt
Download Additional Resources:
  Download the trained model file (marine_animal_model.h5) from Google Drive link and place it in the project directory.
  Download the dataset ZIP file from Google Drive link and extract it into the project directory.

Run Instructions
To run the application locally:

Launch the Streamlit Application:
  streamlit run app.py
Open the Application in Your Browser:
  Streamlit will automatically launch a browser tab. If not, navigate to the URL displayed in the terminal (usually http://localhost:8501).
Upload an Image:
  Use the "Upload an Image" section to select an image of a marine animal.
  View the predicted species and its conservation status on the application interface.

Project Introduction:
------
The primary objective of this project is to train a model that can identify marine animal species from a dataset of images and determine whether they belong to the endangered or extinct population. This system aims to assist wildlife researchers, photographers, and conservationists in quickly and efficiently identifying species and assessing their conservation status. By doing so, it seeks to support efforts in protecting and preserving endangered animals.

As humans, we share this planet with a diverse range of animals that have existed long before us, inhabiting every corner of the Earth. Unfortunately, many of these species are suffering due to human activities, including climate change, habitat destruction, and other environmental impacts. These issues threaten not only their survival but also the ecological balance of our planet.

It is our responsibility to take action in conserving these animals. This project is designed to aid in those efforts by providing an accessible and effective tool for identifying and supporting the protection of endangered species.

Contributors:
-----
Sarah Durrani 

Methods Used:
-----
1. Data Collection and Preprocessing:
Images were sourced from the Kaggle Marine Animal Dataset.
Preprocessing steps included resizing images to 224x224 pixels, normalization, and data augmentation (e.g., horizontal flips, rotations).
Data was split into training (80%) and testing (20%) sets to ensure robust model evaluation.
2. Model Development:
Transfer learning was applied using ResNet50 pre-trained on ImageNet for efficient feature extraction.
Custom dense layers were added to adapt the model for multi-class classification of marine species.
The model was trained for 10 epochs, using categorical cross-entropy loss and the Adam optimizer.
3. Integration of WWF Data:
A supplementary dataset from the WWF was integrated to map identified species to their conservation status.
Custom logic was added to classify species not present in the WWF dataset as "Not Endangered."
4. Interface Development:
A user-friendly interface was created using Streamlit, allowing users to upload images and view predictions with conservation status.
Feedback mechanisms were incorporated to improve usability and gather user input.
5. Evaluation and Deployment:
Model performance was evaluated using accuracy and loss metrics.
The system was deployed locally and via Streamlit for demonstration and user testing.


Technologies:
----

Programming Languages:
Python
Libraries and Frameworks:
TensorFlow/Keras (for model development and training)
OpenCV and PIL (for image preprocessing)
Matplotlib and Seaborn (for data visualization)
Pandas (for data handling and integration)
Streamlit (for developing the user interface)
Tools and Platforms:
Google Colab (for model training and testing)
Git/GitHub (for version control and collaboration)
Google Drive (for hosting large files like the dataset and trained model)
Pre-trained Models:
ResNet50 (used for transfer learning)

Project Description: 
--------
Endanger Detect is a computer vision-based system designed to identify marine animals from images and determine their conservation status. This project leverages transfer learning with ResNet50 and integrates data from the World Wildlife Fund (WWF) to classify species as "Endangered," "Vulnerable," or "Not Endangered." The system provides researchers, conservationists, and photographers with an accessible tool to prioritize protection efforts for at-risk species.

The project includes the following key components:

- Preprocessing of marine animal images to ensure consistency and improve model performance.
- Training a ResNet50-based deep learning model to classify species accurately.
- Integrating WWF conservation data to provide additional insights into the conservation status of identified species.
- Developing a Streamlit GUI for users to interact with the system by uploading images and receiving real-time predictions.
