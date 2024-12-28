# tests/test_face_detection.py

import unittest
import cv2

class TestFaceDetection(unittest.TestCase):

    def test_haarcascade_exists(self):
        """
        Test to ensure the Haar Cascade file exists.
        """
        face_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        self.assertTrue(cv2.CascadeClassifier(face_cascade_path).empty() is False)

if __name__ == '__main__':
    unittest.main()
