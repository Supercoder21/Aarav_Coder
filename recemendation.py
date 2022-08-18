def allofit(x):
    import requests
    texty = ''
    soup = str(requests.get('https://youtube.com/watch?v='+x).content)
    spawny = soup.split(',')
    for i in spawny:
        if i.startswith('"title"'):
            text = i.replace('"title":','')
            text = text.replace('{"accessibility":{"accessibilityData":{"label":','')
            text = text.replace('{"simpleText":','')
            text = text.replace('}','')
            text = text.replace('{"runs":[','')
            text = text.replace(']','')
            text = text.replace('{"text":','')
            text = text.replace('\xe2\x80\x93','')
            texty = texty+text+'\n'
    return texty
