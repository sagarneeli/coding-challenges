def flat_map(arr, map_fn=None):
    def flatten_and_map(lst):
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(flatten_and_map(item))  # Recursively flatten nested lists
            else:
                result.append(
                    map_fn(item) if map_fn else item
                )  # Apply function if provided
        return result

    return flatten_and_map(arr)


# Test cases
if __name__ == "__main__":
    import unittest

    class FlatMapTest(unittest.TestCase):
        def test_should_handle_an_already_flattened_array(self):
            self.assertEqual(flat_map([1, 2, 3, 4]), [1, 2, 3, 4])

        def test_should_handle_an_empty_array(self):
            self.assertEqual(flat_map([]), [])

        def test_should_handle_an_array_that_is_nested_one_layer_deep(self):
            self.assertEqual(flat_map([1, 2, [3]]), [1, 2, 3])

        def test_should_handle_a_nested_array_with_two_elements(self):
            self.assertEqual(flat_map([1, [2, 3]]), [1, 2, 3])

        def test_should_handle_an_array_with_several_layers_of_nesting(self):
            self.assertEqual(flat_map([[1, 2, [3]], 4]), [1, 2, 3, 4])

        def test_should_handle_an_array_with_many_layers_of_nesting(self):
            self.assertEqual(flat_map([[[1, [[[[2]]]], 3]]]), [1, 2, 3])

        def test_should_handle_a_nested_array_with_an_adding_callback_function(self):
            self.assertEqual(flat_map([1, 2, [3]], lambda x: x + 2), [3, 4, 5])

        def test_should_handle_a_double_nested_array_with_a_square_callback_function(
            self,
        ):
            self.assertEqual(flat_map([[1, 2, [3]], 4], lambda x: x * x), [1, 4, 9, 16])

        def test_should_handle_a_several_nested_layers_with_an_adding_callback_function(
            self,
        ):
            self.assertEqual(flat_map([[1, 2, [3]], 4], lambda x: x + 2), [3, 4, 5, 6])

        def test_should_handle_an_array_that_has_an_uncouth_level_of_nesting(self):
            self.assertEqual(flat_map([[[[[[[[[[1]]]]]]]]]]), [1])

    unittest.main()
