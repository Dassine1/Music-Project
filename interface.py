import sys
from PyQt6.QtWidgets import QApplication, QWidget


# 1. Initialize the application handler
app = QApplication(sys.argv)

# 2. Create a basic widget which serves as the window
window = QWidget()
window.setWindowTitle("Music Maker")  # Set the window title
window.resize(300, 200)  # Width, Height in pixels

# 3. Render the window on screen
window.show()

#  après window.show()
window.grab().save("rendu_interface.png")  # Prend une photo de la fenêtre
print("📸 Capture d'écran enregistrée sous 'rendu_interface.png' !")

# 4. Run the main system event loop
sys.exit(app.exec())
