# Bio Bro Bot

Reads the first ten DNA bases from a random genetic sequence of the Lady Slippers Orchid, 
in dialects like Bro and Awesome.

## Install

    git clone [this repo] bio-bro-bot
    cd bio-bro-bot
    virtualenv venv
    sourve venv/bin/activate
    . speak.sh

## Extending

Adding dialects is easy. In `config.yml`, copy the template, 
change the copy's name to something other than template, and add
quoted values for each base.

## Note on the Voice

Bio Bro Bot uses `espeak` to read the Python script's output. If your computer doesn't have `espeak`, you can:

* [get it](http://espeak.sourceforge.net/).
* Use `say` instead, if you're on Mac.
* Cry, if you're on Windows. I haven't looked into making this work on Windows.