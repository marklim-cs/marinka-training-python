import unittest
from .hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def test_insert(self):
        arr = HashTable()
        arr.insert("Alla")
        arr.insert("Camil")
        arr.insert("Doo")
        self.assertEqual(arr.items(), [['Doo'], None, None, None, None, None, ['Camil'], None, ['Alla'], None])

    def test_insert_same_index(self):
        arr = HashTable()
        arr.insert("Alla")
        arr.insert("Lisa")
        arr.insert("Doo")
        arr.insert("Stuart")
        arr.insert("Adelle")
        arr.insert("Bob")
        arr.insert("Thomas")
        self.assertEqual(arr.items(), [['Doo', 'Thomas'], None, None, ['Lisa', 'Stuart', 'Adelle'], None, ['Bob'], None, None, ['Alla'], None])

if __name__ == '__main__':
    unittest.main()