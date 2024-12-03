import unittest
import numpy as np
from unittest.mock import patch
from classes_and_methods import RGB, YCbCr, resize_image, bw_image, serpentine, run_lenght_encoding, DCT, DWT

class TestColorConversion(unittest.TestCase):

    @patch('builtins.input', side_effect=['100', '150', '200'])
    def test_RGB_to_YCbCr(self, mock_input):
        # Expected values calculated based on the RGB to YCbCr conversion formula
        expected_Y = 0.257*100 + 0.504*150 + 0.098*200 + 16
        expected_Cb = -0.148*100 - 0.291*150 + 0.439*200 + 128
        expected_Cr = 0.439*100 - 0.368*150 - 0.071*200 + 128
        
        # Perform the conversion
        result_Y, result_Cb, result_Cr = RGB.RGB_to_YCbCr()
        
        # Assert each component to be almost equal due to floating-point precision
        self.assertAlmostEqual(result_Y, expected_Y, places=2)
        self.assertAlmostEqual(result_Cb, expected_Cb, places=2)
        self.assertAlmostEqual(result_Cr, expected_Cr, places=2)

    @patch('builtins.input', side_effect=['100', '128', '128'])
    def test_YCbCr_to_RGB(self, mock_input):
        # Expected values calculated based on the YCbCr to RGB conversion formula
        expected_R = 1.164 * (100 - 16) + 1.596 * (128 - 128)
        expected_G = 1.164 * (100 - 16) - 0.813 * (128 - 128) - 0.391 * (128 - 128)
        expected_B = 1.164 * (100 - 16) + 2.018 * (128 - 128)
        
        # Perform the conversion
        result_R, result_G, result_B = YCbCr.YCbCr_to_RGB()
        
        # Assert each component to be almost equal due to floating-point precision
        self.assertAlmostEqual(result_R, expected_R, places=2)
        self.assertAlmostEqual(result_G, expected_G, places=2)
        self.assertAlmostEqual(result_B, expected_B, places=2)


class TestResizeImage(unittest.TestCase):

    @patch('subprocess.run')
    def test_resize_image(self, mock_run):
        # Define test parameters
        input_path = "Input images/input.jpg"
        output_path = "Output images/output.jpg"
        width = 800
        quality = 2

        # Call the function
        resize_image(input_path, output_path, width, quality)

        # Check if subprocess.run was called with the correct arguments
        mock_run.assert_called_once_with([
            "ffmpeg", "-i", input_path, "-vf", f"scale={width}:-1", "-q:v", str(quality), output_path
        ])


class TestSerpentineFunction(unittest.TestCase):

    @patch('cv2.imread')
    def test_serpentine(self, mock_imread):
        # Mock image as a 3x3 matrix
        mock_image = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        
        # Mock `cv2.imread` to return the above image when called
        mock_imread.return_value = mock_image

        # Expected result for a 3x3 image in serpentine order:
        # Starts at [0, 0] = 1, then moves through diagonals as per the described algorithm
        expected_output = [
            1, 4, 2, 3, 5, 7, 8, 6, 9
        ]
        
        # Call the serpentine function
        result = serpentine(mock_image)  # the path here is irrelevant due to mocking
        
        # Verify the output matches the expected serpentine order
        self.assertEqual(result, expected_output)


class TestBWImageFunction(unittest.TestCase):

    @patch('subprocess.run')
    def test_bw_image(self, mock_run):
        # Define test parameters
        input_path = "color_image.jpg"
        output_path = "bw_image.jpg"

        # Call the function
        bw_image(input_path, output_path)

        # Check if subprocess.run was called with the correct arguments
        mock_run.assert_called_once_with([
            "ffmpeg", "-i", input_path, "-vf", "hue=s=0", "-q:v", "31", output_path
        ])


