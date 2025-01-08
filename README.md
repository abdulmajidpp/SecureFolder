# Tkinter User Login System with SQLite

This project is a simple login system built using **Tkinter** for the user interface and **SQLite** for storing user credentials. The system allows users to register, login, and access a secure folder once authenticated.

## Features

- **Login System**: Users can log in with their username and password.
- **User Registration**: New users can create an account with a matching password confirmation.
- **Secure Folder**: On successful login, users can open a secure folder.
- **SQLite Database**: User credentials are stored in an SQLite database for persistent storage.
- **User Logs**: User logins are recorded in a log file (`login.txt`).
- **User Feedback**: The system provides appropriate feedback via message boxes on success or failure.

## Installation

### Prerequisites

Make sure you have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/).

### Install Dependencies

To run this project, you need the following Python libraries:

- `tkinter` (for the GUI)
- `sqlite3` (for database handling)

You can install any missing dependencies using `pip`. Here’s the command to install them:

```bash
pip install -r requirements.txt
