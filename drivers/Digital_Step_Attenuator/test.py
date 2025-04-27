import unittest
import ATT_6000

class TestATT6000(unittest.TestCase):
    
    def setUp(self):
        self.att = ATT_6000.ATT_6000(port='/dev/ttyUSB0', baudrate=115200)
        self.att.connect()

    def tearDown(self):
        self.att.disconnect()

    def test_convert_to_cmd_format(self):
        # Test the conversion of a value to command format
        value = 12.34
        expected_output = "1234"
        output = self.att.convert_to_cmd_format(value)
        print(f"Output: {output}")
        self.assertEqual(output, expected_output)

        value = 0
        expected_output = "0000"
        output = self.att.convert_to_cmd_format(value)
        print(f"Output: {output}")
        self.assertEqual(output, expected_output)

        value = 30.0
        expected_output = "3000"
        output = self.att.convert_to_cmd_format(value)
        print(f"Output: {output}")
        self.assertEqual(output, expected_output)

        # Test the conversion of a value outside the valid range
        value = -5
        expected_output = "0000"
        output = self.att.convert_to_cmd_format(value)
        print(f"Output: {output}")
        self.assertEqual(output, expected_output)
        
        value = 35
        expected_output = "3000"    
        output = self.att.convert_to_cmd_format(value)
        print(f"Output: {output}")
        self.assertEqual(output, expected_output)

        # check how it deals with too many decimal places
        value = 12.345678
        expected_output = "1234"
        output = self.att.convert_to_cmd_format(value)
        print(f"Output: {output}")
        self.assertEqual(output, expected_output)


    
    def test_set_attenuation(self):
        # Test setting attenuation within valid range
        try:
            self.att.set_attenuation(0)
            self.assertEqual(self.att.current_attenuation, 0)
        except ValueError as e:
            self.fail(f"set_attenuation raised ValueError unexpectedly: {e}")

        # Test setting attenuation outside valid range
        with self.assertRaises(ValueError):
            self.att.set_attenuation(50)  # Should raise ValueError'
    

if __name__ == '__main__':
    unittest.main()