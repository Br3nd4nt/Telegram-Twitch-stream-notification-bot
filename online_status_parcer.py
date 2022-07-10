import requests


def get_online_status(username: str) -> str:
    url = f'https://twitchtracker.com/{username}'
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    } # I stole this shit, dont care, it works this way so whatever
    response = requests.get(url, headers=headers)
    code = response.status_code
    if code == 404: # stfu
        return 'not_found'
    elif code == 200: # yay
        full_text = response.text
        if '"live-indicator-container"' in full_text:
            return 'ONLINE'
        elif 'Last live' in full_text:
            return 'OFFLINE'
        else:
            return 'error'
    else: # dont care didnt ask
        return 'error'


if __name__ == '__main__':
    print(get_online_status('sadyama'))