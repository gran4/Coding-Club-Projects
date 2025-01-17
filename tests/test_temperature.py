import unittest
from unittest.mock import MagicMock
import cv2
import numpy as np

from monitor.temperature import TemperatureMonitor


def create_mock_notifier():
    notifier = MagicMock()
    notifier.client.return_value = None
    notifier.admin_phone_numbers = []

    return notifier

def create_mock_camera(success: bool = True):
    camera = MagicMock()
    image = load_image()
    camera.capture_image.return_value = (success, image)

def create_mock_cameras():
    cameras = []
    camera = create_mock_camera()
    cameras.append(camera)

    camera2 = create_mock_camera()
    cameras.append(camera2)
    return cameras


def create_mock_cameras():
    return []

# Create mock objects
mock_notifier = create_mock_notifier()
mock_cameras = create_mock_cameras()

# Instantiate the TemperatureMonitor with mock objects
monitor = TemperatureMonitor(mock_cameras, mock_notifier)

def load_image():
    image_path = 'tests/test_image.png'  # Replace with your image file path
    image = cv2.imread(image_path)
    return image

def test_camera():
    image = monitor.capture_image()

    assert isinstance(image, np.ndarray)

def test_process_image():
    image = load_image()
    temperature = monitor.process_image(image)
    assert temperature == 70

def test_monitor_cycle():
    pass


if __name__ == '__main__':
    unittest.main()
