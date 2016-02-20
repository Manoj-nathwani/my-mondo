# My Mondo [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Manoj-nathwani/my-mondo)

Built during [MondoHack 3](https://attending.io/events/mondohack-3)

[Mondo](https://getmondo.co.uk) are awesome however they only have an iOS app. My Mondo is a clone of their app as a heroku webapp which you can access on any device and can be pinned to your home screen to look + act exactly like their iOS app.

Daily summary | Individual purchases
----- | -----
![](http://i.imgur.com/8jUu3K2.jpg) | ![](http://i.imgur.com/E0F0ZfL.jpg)

# Deploying Disclaimer
- Mondo don't currently allow other people to log into your app yet, so you're going to have to host the app yourself and pass in your username and password as raw strings. This sucks. I know. But it's the only way at the moment.
- As the API is in Alpha, I'm not bothering with any cacheing or storing of any data. So the app is technically inefficient when it comes to requesting tokens.

# Deploying
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Manoj-nathwani/my-mondo)
- Have your Mondo `client_id` and `client_secret` at hand from your Mondo Oauth app
- You'll also need (if you want) your [Pushbullet](https://www.pushbullet.com) `Access Token` to send yourself notifications whenever a payment is made. Remember to add the webook on the Mondo developer dashboard to activate this!

# Help
- Check out the official docs here: https://getmondo.co.uk/docs
- Also the slack channel here: https://devslack.getmondo.co.uk
