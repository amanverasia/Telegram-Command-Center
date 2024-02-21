## What is Telegram-Command-Center?
Telegram-Command-Center is a python script that when executed on the target device can give you access to their command shell in your telegram bot.

## Scenario
![[Drawing 2024-02-21 13.04.22.excalidraw.png]]

Obviously the above comic is generalizing a lot of things but you get the gist, don't you? Now you might be asking how can you use it.

Well it is very easy, just follow these steps.

## How?

### Creating a Telegram bot
1. To create a Telegram bot firstly you would need a Telegram account. Duh. So if you do not have it, now is the best time to make [one.](https://telegram.org/)
2. Click the search box and search for BotFather and click on it, and click on `/start`
3. Then type `/newbot` to create a new instance of a bot and then name the bot accordingly and give it a unique username afterwards.
4. Once you do that, you will be provided an `api_key` we will be using that shortly.

### Next Steps
Git clone the folder using,
```
git clone https://github.com/amanverasia/Telegram-Command-Center.git
```
Open the `token.txt` file and then replace the text inside with your `api_key` from BotFather
> Note: Ideally you would change the api_token inside the main.py file and then just send the main.py file.
> This is just a demonstration so, I am going to leave the above mentioned thing has an exercise for the user.


\
Run the python file using,
```
python3 main.py
```
if you are on windows use,
```
python main.py
```

That is basically it. You now need to start the new bot that you created using BotFather and whatever messages you send there, will show up as commands on the system where the bot is running.

## Different Commands
`/start` - Starts the bot
`/screenshot` - Takes the screenshot of the thing currently on the screen and sends it back
`any message` - It will interpret it as a command to be sent on the cmd/terminal on the victim machine. For example, `dir` or `ls` will get executed and the bot would send back the list of files in the current directory.

## Will antivirus flag it?
Short Answer - NO
Long Answer - It's Complicated because if you do decide to convert it into an exe file and not sign it properly then it will be flagged down (not saying that any signed files would do any better). The thing is that the virus definition or the signature for this specific file does not exist yet and so it is unlikely that your Windows Defender will flag this file down. At the end of the day, its just Python code running.

## Why?
Why not? The whole thing is just a collection of my tinkering with the Telegram bot API, So many cool things can be done with this concept. The project is not actively being maintained and so if someone wants to contribute to this, they can definitely do so, by opening up a pull request.

If something does not work, (I am so gonna regret this) please raise an issue in the issues tab up at the top.

There are many features missing from this, and I shall be adding them, whenever I feel like, if you wish to help adding those features, as I said, create a pull request. 

If you think that this is a bad inefficient implementation and can be further improved upon monumentally. Please do so, as I said, create a pull request. This code was cobbled together in one afternoon so yeah there will be bugs.

Below is the TODO for the features.

## TODO
- [x] Add screenshots
- [ ] Functionality to have better screenshots (idk what that means, figure it out?)
- [ ] File upload, download functionality. (in progress)
- [ ] Get System Information (merge it with my `machine-info-osint` code)
- [ ] Process Management (yeah idk what we are doing here)