class TestRunLengthEncoding(unittest.TestCase):

    def test_basic_encoding(self):
        data = [1, 1, 2, 2, 2, 3, 3, 1, 1]
        expected_output = [(1, 2), (2, 3), (3, 2), (1, 2)]
        result = run_lenght_encoding(data)
        self.assertEqual(result, expected_output)

    def test_single_value(self):
        data = [5, 5, 5, 5, 5]
        expected_output = [(5, 5)]
        result = run_lenght_encoding(data)
        self.assertEqual(result, expected_output)

    def test_alternating_values(self):
        data = [1, 2, 1, 2, 1, 2]
        expected_output = [(1, 1), (2, 1), (1, 1), (2, 1), (1, 1), (2, 1)]
        result = run_lenght_encoding(data)
        self.assertEqual(result, expected_output)

    def test_large_sequence(self):
        data = [4] * 100  # 100 consecutive 4s
        expected_output = [(4, 100)]
        result = run_lenght_encoding(data)
        self.assertEqual(result, expected_output)


class TestDCT(unittest.TestCase):

    def test_dct_inverse(self):
        # Create a test input signal (e.g., 4x4 matrix with random values)
        input_signal = np.random.rand(4, 4)

        # Encode and then decode the signal
        encoded_signal = DCT.dct_encoder(input_signal)
        decoded_signal = DCT.dct_decoder(encoded_signal)

        # Check if the decoded signal is close to the original signal
        np.testing.assert_allclose(decoded_signal, input_signal, atol=1e-6)

    def test_dct_zero_input(self):
        # Test DCT on a zero input signal
        input_signal = np.zeros((4, 4))

        # Encode and decode
        encoded_signal = DCT.dct_encoder(input_signal)
        decoded_signal = DCT.dct_decoder(encoded_signal)

        # The encoded and decoded signals should both be zero matrices
        np.testing.assert_array_almost_equal(encoded_signal, np.zeros((4, 4)), decimal=6)
        np.testing.assert_array_almost_equal(decoded_signal, np.zeros((4, 4)), decimal=6)

    def test_output_shape(self):
        # Ensure the output shape of dct_encoder and dct_decoder matches the input
        input_signal = np.random.rand(8, 8)
        encoded_signal = DCT.dct_encoder(input_signal)
        decoded_signal = DCT.dct_decoder(encoded_signal)

        # Check shape
        self.assertEqual(encoded_signal.shape, input_signal.shape)
        self.assertEqual(decoded_signal.shape, input_signal.shape)


class TestDWT(unittest.TestCase):

    def test_dwt_known_signal(self):
        # Test a known input where we can manually verify results
        input_signal = np.array([1, 2, 3, 4])

        # Expected outputs after convolution and downsampling
        lp = [np.pi / 2, np.pi / 2]
        hp = [np.pi / 2, -np.pi / 2]
        ylow = np.convolve(input_signal, lp)
        yhigh = np.convolve(input_signal, hp)

        expected_approx = ylow[::2]  # Downsample low-pass result
        expected_detail = yhigh[::2]  # Downsample high-pass result

        # Call the encode_dwt function
        approx_coef, detail_coef = DWT.encode_dwt(input_signal)

        # Verify the function's output with expected results
        np.testing.assert_array_almost_equal(approx_coef, expected_approx, decimal=6)
        np.testing.assert_array_almost_equal(detail_coef, expected_detail, decimal=6)

    def test_dwt_zero_input(self):
        # Test with an all-zero input signal
        input_signal = np.zeros(4)
        approx_coef, detail_coef = DWT.encode_dwt(input_signal)

        # Both approximation and detail coefficients should be arrays of zeros
        expected_approx = np.zeros(len(approx_coef))
        expected_detail = np.zeros(len(detail_coef))

        np.testing.assert_array_almost_equal(approx_coef, expected_approx, decimal=6)
        np.testing.assert_array_almost_equal(detail_coef, expected_detail, decimal=6)

    def test_dwt_single_value(self):
        # Edge case with a single element
        input_signal = np.array([5])
        approx_coef, detail_coef = DWT.encode_dwt(input_signal)

        # Convolve with filters manually to get expected results
        lp = [np.pi / 2, np.pi / 2]
        hp = [np.pi / 2, -np.pi / 2]
        ylow = np.convolve(input_signal, lp)
        yhigh = np.convolve(input_signal, hp)

        expected_approx = ylow[::2]
        expected_detail = yhigh[::2]

        np.testing.assert_array_almost_equal(approx_coef, expected_approx, decimal=6)
        np.testing.assert_array_almost_equal(detail_coef, expected_detail, decimal=6)

if __name__ == '__main__':
    unittest.main()