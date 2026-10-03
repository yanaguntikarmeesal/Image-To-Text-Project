# 📄 OCR Text Extractor using EasyOCR



**Developed by:** **Yanaguntikar Meesal**


**📧 Email:** **[yanaguntikarm@gmail.com](mailto:yanaguntikarm@gmail.com)**


**🌐 Live Project:** [OCR Text Extractor using EasyOCR](https://image-to-text-project-myvsw3tfqgsxxgzquzrczl.streamlit.app/)






## 📝 Project Overview

**OCR Text Extractor** is a computer vision project built using Python, Streamlit, and EasyOCR. It extracts machine-readable text from images using Optical Character Recognition (OCR).

The application provides a simple, interactive webpage where users can upload an image, extract text, view the results, and download the extracted text as a `.txt` file.

## ✨ Features

* 📤 Upload images in PNG, JPG, and JPEG formats.
* 🖼️ Preview the uploaded image.
* 🤖 Extract text using EasyOCR.
* 📝 Display extracted text in an editable text area.
* 📥 Download extracted text as a TXT file.
* 🎨 Professional Streamlit interface with custom CSS.
* ⚡ Cache the OCR reader for reuse.
* 💻 Simple and user-friendly interface.

## 🛠️ Technologies Used

| Technology   | Purpose                               |
| ------------ | ------------------------------------- |
| Python       | Programming language                  |
| Streamlit    | Web application framework             |
| EasyOCR      | Text recognition from images          |
| Pillow (PIL) | Image loading and processing          |
| NumPy        | Image conversion and array processing |

## 📂 Project Structure

```text
OCR-Text-Extractor/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/OCR-Text-Extractor.git
```

### 2. Navigate to the project folder

```bash
cd OCR-Text-Extractor
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📦 Requirements

Create a `requirements.txt` file with:

```text
streamlit
easyocr
Pillow
numpy
opencv-python-headless
```

## 🚀 How to Use

1. Open the OCR Text Extractor webpage.
2. Upload an image containing text.
3. Preview the uploaded image.
4. Click **Extract Text**.
5. View the recognized text in the result area.
6. Download the extracted text as a `.txt` file.

## 🧠 How OCR Works

The application follows this workflow:

```text
Input Image
    ↓
Image Upload
    ↓
PIL Image Conversion
    ↓
NumPy Array
    ↓
EasyOCR Text Recognition
    ↓
Extracted Text
    ↓
Display and Download
```

## 📌 Applications

* 📄 Extract text from scanned documents.
* 📚 Convert printed text from books into editable text.
* 🧾 Read text from invoices and receipts.
* 📷 Extract text from screenshots and photographs.
* 🏢 Digitize printed documents.

## ⚠️ Notes

* EasyOCR downloads its required model files during the first initialization.
* The application currently uses the English OCR model.
* OCR accuracy depends on image quality, text clarity, and image resolution.
* The first OCR run may take longer while the model is being initialized.
* A working Python environment with compatible PyTorch and EasyOCR dependencies is required.

## 🔮 Future Improvements

* Support for multiple languages.
* OCR support for PDF documents.
* Extract text from multiple images at once.
* Add image preprocessing and enhancement.
* Export results to PDF, Word, or Excel.
* Add OCR confidence scores and text detection visualization.

## 👨‍💻 Author

**Yanaguntikar Meesal**

## 📜 License

This project is available for educational and personal learning purposes. Add a suitable open-source license if you plan to distribute it publicly.

---

⭐ If you find this project useful, consider giving the repository a star!
