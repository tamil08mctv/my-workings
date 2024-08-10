import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QVideoWidget
from PyQt6.QtCore import Qt, QUrl

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6 Video Background with Title")
        self.setGeometry(100, 100, 800, 600)

        # Create a video widget
        self.video_widget = QVideoWidget()

        # Create a media player object
        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.setSource(QUrl.fromLocalFile("Siva\\12.mp4"))

        # Create a title label
        self.title_label = QLabel("Your Title Here")
        self.title_label.setStyleSheet("font-size: 24px; color: white; background: transparent;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create a central widget and layout
        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.video_widget)
        self.layout.addWidget(self.title_label)
        self.central_widget.setLayout(self.layout)

        # Set the central widget
        self.setCentralWidget(self.central_widget)

        # Play the video
        self.media_player.play()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
