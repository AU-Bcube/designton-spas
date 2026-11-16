import io
import json
import os
from pathlib import Path
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

from scripts.build_netlify import register_domains


class Response(io.BytesIO):
    def __init__(self, data):
        super().__init__(json.dumps(data).encode())


class DomainRegistrationTests(unittest.TestCase):
    def setUp(self):
        self.env = patch.dict(os.environ, {
            "SITE_ID": "site-id", "NETLIFY_DOMAIN_TOKEN": "test-token",
        }, clear=True)
        self.env.start()
        self.addCleanup(self.env.stop)
        self.projects = [Path("alpha"), Path("beta")]

    @patch("scripts.build_netlify.urlopen")
    def test_adds_missing_domains_and_preserves_existing_aliases(self, open_url):
        open_url.side_effect = [
            Response({"custom_domain": "alpha.b-cube.kr", "domain_aliases": ["other.example"]}),
            Response({}),
            Response({"custom_domain": "alpha.b-cube.kr", "domain_aliases": ["other.example", "beta.b-cube.kr"]}),
        ]
        register_domains(self.projects)
        request = open_url.call_args_list[1].args[0]
        self.assertEqual(request.get_method(), "PATCH")
        self.assertEqual(json.loads(request.data), {"domain_aliases": ["other.example", "beta.b-cube.kr"]})

    @patch("scripts.build_netlify.urlopen")
    def test_already_registered_does_not_patch(self, open_url):
        open_url.return_value = Response({"custom_domain": "ALPHA.B-CUBE.KR", "domain_aliases": ["beta.b-cube.kr"]})
        register_domains(self.projects)
        self.assertEqual(open_url.call_count, 1)

    @patch("scripts.build_netlify.urlopen")
    def test_refuses_invalid_response_and_does_not_patch(self, open_url):
        open_url.return_value = Response({})
        with self.assertRaisesRegex(ValueError, "missing the domain alias list"):
            register_domains(self.projects)
        self.assertEqual(open_url.call_count, 1)

    @patch("scripts.build_netlify.urlopen")
    def test_detects_lost_domains_after_update(self, open_url):
        open_url.side_effect = [Response({"domain_aliases": ["other.example"]}), Response({}),
                                Response({"domain_aliases": ["alpha.b-cube.kr", "beta.b-cube.kr"]})]
        with self.assertRaisesRegex(ValueError, "did not retain"):
            register_domains(self.projects)

    @patch("scripts.build_netlify.urlopen")
    def test_api_errors_do_not_expose_response_or_token(self, open_url):
        open_url.side_effect = HTTPError("https://example.com", 403, "forbidden", {}, None)
        with self.assertRaisesRegex(ValueError, "HTTP 403") as error:
            register_domains(self.projects)
        self.assertNotIn("test-token", str(error.exception))

    def test_missing_credentials_fail(self):
        del os.environ["NETLIFY_DOMAIN_TOKEN"]
        with self.assertRaisesRegex(ValueError, "NETLIFY_DOMAIN_TOKEN"):
            register_domains(self.projects)


if __name__ == "__main__":
    unittest.main()
