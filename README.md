# What Did I Miss? 📱🔍

> A fast, private, local-first web app to parse, view, and inspect real exported WhatsApp chat files (`.txt`). Built with **React + Vite** and **Python FastAPI**.

---

## Key Features (Milestone 1)

- 🔒 **100% Local & Private**: All file processing happens locally in-memory on your machine. Chat files are never sent to external AI services or uploaded to any third-party cloud.
- 📂 **Direct WhatsApp Upload**: Drag and drop or browse for an exported `.txt` chat file.
- ⚡ **Multi-Format WhatsApp Parser**:
  - **Android format**: `DD/MM/YYYY, HH:MM [am/pm] - Sender: Message` (12-hour and 24-hour)
  - **iOS format**: `[DD/MM/YYYY, HH:MM:SS AM] Sender: Message`
  - **Multiline Messages**: Multi-line messages are preserved and formatted intact.
  - **System Notices**: Automatically identifies group events, encryption alerts, and admin actions.
  - **Unicode & BOM Normalization**: Strips invisible LTR marks (`\u200e`), narrow non-breaking spaces, and BOM characters.
- 🎨 **Modern WhatsApp-Inspired Viewer**:
  - Live search across message text, senders, and timestamps.
  - Filter by participant dropdown.
  - Toggle system notices on or off.
  - Distinct sender badge colors and readable chat bubbles.
- 🚫 **No Mock Data**: Real chats only. Displays an empty upload screen on first launch and only populates messages from your real uploaded `.txt` file.
- ⚠️ **Clear Error Handling**: Actionable error messages and tips when encountering non-txt files, empty files, or corrupted formats.

---

## Directory Structure

```
what-did-i-miss/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI app, CORS, /api/parse-chat
│   │   ├── models.py            # Pydantic data schemas
│   │   └── parser.py            # WhatsApp regex & multiline parsing engine
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_parser.py       # Unit tests for parser formats
│   │   └── test_api.py          # Integration tests for upload endpoints
│   ├── requirements.txt         # FastAPI, Uvicorn, python-multipart, pytest
│   └── run_backend.bat          # 1-click backend launcher for Windows
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── FileUpload.jsx   # Drag-and-drop file upload & export guide
│   │   │   ├── ChatStats.jsx    # Top statistics ribbon
│   │   │   ├── ChatViewer.jsx   # Interactive message stream & filters
│   │   │   └── ErrorAlert.jsx   # Friendly error notification banner
│   │   ├── App.jsx              # Main application view & state
│   │   ├── App.css              # Styling
│   │   └── main.jsx             # React entry point
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── run_frontend.bat         # 1-click frontend launcher for Windows
└── README.md
```

---

## Prerequisites for Windows

1. **Python 3.10 or higher** (Python 3.12 is already detected on your system).
2. **Node.js (LTS version)**:
   - If you do not have Node.js installed, open PowerShell or Command Prompt and run:
     ```powershell
     winget install OpenJS.NodeJS.LTS
     ```
   - Or download and run the installer from: **https://nodejs.org/** (LTS version recommended).
   - After installing, close and re-open your terminal.

---

## Quick Start on Windows (1-Click Batch Files)

We have provided convenient `.bat` scripts inside both the backend and frontend folders:

### 1. Start the Backend
Double-click `backend\run_backend.bat`, or in terminal:
```powershell
cd d:\studies\what-did-i-miss\backend
.\run_backend.bat
```
This automatically verifies dependencies and starts the FastAPI server at:
**http://127.0.0.1:8000** (Interactive docs at **http://127.0.0.1:8000/docs**).

### 2. Start the Frontend
In a new terminal window, double-click `frontend\run_frontend.bat`, or in terminal:
```powershell
cd d:\studies\what-did-i-miss\frontend
.\run_frontend.bat
```
This will run `npm install` (first time only) and start the Vite development server at:
**http://localhost:5173**

---

## Manual Step-by-Step Setup

If you prefer running commands manually:

### Backend Setup (Terminal 1)
```powershell
# Navigate to the backend folder
cd d:\studies\what-did-i-miss\backend

# Install required Python packages
python -m pip install -r requirements.txt

# Run the test suite to verify everything works
python -m pytest tests/ -v

# Start the development server
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

### Frontend Setup (Terminal 2)
```powershell
# Navigate to the frontend folder
cd d:\studies\what-did-i-miss\frontend

# Install dependencies (only required the first time)
npm install

# Start Vite dev server
npm run dev
```

Open your browser to: **http://localhost:5173**

---

## How to Export a Real WhatsApp Chat (.txt)

1. Open WhatsApp on your Android or iPhone device.
2. Open the conversation or group chat you wish to view.
3. Tap the **three dots menu (⋮)** or the group name at the top.
4. Tap **More** > **Export chat**.
5. Select **Without Media** (this generates a lightweight `.txt` file containing the chat transcript).
6. Send or transfer the `.txt` file to your PC.
7. Open **http://localhost:5173** and drag & drop the `.txt` file onto the upload area.

---

## Privacy & Security Verification

- **Local Processing**: Uploaded files are streamed in-memory to the local Python FastAPI process (`http://127.0.0.1:8000`).
- **No External AI APIs**: There are no OpenAI, Gemini, Anthropic, or external API calls configured in this milestone.
- **No Cloud Database**: Chats exist only in the browser's active tab state and are discarded upon closing or resetting the page.
