import requests, time
while True:
    stats = requests.get('https://redacted.ch/ajax.php?action=user&id=4645',
                 cookies={'session': 'V0hBVCBUSEUgRlVDSyBBUkUgWU9VIFRSWUlORyBUTyBETyBOSUdHRVIgRlVDSyBPRkYgVEhJUyBJUyBSQVBFIEpVU1QgRE9OJ1Q=:'},
                 headers={'user-agent': 'stats scraper pls no bulli'}).json()
    print(stats['response']['stats'])
    with open('stats.csv', 'a') as www:
        www.write('{}|{}|{}\n'.format(
            stats['response']['stats']['downloaded'],
            stats['response']['stats']['uploaded'],
            int(time.time())
                  ))
    time.sleep(60*60)#scrape stats every hour, "API use is limited to 5 requests within any 10-second window."

