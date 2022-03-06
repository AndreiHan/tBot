# tBot
Twitter Bot - every 24 hours it send a tweet to the preconfigured account <br>
### Setup
1. Add the KEYs
First option. Follow the menu and enter the credentials <br>
Second option. Create KEY.json inside the storage folder: <br>
###### Note: The key is not stored as plain text. (after the first run, the file is encrypted)
```json
{
  "INIT" : "True",
  "API_Key": "abcdabcdabcdabcd",
  "API_Key_Secret": "1332Q4TERWHTSHRJEUHTF",
  "ACCESS_TOKEN": "1AEWERGFVDZFER",
  "ACCESS_SECRET": "AFEWVDFGBDTGR"
}
```
2. Start the bot with main.py / run.bat (as a docker container) and select the corresponding option.
