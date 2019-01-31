simple web client to display play count of given song on itg machine

todo:
* build a song list in a python representation
	* parse the xml into a dict
* have a search bar that queries the python dict
database")

---

nice things todo later:
* only parse the xml once an hour? once per session? idk how often
stepmania writes stats.xml. probably after every song or every 3 songs.
* make sure everything is compressed
* since it's big xml we might need to turn it into sqlite first

---

run with:
```
FLASK_APP=main.py flask run
```

exact line of code that does what i want to replicate:
https://github.com/stepmania/stepmania/blob/27fdfb38718474253aeb33e9f9c7fd1a91ed823a/src/Profile.cpp#L2300

so looks like i just need to build a list of songs in python from the xml.

* interesting reading: https://blog.sqreen.io/preventing-sql-injections-in-python/
