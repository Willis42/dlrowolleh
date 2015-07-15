#!/usr/bin/env python
# -*- coding: utf-8 -*-


# q/quit to quit, ENC_message to print encoded "message", otherwise decodes message
# To type an encoded message, use type your message while holding the option key
# (this makes it type in weird unicode characters), letters will be automatically
# lowercased due to an overlap issue, but you can use symbols and punctuation with
# the shift key and it should encode/decode correctly.
# Doesn't support ` or ~ (they're the same character w/ option key), but why the
# hell would you need that?
# Also doesn't support multi-line input, because why

import sys

lettersH = u'œ∑´®†\¨ˆøπåß∂ƒ©˙∆˚¬Ω≈ç√∫˜µŒ„´‰ˇÁ¨ˆØ∏ÅÍÎÏ˝ÓÔÒ¸˛Ç◊ı˜Â¥'
letters = u'qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmy'
punctH = u' ¯˘¿ÚÆ”’» ≤≥÷…æ“‘«``'
punct = u' <>?:"{}| ,./;\'[]\\`~'
numbersH = u'⁄€‹›ﬁﬂ‡°·‚—±¡™£¢∞§¶•ªº–≠'
numbers = u'!@#$%^&*()_+1234567890-='
def decode(s):
	print 'DECODE:',s
	ret = ''
	for i in range(len(s)):
		if s[i] in lettersH:
			ret += letters[lettersH.find(s[i])]
		elif s[i] in punctH:
			ret += punct[punctH.find(s[i])]
		elif s[i] in numbersH:
			ret += numbers[numbersH.find(s[i])]
		else:
			ret += s[i]
	return ret

def encode(s):
	print 'ENCODE:',s
	ret = ''
	for c in s:
		if c in letters:
			ret += lettersH[letters.find(c)]
		elif c in punct:
			ret += punctH[punct.find(c)]
		elif c in numbers:
			ret += numbersH[numbers.find(c)]
		else:
			ret += c
	return ret

if __name__ == "__main__":
	while True:
		s = raw_input('Gimme an encoded message: ')
		encodeCode = 'ENC_'
		if s == 'q' or s == 'quit':
			sys.exit()
		elif s.find(encodeCode) == 0:
			print encode(unicode(s[len(encodeCode):].lower(),'utf-8'))
		else:
			print decode(unicode(s,'utf-8'))
