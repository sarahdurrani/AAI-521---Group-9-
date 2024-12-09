import streamlit as st
st.title("Hello, Streamlit!")


import pandas as pd
from PIL import Image
import os

# Load WWF data
@st.cache_data
def load_wwf_data(csv_path):
    """
    Load and preprocess WWF dataset.
    """
    wwf_data = pd.read_csv(csv_path)
    wwf_data['COMMON NAME'] = wwf_data['COMMON NAME'].str.lower().str.strip()
    wwf_data = wwf_data.drop_duplicates(subset='COMMON NAME')
    return wwf_data

# Get conservation status
def get_conservation_status(species, wwf_data):
    """
    Return the conservation status of a species from the WWF dataset.
    """
    status = wwf_data[wwf_data['COMMON NAME'] == species.lower().strip()]['CONSERVATION STATUS'].values
    return status[0] if len(status) > 0 else "Unknown"

# Main Streamlit app
def main():
    st.title("Endangered Marine Animal Detector")
    st.write("Upload an image of a marine animal to identify it and check its conservation status.")

    # Load WWF dataset
    wwf_csv_path = "WWF list of endangered marine animals  - Sheet1.csv"
    if not os.path.exists(wwf_csv_path):
        st.error(f"WWF dataset not found at: {wwf_csv_path}")
        return
    wwf_data = load_wwf_data(wwf_csv_path)

    # Upload image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Mock prediction (replace with your model's prediction)
        mock_predictions = {
            "leatherback turtle": "Endangered",
            "blue whale": "Endangered",
            "great white shark": "Vulnerable",
        }

        # Get species name from user (for now)
        species_name = st.text_input("Enter the predicted species name:")
        if st.button("Check Conservation Status"):
            if species_name:
                # Get conservation status from WWF data
                status = get_conservation_status(species_name, wwf_data)
                st.success(f"The species '{species_name}' is classified as: {status}")
            else:
                st.warning("Please enter a species name.")

# Run the app
if __name__ == "__main__":
    main()



    


import streamlit as st
import pandas as pd
from PIL import Image
import os

# Load WWF data
@st.cache_data
def load_wwf_data(csv_path):
    """
    Load and preprocess WWF dataset.
    """
    wwf_data = pd.read_csv(csv_path)
    wwf_data['COMMON NAME'] = wwf_data['COMMON NAME'].str.lower().str.strip()
    wwf_data = wwf_data.drop_duplicates(subset='COMMON NAME')
    return wwf_data

# Get conservation status
def get_conservation_status(species, wwf_data):
    """
    Return the conservation status of a species from the WWF dataset.
    """
    status = wwf_data[wwf_data['COMMON NAME'] == species.lower().strip()]['CONSERVATION STATUS'].values
    return status[0] if len(status) > 0 else "Unknown"

# Main Streamlit app
def main():
    st.title("Endangered Marine Animal Detector")
    st.write("Upload an image of a marine animal to identify it and check its conservation status.")

    # Load WWF dataset
    wwf_csv_path = "WWF list of endangered marine animals  - Sheet1.csv"
    if not os.path.exists(wwf_csv_path):
        st.error(f"WWF dataset not found at: {wwf_csv_path}")
        return
    wwf_data = load_wwf_data(wwf_csv_path)

    # Upload image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Mock prediction (replace with your model's prediction)
        mock_predictions = {
            "leatherback turtle": "Endangered",
            "blue whale": "Endangered",
            "great white shark": "Vulnerable",
        }

        # Get species name from user (for now)
        species_name = st.text_input("Enter the predicted species name:")
        if st.button("Check Conservation Status"):
            if species_name:
                # Get conservation status from WWF data
                status = get_conservation_status(species_name, wwf_data)
                st.success(f"The species '{species_name}' is classified as: {status}")
            else:
                st.warning("Please enter a species name.")

# Run the app
if __name__ == "__main__":
    main()
