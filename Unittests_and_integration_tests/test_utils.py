#!/usr/bin/env python3
"""Unittest"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch
from client import GithubOrgClient


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class that inherits from unittest.TestCase"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test that access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, missing_key):
        """Test that a KeyError is raised with the expected message"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{missing_key}'")


class TestGetJson(unittest.TestCase):
    """TestGetJson class that inherits from unittest.TestCase"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """test get_json"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """TestMemoize class that inherits from unittest.TestCase"""
    def test_memoize(self):
        """test memoize"""
        class TestClass:
            """Test class"""
            def a_method(self):
                """a_method"""
                return 42

            @memoize
            def a_property(self):
                """a_propery"""
                return self.a_method()

        test_obj = TestClass()

        with patch.object(test_obj, 'a_method',
                          return_value=42) as mock_method:
            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mock_method.assert_called_once()


class TestGithubOrgClient(unittest.TestCase):
    """TestMemoize class that inherits from unittest.TestCase"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        expected_payload = {"login": org_name, "id": 123}
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected_payload)


