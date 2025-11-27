import importlib.util
import pathlib
import unittest


def _load_module():
    repo_root = pathlib.Path(__file__).resolve().parents[1]
    module_path = repo_root / "03" / "bubble-sort.py"
    spec = importlib.util.spec_from_file_location("bubble_sort_mod", str(module_path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestBubbleSort(unittest.TestCase):
    def setUp(self):
        self.mod = _load_module()

    def test_ascending(self):
        self.assertEqual(self.mod.bubble_sort([3, 1, 2]), [1, 2, 3])

    def test_descending(self):
        self.assertEqual(self.mod.bubble_sort([3, 1, 2], reverse=True), [3, 2, 1])

    def test_in_place(self):
        lst = [5, 2, 4]
        self.mod.bubble_sort(lst, in_place=True)
        self.assertEqual(lst, [2, 4, 5])

    def test_empty_and_single(self):
        self.assertEqual(self.mod.bubble_sort([]), [])
        self.assertEqual(self.mod.bubble_sort([1]), [1])

    def test_tuple_and_strings(self):
        self.assertEqual(self.mod.bubble_sort((3, 1, 2)), [1, 2, 3])
        self.assertEqual(self.mod.bubble_sort(["b", "a"]), ["a", "b"])


if __name__ == "__main__":
    unittest.main()
