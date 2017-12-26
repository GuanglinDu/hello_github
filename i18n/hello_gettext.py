# -*- coding: utf-8 -*-
# Ref 1: http://oz123.github.io/writings/2013-08-04-Localizing-with-gettext/
# Ref 2: https://wiki.maemo.org/Internationalize_a_Python_application

# 0. Create the folder structure
# mkdir -pv po/locales/{de_DE,en_US}/LC_MESSAGES/

# 1. Create the template
# xgettext -k_ -kN_ -o po/locales/hello_gettext.pot hello_gettext.py

# 2. Translate the template to different locales
# msginit --input=po/locales/hello_gettext.pot --locale=de_DE --output=po/locales/de_DE/LC_MESSAGES/hello_gettext.po
# msginit --input=po/locales/hello_gettext.pot --locale=en_US --output=po/locales/en_US/LC_MESSAGES/hello_gettext.po
# msginit --input=po/locales/hello_gettext.pot --locale=zh_CN --output=po/locales/zh_CN/LC_MESSAGES/hello_gettext.po

# 3. Compile the translations file
# msgfmt po/locales/de_DE/LC_MESSAGES/hello_gettext.po -o po/locales/de_DE/LC_MESSAGES/hello_gettext.mo
# msgfmt po/locales/en_US/LC_MESSAGES/hello_gettext.po -o po/locales/en_US/LC_MESSAGES/hello_gettext.mo
# msgfmt po/locales/zh_CN/LC_MESSAGES/hello_gettext.po -o po/locales/zh_CN/LC_MESSAGES/hello_gettext.mo

# 4. Run with the specified locale (on Linux/Unix only)
# Now the translation should work:
# LANGUAGE=de_DE python hello_gettext.py 

# 5. msgfmt "invalid multibyte sequence" error (*IMPORTANT)
# Edit zh_CN *.po file and change the Content-Type line to "Content-Type: text/plain; charset=UTF-8\n"
# (Changing the charset from ASCII to UTF-8)

import os
import locale
import gettext

APPNAME = "hello_gettext"
default_lang = 'en_US'

# Determines the language path (the i10n path), ./lang, to load the correct language
current_path = os.path.dirname(os.path.abspath(__file__))
print("The current path: %s" % current_path)

#TRANSLATION_ROOT = os.path.join(os.getcwd(), "po/locales") # only works on Linux/Unix
TRANSLATION_ROOT = os.path.join(current_path, 'po', 'locales') # works on Windows/Linux/Unix
print("The TRANSLATION ROOT: %s" % TRANSLATION_ROOT)

# https://wiki.maemo.org/Internationalize_a_Python_application
# Get the default locale
#lang_encoding = os.environ.get('LANG', '').split('.') # e.g., ['en_US', 'UTF-8'] # Linux/Unix only
current_locale, encoding = locale.getdefaultlocale() # tuple, e.g., ('en_US', 'UTF-8')
if current_locale:
    default_lang =  current_locale
print("The default language is %s" % default_lang)

# A note about setting the language environment: I used the variable LANGUAGE,
# however the gettext module looks for the following variables in that order:
# ('LANGUAGE', 'LC_ALL', 'LC_MESSAGES', 'LANG')
# The following lines make demo work on Windows. Or it only works on Linux/Unix.
#default_lang = 'en_US' # tests only
#default_lang = 'de_DE'
default_lang = 'zh_CN'
os.environ['LC_MESSAGES'] = default_lang

try:
    l = os.environ['LC_MESSAGES']
    print("LC_MESSAGES: %s" % l)
    t = gettext.translation(APPNAME, TRANSLATION_ROOT, [l]) # returns a Translations object
except KeyError:
    t = gettext.translation(APPNAME, TRANSLATION_ROOT)
	
#t = gettext.translation(APPNAME, TRANSLATION_ROOT, [default_lang])
_ = t.ugettext

print(_("Hello World"))
