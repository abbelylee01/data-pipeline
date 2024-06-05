# tests/test_transform.py
import unittest
import pandas as pd
from etl.transform import transform_data

class TestTransform(unittest.TestCase):
    @unittest.skip("Reason for skipping this test")
    def test_transform_data(self):
        # Sample input data
        data = pd.DataFrame({
            'productId': ['P001', 'P@002', 'P003'],
            'item': ['Item 1', 'Item 2', 'Item 3'],
            'sellprice': ['$10', '$20', '$30'],
            'costprice': ['$8', '$18', '$28'],
            'store location': ['Store#1', 'Store@2', 'Store 3']
        })

        # Expected output data after transformation
        expected_data = pd.DataFrame({
            'PRODUCT ID': ['P001', 'P002', 'P003'],
            'ITEM': ['Item 1', 'Item 2', 'Item 3'],
            'SELLPRICE': [10.0, 20.0, 30.0],
            'COSTPRICE': [8.0, 18.0, 28.0],
            'STORE LOCATION': ['Store1', 'Store2', 'Store 3']
        })

        # Apply the transformation
        transformed_data = transform_data(data)

        # Check if the transformed data matches the expected data
        pd.testing.assert_frame_equal(transformed_data, expected_data)

if __name__ == '__main__':
    unittest.main()



# python -m unittest discover -s test

