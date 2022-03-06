# tBot
Twitter Bot - every 24 hours it send a tweet to the preconfigured account <br>
### Setup
1. Create KEY.json inside the storage folder: <br>
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
2. Start the bot with main.py / run.bat (as a docker container)
