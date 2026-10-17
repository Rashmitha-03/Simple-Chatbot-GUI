# Kasturba Hospital HelpDesk

A desktop help-desk chat interface built with Python and Tkinter. The app displays a welcome message and lets users enter messages in a simple chat window.

> **Project status:** This is a graphical interface prototype. Messages are displayed in the conversation window, but there is not yet a chatbot response engine or connection to hospital services.

## Features

- Tkinter desktop window with a chat transcript and scrollbar
- Message input with a submit button and Enter-key support
- Welcome text for the Kasturba Hospital HelpDesk
- Image assets for the header and submit button

## Requirements

- Python 3
- Tkinter (included with most standard Python installations)

On Linux, Tkinter may need to be installed through your distribution's package manager if it is not included with Python.

## Run Locally

1. Clone this repository and open its directory:

	```bash
	git clone <repository-url>
	cd <repository-directory>
	```

2. Run the application from the project directory so its image assets can be found:

	```bash
	python main.py
	```

On Windows, you can also use `py main.py` if `python` is not the Python launcher on your system.

## Project Structure

```text
.
├── main.py               # Tkinter application
├── chatbot2-icon.png     # Header logo
├── submit-button.png     # Submit button image
└── images.png            # Additional image asset
```

## Current Limitations

- Submitted messages are shown in the transcript, but the app does not generate replies.
- The interface does not send or store messages and is not connected to hospital systems.
- The window currently expects the image files to remain alongside `main.py`.
