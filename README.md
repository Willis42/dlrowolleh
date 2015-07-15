# dlrowolleh
A silly little python script for converting "coded" messages typed by holding down the option key on a mac. Used for shenanigans in an intern skype chat.

## How do I use it??
You need python 2.7 (it might work with 3.x but I have not tried it)
* run it in terminal (python translate.py)
* paste an "encoded" message to output the decoded message
* write ENC_this is my message to encode "this is my message"
* It will convert all letters to lowercase because of how the mac unicode keyboard is set up (some of them overlap between uppercase and lowercase and it's better if they don't LooK LIKe thIs). 
* All punctuation/numbers are supported (you can use the shift key), except for \`/~ (below escape), because those aren't unicodified. It'll technically work, but it will just convert anything to \`. 
* type q/quit/control+c to quit the program

I really don't expect this repo to be used much or for much to be done with it, but if you feel like contributing, go ahead!
