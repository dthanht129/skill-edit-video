import io
import json
import unittest
from unittest.mock import Mock
from urllib.error import HTTPError, URLError
from check_connection import check, NoRedirect


class ConnectionTests(unittest.TestCase):
    def mock_api(self, data):
        response = io.BytesIO(json.dumps(data).encode())
        return Mock(open=Mock(return_value=response))

    def test_missing_key_never_calls_network(self):
        op = Mock()
        code, result = check({}, op)
        self.assertEqual(code, 2)
        op.open.assert_not_called()

    def test_matched_avatar_does_not_claim_generation(self):
        op = self.mock_api({'data': {'avatars': [{'avatar_id': 'test-avatar'}]}})
        code, result = check({'HEYGEN_API_KEY': 'test-only', 'HEYGEN_AVATAR_ID': 'test-avatar'}, op)
        self.assertEqual(code, 0)
        self.assertFalse(result['generation_verified'])
        self.assertNotIn('test-only', json.dumps(result))

    def test_missing_avatar_requires_configuration(self):
        code, result = check({'HEYGEN_API_KEY': 'test-only'}, self.mock_api({'data': {'avatars': []}}))
        self.assertEqual(code, 2)
        self.assertEqual(result['reason'], 'missing_avatar_id')

    def test_unknown_schema_is_not_readiness(self):
        code, result = check({'HEYGEN_API_KEY': 'test-only'}, self.mock_api({'message': 'changed'}))
        self.assertEqual(code, 3)
        self.assertFalse(result['ready'])

    def test_errors_do_not_expose_values(self):
        for err in [HTTPError('https://api.heygen.com', 401, 'test-only', {}, None), URLError('test-only')]:
            op = Mock(open=Mock(side_effect=err))
            code, result = check({'HEYGEN_API_KEY': 'test-only'}, op)
            self.assertEqual(code, 3)
            self.assertNotIn('test-only', json.dumps(result))

    def test_redirect_does_not_forward_key(self):
        self.assertIsNone(NoRedirect().redirect_request(None, None, 302, '', {}, 'https://elsewhere.example'))


if __name__ == '__main__':
    unittest.main()
