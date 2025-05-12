#README 

# 🧹 Desktop File Organizer

A cross-platform Python script to automatically organize and declutter your desktop by categorizing files into folders based on file type.

## 📦 Features

- Automatically organizes files into categories like **Images**, **Documents**, **Videos**, etc.
- Creates folders if they don't exist
- Handles unsupported file types by placing them in an **"Others"** folder
- Easy to run and lightweight
- Uses built-in Python modules (`os`, `shutil`)

## 🔧 How It Works

1. Scans the desktop for all files.
2. Sorts them based on their file extensions.
3. Moves each file into its corresponding folder:
   - 📷 Images: `.jpg`, `.png`, etc.
   - 📄 Documents: `.pdf`, `.docx`, etc.
   - 🎥 Videos: `.mp4`, `.avi`, etc.
   - 🎵 Music: `.mp3`, `.wav`, etc.
   - 📦 Archives: `.zip`, `.rar`, etc.
   - 💻 Programs: `.exe`, `.py`, etc.
   - 📁 Others: everything else

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your machine

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/desktop-file-organizer.git
   cd desktop-file-organizer
