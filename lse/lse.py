from argparse import ArgumentParser
import json
import requests


def extract_streak(token: str, session: str) -> str:
    payload = {
        'operationName': 'getStreakCounter',
        'query': '''query getStreakCounter {
            streakCounter {
            streakCount
            currentDayCompleted
            }
        }'''
    }
    biscuit = {
        'csrftoken': token,
        'LEETCODE_SESSION': session
    }
    response = requests.post('https://leetcode.com/graphql', json=payload, cookies=biscuit)
    return json.loads(response.text)['data']['streakCounter']


if __name__ == '__main__':
    parser = ArgumentParser(description='LeetCode Streak Extractor')
    parser.add_argument('-t', '--token', help='CSRF token', required=True)
    parser.add_argument('-s', '--session', help='LeetCode Session', required=True)

    args = parser.parse_args()
    streak = extract_streak(args.token, args.session)
    print(streak)
