simple web client to display play count of itg machine

parses the xml and fetches a result

since it's big xml we might need to turn it into sqlite first

todo:
* parse the xml every once in a while (for now let's do once)
* have a search bar
* load everything locally at first (then have a proper "this fetches from a
database")
* make sure everything is compressed

maybe useful:
* https://github.com/martinblech/xmltodict

---

run with:
```
FLASK_APP=main.py flask run
```

exact line of code that does what i want to replicate:
https://github.com/stepmania/stepmania/blob/27fdfb38718474253aeb33e9f9c7fd1a91ed823a/src/Profile.cpp#L2300

so looks like i just need to build a list of songs in python from the xml.
