# 🖥️ Command Line Assistant with AI (Gemini Integration)

A desktop application built using **Python Tkinter** that simulates a command-line interface and integrates **Google's Gemini AI** for intelligent, context-aware responses.

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

- 🖼️ **Branding Support**  
  Add your own logo via `logo.png` on the right-hand side of the app.

---

## 🖼️ Screenshot

> Sample UI preview  
> *(Replace this with an actual screenshot)*

//img

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/command-line-assistant-ai.git
cd command-line-assistant-ai
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

Set your Gemini API key as an environment variable.

**Linux/macOS:**

```bash
export GEMINIAI_API_KEY='your_api_key'
```

**Windows (CMD):**

```cmd
set GEMINIAI_API_KEY=your_api_key
```

---

## 🧾 Usage

Run the app with:

```bash
python main.py
```

### Terminal Actions:

- Type a command like `cd ..`, `dir`, `ls` and press **Enter**
- Use `clear` to reset the terminal output area

### Ask Gemini:

- Type your question in the AI input field (e.g., `Why did my last command fail?`)
- Press **Enter** or click **Ask AI**
- Gemini responds with context-aware answers based on your full command history

---

## 📁 Project Structure

```
├── main.py               # Main Python script
├── logo.png              # Logo displayed on the right side of the UI
├── README.md             # This documentation file
├── requirements.txt      # List of Python dependencies
```

---

## 📦 Requirements

- Python 3.7 or higher
- Internet connection (for Gemini AI)
- A valid [Google Generative AI Key](https://makersuite.google.com/app)

---

## 🔐 Environment Variable

Before running the app, ensure this environment variable is set:

```bash
GEMINIAI_API_KEY=your_google_generative_ai_key
```

---

## ✨ Customization Tips

- 🖼️ Replace `logo.png` with your own branding
- 🎨 Modify fonts, colors, and layout in `main.py` to personalize UI
- 💬 Extend chatbot capability using Gemini Pro or image input (optional)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

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
