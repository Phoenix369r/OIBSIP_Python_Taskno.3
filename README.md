# Advanced Password Generator

A secure and user-friendly password generator built with Python and Tkinter that creates customizable passwords with various character sets and automatically copies them to your clipboard.

## 🎯 Objective

Create a robust desktop application that generates cryptographically secure passwords with customizable options, providing users with a simple interface to create strong passwords for their security needs.

## ✨ Features

- **Customizable Length**: Generate passwords between 8-64 characters
- **Character Set Options**: Choose from uppercase letters, lowercase letters, digits, and symbols
- **Guaranteed Inclusion**: Ensures at least one character from each selected character set
- **Cryptographically Secure**: Uses Python's `secrets` module for secure random generation
- **One-Click Copy**: Copy generated passwords directly to clipboard
- **Visual Interface**: Clean GUI with logo support and intuitive controls
- **Input Validation**: Prevents invalid inputs and provides user feedback

## 🛠️ Tools & Technologies Used

- **Python 3.x** - Core programming language
- **Tkinter** - GUI framework for the desktop interface
- **PIL (Pillow)** - Image processing for logo display
- **pyperclip** - Clipboard functionality
- **secrets** - Cryptographically secure random number generation
- **string** - Character set definitions

## 📋 Requirements

```txt
pillow>=9.0.0
pyperclip>=1.8.0
```

## 🚀 Installation & Setup

1. **Clone or download** the project files
2. **Install dependencies**:
   ```bash
   pip install pillow pyperclip
   ```
3. **Add logo image** (optional): Place a `logo.png` file in the same directory
4. **Run the application**:
   ```bash
   python password_generator.py
   ```

## 💻 How to Use

1. **Set Password Length**: Enter desired length (8-64 characters)
2. **Select Character Types**: Check/uncheck options for:
   - Uppercase letters (A-Z)
   - Lowercase letters (a-z)
   - Digits (0-9)
   - Symbols (!@#$%^&* etc.)
3. **Generate**: Click "Generate Password" button
4. **Copy**: Click "Copy to Clipboard" to copy the password

## 🔧 Steps Performed

1. **Password Generation Logic**:
   - Validates user input for length constraints
   - Builds character pool based on selected options
   - Guarantees inclusion of at least one character from each selected set
   - Uses cryptographically secure random generation
   - Shuffles final password for additional randomization

2. **User Interface Development**:
   - Created responsive GUI layout with Tkinter
   - Implemented image loading and resizing functionality
   - Added input validation and error handling
   - Integrated clipboard functionality

3. **Security Implementation**:
   - Used `secrets` module instead of `random` for cryptographic security
   - Implemented character set validation
   - Added password strength enforcement

## 📊 Outcome

- ✅ **Secure Password Generation**: Creates cryptographically strong passwords
- ✅ **User-Friendly Interface**: Intuitive GUI suitable for all users
- ✅ **Customizable Options**: Flexible character set selection
- ✅ **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux
- ✅ **Clipboard Integration**: Seamless password copying functionality
- ✅ **Input Validation**: Prevents errors and guides user input
- ✅ **Visual Appeal**: Clean design with logo support

## 🔒 Security Features

- Uses `secrets.SystemRandom()` for cryptographically secure randomization
- Guarantees character diversity in generated passwords
- No password storage or logging
- Immediate clipboard integration for secure handling

