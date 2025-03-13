import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="Crop Yield Prediction",page_icon='<')


# Function to set background image
def set_bg(image_file):
    with open(image_file, "rb") as img:
        encoded_string = base64.b64encode(img.read()).decode()
    bg_image = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded_string}");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }}

    /* Title Styling Fix */
    .title-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 50vh;
    }}
    .title-text {{
        font-size: 100px !important; /* Force size */
        font-weight: bold;
        color: #FFD700  !important; /* Change to gold */
        text-shadow: 10px 10px 15px black !important;
        text-align: center;
        display: block;
    }}

    /* Sidebar - Glassmorphism */
    section[data-testid="stSidebar"] {{
        background: rgba(255, 255, 255, 0.3); /* Semi-transparent white */
        backdrop-filter: blur(10px); /* Blur effect */
        border-radius: 15px;
        padding: 20px;
        color: white !important; 
    }}

    /* Sidebar Toggle Button Fix */
    [data-testid="collapsedControl"] {{
        color: white !important;
        visibility: visible !important;
        width: 30px !important; /* Increase size */
        height: 30px !important; /* Increase size */
        filter: drop-shadow(2px 2px 4px rgba(255, 255, 255, 0.8));
    }}

    /* Button - Glassmorphism */
    .button-container {{
        display: flex;
        justify-content: center;
        margin-top: 50px;
    }}

    .title-wrapper {{
    display: flex;
    flex-direction: column;
    align-items: center; /* Center horizontally */
    text-align: center;
    }}

    .subtitle-text {{
    font-size: 30px !important;
    font-weight: lighter;
    color: #ffffff !important;  /* White text */
    text-shadow: 5px 5px 10px black !important;
    text-align: center;
    margin-top: -20px;
    }}

    .proceed-button {{
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(8px);
        color: white;
        font-size: 26px;
        padding: 18px 35px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 12px;
        cursor: pointer;
        box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.3);
        transition: 0.3s;
        text-decoration: none;
    }}
    .proceed-button:hover {{
        background-color: rgba(255, 255, 255, 0.3);
        transform: scale(1.08);
    }}

    /* Hide Streamlit menu, footer, and deploy panel */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    </style>
    """
    st.markdown(bg_image, unsafe_allow_html=True)

# Call function to set background
set_bg("crop3.avif")  # Ensure this image exists in your directory

# Sidebar with "ℹ️ About" section
with st.sidebar:
    st.markdown(
        """
        <div class="stSidebar">
            <h2>About</h2>
            <p>This system predicts crop yield based on input factors like rainfall, temperature, soil type, and more.
              By analyzing factors like weather, soil conditions, and past harvests, it enables better planning, efficient resource use, and improved food security.
              Accurate predictions help reduce losses, optimize irrigation and fertilization, and adapt to changing climate conditions. With data-driven insights, farmers can maximize productivity while ensuring sustainability.
              </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Centered Title in the Middle
st.markdown(
    """
    <div class='title-container'>
       <div class='title-wrapper'>
           <h1 class='title-text'> CROP YIELD PREDICTION </h1>
           <h3 class='subtitle-text'>Enhancing Crop Forecasting with Machine Learning</h3>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


        

