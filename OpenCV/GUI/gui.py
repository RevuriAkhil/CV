import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QGroupBox, QFormLayout
from PyQt5.QtGui import QFont, QColor, QPalette, QPainter, QBrush
from PyQt5.QtCore import Qt, QTimer
import random

class RelayTestBenchGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Relay & Contactor Test Bench")
        self.setGeometry(100, 100, 800, 600)

        # Set color scheme
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(0, 255, 255))  # Cyan background
        palette.setColor(QPalette.WindowText, Qt.white)  # White text
        palette.setColor(QPalette.Window, QColor(0, 0, 139))  # Dark blue heading
        self.setPalette(palette)

        # Create a main widget and set it as the central widget
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Create a vertical layout for the main widget
        layout = QVBoxLayout(main_widget)

        # Create the heading label
        heading_label = QLabel("Relay & Contactor Test Bench", self)
        heading_label.setFont(QFont("Arial", 16, QFont.Bold))
        layout.addWidget(heading_label)

        # Create a horizontal layout for the panels
        panels_layout = QHBoxLayout()

        # Create the Electropneumatic Contractor panel
        electropneumatic_panel = QGroupBox("Electropneumatic Contractor", self)
        electropneumatic_layout = QVBoxLayout(electropneumatic_panel)

        # Create the dynamic text fields for Electropneumatic Contractor
        field_names_electropneumatic = ["Pickup Voltage", "Drop Voltage", "Current", "Coil Resistance", "Pneumatic Pressure"]
        field_layout_electropneumatic = QFormLayout()
        for field_name in field_names_electropneumatic:
            field_label = QLabel(field_name + ":")
            field_value = QLabel("0")  # Initial value, will be updated dynamically
            field_layout_electropneumatic.addRow(field_label, field_value)
        electropneumatic_layout.addLayout(field_layout_electropneumatic)

        panels_layout.addWidget(electropneumatic_panel)

        # Create the Electro-magnetic Contractor panel
        electromagnetic_panel = QGroupBox("Electro-magnetic Contractor", self)
        electromagnetic_layout = QVBoxLayout(electromagnetic_panel)

        # Create the dynamic text fields for Electro-magnetic Contractor
        field_names_electromagnetic = ["Pickup Voltage", "Drop Voltage", "Current", "Coil Resistance", "No. of Operations", "Coil Temperature"]
        field_layout_electromagnetic = QFormLayout()
        for field_name in field_names_electromagnetic:
            field_label = QLabel(field_name + ":")
            field_value = QLabel("0")  # Initial value, will be updated dynamically
            field_layout_electromagnetic.addRow(field_label, field_value)
        electromagnetic_layout.addLayout(field_layout_electromagnetic)

        panels_layout.addWidget(electromagnetic_panel)

        # Create a copy of the Electro-magnetic Contractor panel
        electromagnetic_panel2 = QGroupBox("Electro-magnetic Contractor (Copy)", self)
        electromagnetic_layout2 = QVBoxLayout(electromagnetic_panel2)

        # Create the dynamic text fields for the copied Electro-magnetic Contractor
        field_layout_electromagnetic2 = QFormLayout()
        for field_name in field_names_electromagnetic:
            field_label = QLabel(field_name + ":")
            field_value = QLabel("0")  # Initial value, will be updated dynamically
            field_layout_electromagnetic2.addRow(field_label, field_value)
        electromagnetic_layout2.addLayout(field_layout_electromagnetic2)

        panels_layout.addWidget(electromagnetic_panel2)

        layout.addLayout(panels_layout)

        # Create the circles for healthy and bad indications with labels
        circle_layout = QVBoxLayout()
        healthy_layout = QHBoxLayout()
        healthy_label = QLabel("Healthy", self)
        healthy_label.setAlignment(Qt.AlignCenter)
        healthy_indicator = CircleWidget(QColor(0, 255, 0))  # Green color for healthy
        healthy_layout.addWidget(healthy_indicator)
        healthy_layout.addWidget(healthy_label)

        bad_layout = QHBoxLayout()
        bad_label = QLabel("Bad", self)
        bad_label.setAlignment(Qt.AlignCenter)
        bad_indicator = CircleWidget(QColor(255, 0, 0))  # Red color for bad
        bad_layout.addWidget(bad_indicator)
        bad_layout.addWidget(bad_label)

        circle_layout.addLayout(healthy_layout)
        circle_layout.addLayout(bad_layout)
        electromagnetic_layout.addLayout(circle_layout)
        electromagnetic_layout2.addLayout(circle_layout)

        # Update the dynamic text fields with random values (for demonstration)
        self.update_dynamic_fields()

    def update_dynamic_fields(self):
        # Update the dynamic text fields with random values (for demonstration)
        field_names_electropneumatic = ["Pickup Voltage", "Drop Voltage", "Current", "Coil Resistance", "Pneumatic Pressure"]
        for field_name in field_names_electropneumatic:
            field_value = str(random.uniform(0, 10))  # Random value between 0 and 10
            field_widget = self.findChild(QLabel, field_name)
            if field_widget:
                field_widget.setText(field_name + ": " + field_value)

        field_names_electromagnetic = ["Pickup Voltage", "Drop Voltage", "Current", "Coil Resistance", "No. of Operations", "Coil Temperature"]
        for field_name in field_names_electromagnetic:
            field_value = str(random.uniform(0, 10))  # Random value between 0 and 10
            field_widget = self.findChild(QLabel, field_name)
            if field_widget:
                field_widget.setText(field_name + ": " + field_value)

        # Call this method again after a certain interval to update the fields dynamically
        QTimer.singleShot(1000, self.update_dynamic_fields)


class CircleWidget(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setMinimumSize(60, 60)
        self.color = color

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(self.color))
        painter.drawEllipse(10, 10, 40, 40)


# Create the PyQt5 application
app = QApplication(sys.argv)

# Create the GUI window
window = RelayTestBenchGUI()

# Show the window
window.show()

# Start the event loop
sys.exit(app.exec())

