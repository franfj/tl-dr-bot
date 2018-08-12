with open('../resources/tokens.txt') as f:
    file_lines = f.readlines()

    BOT_TOKEN = file_lines[0].split('===')[1].replace('\n', '')
    FIREBASE_URL = file_lines[1].split('===')[1].replace('\n', '')
