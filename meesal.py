import streamlit as st
import easyocr
from PIL import Image
import numpy as np


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="OCR Text Extractor",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* ========================================================
       MAIN PAGE
       ======================================================== */

    .stApp {
        background: linear-gradient(
            135deg,
            #f8fafc 0%,
            #eef2ff 50%,
            #f8fafc 100%
        );
    }

    .main .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }


    /* ========================================================
       HEADINGS
       ======================================================== */

    h1 {
        text-align: center;
        font-size: 42px !important;
        font-weight: 800 !important;
        letter-spacing: -1px;
        margin-bottom: 5px !important;
    }

    h2 {
        font-weight: 750 !important;
    }

    h3 {
        font-weight: 700 !important;
    }


    /* ========================================================
       HEADER BANNER
       ======================================================== */

    [data-testid="stMarkdownContainer"] h1:first-child {
        padding: 25px 20px;
        border-radius: 20px;
        background: linear-gradient(
            135deg,
            #4f46e5,
            #7c3aed,
            #9333ea
        );
        color: white;
        box-shadow: 0 12px 30px rgba(79, 70, 229, 0.25);
        margin-bottom: 10px !important;
    }


    /* ========================================================
       FILE UPLOADER
       ======================================================== */

    [data-testid="stFileUploader"] {
        background: white;
        padding: 20px;
        border-radius: 18px;
        border: 2px dashed #6366f1;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.06);
        margin-top: 15px;
        margin-bottom: 20px;
    }

    [data-testid="stFileUploaderDropzone"] {
        border: none !important;
        background: transparent !important;
    }


    /* ========================================================
       BUTTON
       ======================================================== */

    .stButton > button {
        width: 100%;
        height: 52px;
        border-radius: 12px;
        border: none;
        font-size: 17px;
        font-weight: 700;
        background: linear-gradient(
            135deg,
            #4f46e5,
            #7c3aed
        );
        color: white;
        box-shadow: 0 8px 20px rgba(79, 70, 229, 0.25);
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 25px rgba(79, 70, 229, 0.35);
    }


    /* ========================================================
       IMAGE
       ======================================================== */

    [data-testid="stImage"] {
        border-radius: 15px;
        overflow: hidden;
    }


    /* ========================================================
       TEXT AREA
       ======================================================== */

    textarea {
        border-radius: 12px !important;
        border: 1px solid #c7d2fe !important;
        font-size: 15px !important;
        line-height: 1.6 !important;
    }


    /* ========================================================
       DOWNLOAD BUTTON
       ======================================================== */

    .stDownloadButton > button {
        width: 100%;
        height: 45px;
        border-radius: 10px;
        font-weight: 600;
    }


    /* ========================================================
       ALERTS
       ======================================================== */

    [data-testid="stAlert"] {
        border-radius: 12px;
    }


    /* ========================================================
       DIVIDER
       ======================================================== */

    hr {
        margin-top: 30px;
        margin-bottom: 30px;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    footer {
        visibility: hidden;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.title("📄 OCR Text Extractor")

st.markdown(
    """
    ### 🧠 Convert Image Text into Machine-Readable Text

    Upload an image and use **EasyOCR** to automatically
    detect and extract the text.
    """
)

st.divider()


# ============================================================
# OCR MODEL
# ============================================================

@st.cache_resource
def load_ocr_reader():

    return easyocr.Reader(
        ["en"],
        gpu=False
    )


# ============================================================
# IMAGE UPLOAD SECTION
# ============================================================

st.subheader("📤 Upload Your Image")

uploaded_file = st.file_uploader(
    "Choose an image containing text",
    type=["png", "jpg", "jpeg"],
    help="Supported formats: PNG, JPG and JPEG"
)


# ============================================================
# MAIN OCR SECTION
# ============================================================

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.success("✅ Image uploaded successfully!")

    st.divider()

    col1, col2 = st.columns(
        2,
        gap="large"
    )


    # ========================================================
    # LEFT COLUMN
    # ========================================================

    with col1:

        st.subheader("🖼️ Input Image")

        st.image(
            image,
            caption="Uploaded Image",
            width="stretch"
        )


    # ========================================================
    # RIGHT COLUMN
    # ========================================================

    with col2:

        st.subheader("📝 Extracted Text")

        extract_button = st.button(
            "🔍 Extract Text",
            use_container_width=True
        )

        if extract_button:

            with st.spinner(
                "🤖 EasyOCR is analyzing your image..."
            ):

                try:

                    # Load OCR model
                    reader = load_ocr_reader()

                    # Convert PIL image to NumPy
                    image_array = np.array(image)

                    # Run OCR
                    results = reader.readtext(
                        image_array
                    )

                    # Extract recognized text
                    extracted_text = "\n".join(
                        result[1]
                        for result in results
                    )


                    # ====================================================
                    # OCR RESULT
                    # ====================================================

                    if extracted_text.strip():

                        st.success(
                            "✅ Text extracted successfully!"
                        )

                        st.text_area(
                            "📋 OCR Result",
                            extracted_text,
                            height=350
                        )


                        # ====================================================
                        # DOWNLOAD
                        # ====================================================

                        st.download_button(
                            label="📥 Download Extracted Text",
                            data=extracted_text,
                            file_name="ocr_result.txt",
                            mime="text/plain",
                            use_container_width=True
                        )


                    else:

                        st.warning(
                            "⚠️ No readable text was detected "
                            "in this image."
                        )


                except Exception as e:

                    st.error(
                        f"❌ OCR Error: {e}"
                    )


# ============================================================
# BEFORE IMAGE UPLOAD
# ============================================================

else:

    st.divider()

    st.subheader("🚀 How It Works")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("### 📤 1. Upload")

        st.write(
            "Upload a PNG, JPG or JPEG image "
            "containing text."
        )


    with col2:

        st.markdown("### 🔍 2. Extract")

        st.write(
            "Click the Extract Text button "
            "to analyze your image."
        )


    with col3:

        st.markdown("### 📋 3. Get Text")

        st.write(
            "View the detected text and "
            "download it as a TXT file."
        )


# ============================================================
# FEATURES
# ============================================================

st.divider()

st.subheader("✨ OCR Features")

feature_col1, feature_col2, feature_col3, feature_col4 = st.columns(4)

with feature_col1:

    st.markdown("### 🖼️ Image OCR")

    st.caption(
        "Extract text directly from images."
    )


with feature_col2:

    st.markdown("### 🤖 EasyOCR")

    st.caption(
        "AI-powered optical character recognition."
    )


with feature_col3:

    st.markdown("### 📋 Editable Text")

    st.caption(
        "View and copy the extracted text."
    )


with feature_col4:

    st.markdown("### 📥 Download")

    st.caption(
        "Save the OCR result as a text file."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "📄 OCR Text Extractor  •  Powered by EasyOCR  •  Computer Vision Project"
)

