# 🖥️ Command Line Pro with AI (Gemini Integration)

A modern desktop application built using **Python Tkinter** that provides a feature-rich command-line interface with **Google's Gemini AI** integration for intelligent, context-aware assistance.

---

## 🚀 Features

- 🔧 **Shell Command Execution**  
  Execute real shell commands directly from the GUI:
  - `cd` to change directory  
  - `clear` to reset the terminal  
  - Supports common shell commands like `ls`, `dir`, `pip list`, etc.

- 🤖 **AI Assistant (Gemini 1.5 Flash)**  
  Interact with Google's Gemini AI and get answers based on:
  - Your executed command history  
  - General coding or terminal-related questions

- 📜 **Command History Log**  
  Logs each command along with its output and error for Gemini context.

- 🧠 **Smart Chat UI**  
  A separate AI chat panel styled like a terminal with:
  - Bold response formatting  
  - Real-time scroll

---

## 🖼️ Screenshot

> Sample UI preview  
![image](https://github.com/user-attachments/assets/7db310d0-b0e6-40ef-88c0-67e9d2c21e34)


---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Pranay-Dommati/CommandLineAi.git
cd CommandLineAi
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install google-generativeai pillow
```

### 3. Set Up Gemini AI API Key

You have two options to set your Google API key:

#### Option 1: Environment Variable (Recommended for Production)

Set your Google API key as an environment variable.

**Linux/macOS:**

```bash
export GOOGLE_API_KEY='your_api_key'
```

**Windows (CMD):**

```cmd
set GOOGLE_API_KEY=your_api_key
```

**Windows (PowerShell):**

```powershell
$env:GOOGLE_API_KEY="your_api_key"
```

#### Option 2: .env File (Convenient for Development)

Create a `.env` file in the project root directory with the following content:

```
GOOGLE_API_KEY=your_api_key
```

The application will automatically check for the API key in both locations.

---

## 🧾 Usage

Run the app with:

```bash
python clproject.py
```

Run in CLI mode (no GUI):

```bash
python clproject.py --cli
```

### Terminal Actions:

- Type a command like `cd ..`, `dir`, `ls` and press **Enter**
- Use `clear` to reset the terminal output area

### Use AI Assistant:

- Click the **🤖 AI Assistant** button to toggle the AI panel
- Type your question in the AI input field (e.g., `Why did my last command fail?`)
- Press **Enter** or click **Send**
- Gemini responds with context-aware answers based on your command history

---

## 📁 Project Structure

```
├── clproject.py          # Main Python script 
├── logo.png              # Logo displayed on the right side of the UI
├── README.md             # This documentation file
├── requirements.txt      # List of Python dependencies
├── .env                  # Environment file for API key (not tracked in git)
├── .gitignore            # Git ignore file (ignores .env file)
```

---

## 📦 Requirements

- Python 3.7 or higher
- Internet connection (for Gemini AI)
- A valid [Google Generative AI Key](https://makersuite.google.com/app)

---

## 🔐 API Key Configuration

Before running the app, ensure you've set up your Google API key using one of these methods:

### Environment Variable (Recommended)

```bash
GOOGLE_API_KEY=your_google_generative_ai_key
```

### .env File Alternative

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_google_generative_ai_key
```

Note: The `.env` file is included in `.gitignore` to prevent accidentally committing your API key.

---

## ✨ Customization Tips

- 🖼️ Replace `logo.png` with your own branding
- 🎨 Modify fonts, colors, and layout in `main.py` to personalize UI
- 💬 Extend chatbot capability using Gemini Pro or image input (optional)

---

## 🤝 Contributing

Pull requests are welcome!  
For major changes, please open an issue first to discuss what you'd like to change.

---

## 👨‍💻 Author

**Pranay Dommati**  
GitHub: [@Pranay-Dommati](https://github.com/Pranay-Dommati)  
LinkedIn: [LinkedIn Profile](https://www.linkedin.com)

---
