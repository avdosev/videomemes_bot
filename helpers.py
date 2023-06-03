def get_bot_token():
    with open('sensitive_info/bot_token') as f:
        res = f.read()
    
    return res