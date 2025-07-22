#!/usr/bin/env python3
"""Unittest"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch, PropertyMock
from client import GithubOrgClient


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

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the correct URL from org payload."""
        expected_url = "https://api.github.com/orgs/google/repos"
        test_payload = {"repos_url": expected_url}

        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = test_payload

            client = GithubOrgClient("google")
            result = client._public_repos_url

            self.assertEqual(result, expected_url)
