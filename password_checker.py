import sys
import string
import re
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QMessageBox
from PyQt5.QtGui import QFont

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Complexity Checks
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add lowercase letters for better security.")
    
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Include uppercase letters to strengthen your password.")
    
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Use numbers to make your password stronger.")
    
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Special characters (!@#$%^&*) improve security.")
    
    # Common Pattern Check
    common_patterns = ["123456", "password", "qwerty", "abc123", "letmein"]
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 2
        feedback.append("Avoid common words or sequences like 'password' or '123456'.")
    
    # Strength Rating
    if score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    return strength, feedback

class PasswordChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Password Strength Checker")
        self.setGeometry(100, 100, 400, 200)
        
        layout = QVBoxLayout()
        
        self.label = QLabel("Enter your password:")
        self.label.setFont(QFont("Arial", 12))
        layout.addWidget(self.label)
        
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)
        
        self.check_button = QPushButton("Check Strength")
        self.check_button.clicked.connect(self.check_strength)
        layout.addWidget(self.check_button)
        
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)
        
        self.setLayout(layout)
    
    def check_strength(self):
        password = self.password_input.text()
        if not password:
            QMessageBox.warning(self, "Input Error", "Please enter a password.")
            return
        
        strength, feedback = check_password_strength(password)
        feedback_text = "\n".join(feedback)
        self.result_label.setText(f"Strength: {strength}\n{feedback_text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordChecker()
    window.show()
    sys.exit(app.exec_())
