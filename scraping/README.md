# Scraping part of the project

We saved into a .json document the name of associations and their instagrams accounts. 

Now, we'll scrap the data we need with Node.js !

**Why Node.Js ?** 

Simply because we want to explore different languages. We already have some experience with Selenium and BS4, let's use Axios and Cheerio, it'll be fun !

## Information we want to get 

Here is the list of the information we want to get

### Per association 

- Number of publication
- Number of followers
- Number of followings
- Description (we might use some NLP on it. Or at least, get the '#', links and emojis thanks to Regex)
- Highlights stories (number and names)

### Per publication 

- Description
- Number of likes (target)
- Number of commentaries
- Date / Hour
- Localisation 
- ImageB (True or False)
- Image (.jpg)
- Video (True or False)
- Video's duration
- Accounts tag on publication
