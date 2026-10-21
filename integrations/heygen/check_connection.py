#!/usr/bin/env python3
"""Read-only HeyGen readiness check. No upload, generation or paid request."""
import json
import os
import sys
import urllib.error
import urllib.request

ENDPOINT = 'https://api.heygen.com/v2/avatars'


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # Never forward X-Api-Key to a redirect destination.
        return None


def check(environ=None, opener=None):
    env = os.environ if environ is None else environ
    key = env.get('HEYGEN_API_KEY')
    avatar = env.get('HEYGEN_AVATAR_ID')
    if not key:
        return 2, {'ready': False, 'reason': 'missing_api_key',
                   'action': 'Set HEYGEN_API_KEY securely in environment settings.'}
    if opener is None:
        opener = urllib.request.build_opener(NoRedirect())
    request = urllib.request.Request(ENDPOINT, headers={
        'X-Api-Key': key, 'Accept': 'application/json',
        'User-Agent': 'skill-edit-video-readiness/1.0'})
    try:
        with opener.open(request, timeout=20) as response:
            raw = response.read(2_000_001)
        if len(raw) > 2_000_000:
            return 3, {'ready': False, 'reason': 'response_too_large'}
        body = json.loads(raw)
        data = body.get('data') if isinstance(body, dict) else None
        avatars = data.get('avatars') if isinstance(data, dict) else None
        if not isinstance(avatars, list) or any(not isinstance(a, dict) for a in avatars):
            return 3, {'ready': False, 'reason': 'unexpected_api_schema',
                       'action': 'Check current official API documentation.'}
        matched = bool(avatar) and any(a.get('avatar_id') == avatar for a in avatars)
        result = {'api_list_access': True, 'avatar_count': len(avatars),
                  'avatar_configured': bool(avatar), 'avatar_in_list': matched,
                  'generation_verified': False}
        if not avatar:
            result.update(ready=False, reason='missing_avatar_id')
            return 2, result
        if not matched:
            result.update(ready=False, reason='avatar_not_in_this_list',
                          action='Check avatar type, account and current API docs; absence is not proof the avatar does not exist.')
            return 3, result
        result.update(ready=True, scope='read_only_avatar_list_access_only')
        return 0, result
    except urllib.error.HTTPError as exc:
        return 3, {'ready': False, 'reason': 'http_error', 'status': exc.code,
                   'action': 'Check network policy, API entitlement and authentication. Redirects are intentionally refused.'}
    except (urllib.error.URLError, TimeoutError, OSError):
        # Exception messages and response bodies can contain signed URLs or credentials.
        return 3, {'ready': False, 'reason': 'network_or_tls_error',
                   'action': 'Check configured proxy, domain access and TLS trust; do not disable verification.'}
    except (ValueError, UnicodeError):
        return 3, {'ready': False, 'reason': 'invalid_json_response'}


if __name__ == '__main__':
    code, result = check()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(code)
