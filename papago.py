import urllib.request
import json


def select_lang(lang_from, lang_to):
    if lang_from == '한국어':
        source = 'ko'
    elif lang_from == '영어':
        source = 'en'
    elif lang_from == '독일어':
        source = 'de'
    elif lang_from == '러시아어':
        source = 'ru'
    elif lang_from == '프랑스어':
        source = 'fr'
    else:
        source = 'en'
    if lang_to == '한국어':
        target = 'ko'
    elif lang_to == '영어':
        target = 'en'
    elif lang_to == '독일어':
        target = 'de'
    elif lang_to == '러시아어':
        target = 'ru'
    elif lang_to == '프랑스어':
        target = 'fr'
    else:
        target = 'ko'
    return (source, target)

def papago(txt, lang_from, lang_to):
    client_id = "YOUR_CLIENT_ID"  # 개발자센터에서 발급받은 Client ID 값
    client_secret = "YOUR_CLIENT_SECRET"  # 개발자센터에서 발급받은 Client Secret 값

    encText = urllib.parse.quote(txt)
    source, target = select_lang(lang_from, lang_to)
    data = "source=" + source + "&target=" + target + "&text=" + encText

    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if (rescode != 200):
        print("Error Code:" + rescode)
        return 'Cannot translate'

    response_body = response.read().decode('utf-8')
    res = json.loads(response_body)

    return (res['message']['result']['translatedText'])
