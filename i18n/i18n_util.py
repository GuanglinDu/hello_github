# -*- coding: utf-8 -*-
# Ref 1: http://oz123.github.io/writings/2013-08-04-Localizing-with-gettext/
# Ref 2: https://wiki.maemo.org/Internationalize_a_Python_application
# A simplified version based on hello_gettext.py

# 0. Create the folder structure
# mkdir -pv lang/{de_DE,en_US,zh_CN}/LC_MESSAGES/

# 1. Create the template (APPNAME = i18n_util)
# xgettext -k_ -kN_  -o lang/i18n_util.pot i18n_util.py (a single file)
# xgettext -k_ -kN_  -o lang/i18n_util.pot -f files-need-i10n.txt (file list)

# 2. Translate the template to different locales
# msginit --input=lang/i18n_util.pot --locale=en_US --output=lang/en_US/LC_MESSAGES/i18n_util.po
# msginit --input=lang/i18n_util.pot --locale=de_DE --output=lang/de_DE/LC_MESSAGES/i18n_util.po
# msginit --input=lang/i18n_util.pot --locale=zh_CN --output=lang/zh_CN/LC_MESSAGES/i18n_util.po

# 3. Compile the translations files
# msgfmt lang/en_US/LC_MESSAGES/i18n_util.po -o lang/en_US/LC_MESSAGES/i18n_util.mo
# msgfmt lang/de_DE/LC_MESSAGES/i18n_util.po -o lang/de_DE/LC_MESSAGES/i18n_util.mo
# msgfmt lang/zh_CN/LC_MESSAGES/i18n_util.po -o lang/zh_CN/LC_MESSAGES/i18n_util.mo

# 4. msgfmt "invalid multibyte sequence" error (*IMPORTANT)
# Edit zh_CN *.po file and change the Content-Type line to "Content-Type: text/plain; charset=UTF-8\n"
# (Changing the charset from ASCII to UTF-8)

import os
import sys
import locale
import gettext

import i18n_tester

APPNAME = "i18n_util"
# Either en_US or zh_CN
default_lang = 'en_US'

# Determines the language path (the i10n path), ./lang, to load the correct language
current_path = os.path.dirname(os.path.abspath(__file__))
print("The current path: %s" % current_path)

#localedir = os.path.join(os.getcwd(), "lang")
localedir = os.path.join(current_path, "lang")
print("The locale dir: %s" % localedir)

# https://wiki.maemo.org/Internationalize_a_Python_application
# Get the default locale
#lang_encoding = os.environ.get('LANG', '').split('.') # e.g., ['en_US', 'UTF-8'] # Linux/Unix only
current_locale, encoding = locale.getdefaultlocale() # tuple, e.g., ('en_US', 'UTF-8')
if current_locale == "zh_CN":
    default_lang =  'zh_CN'
print("The default language is %s" % default_lang)


# http://www.wefearchange.org/2012/06/the-right-way-to-internationalize-your.html
# Perhaps more usefully, you can use the gettext.install() function to put _() into the built-in namespace,
# so that all your other code can just use that function without doing anything special.
# Again, though we have to work around the boneheaded Python 2 API.  
# Here's how to write code which works correctly in both Python 2 and Python 3.
def install():
    kwargs = {}
    if sys.version_info[0] < 3:
        # In Python 2, ensure that the _() that gets installed into built-ins
        # always returns unicodes. This matches the default behavior under Python
        # 3, although that keyword argument is not present in the Python 3 API.
        kwargs['unicode'] = True
    gettext.install(APPNAME, **kwargs)


def set_language(language='en_US'):
    print("\n--- Your current locale: %s" % language)
    t = gettext.translation(APPNAME, localedir, [language])
    global _ # or only the default locale used
    _ = t.ugettext


def test_me():    
    """Tests"""
    print(_("Hello World"))
    print(_("i18n in Python is easy"))


def test_in_class():
    """Tests i18n with an external class"""
    it = i18n_tester.I18nTester()

    # Accesses the variables directly from the object
    #print(it.result)
    print(_(it.greeting))

    # Calls method add
    it.add(2)
    sum1 = it.get_result()
    print("%s = %i" % (_("sum"), sum1))


# Tests with en_US, de_DE, and zh_CN
if __name__ == '__main__':
    install()
    
    set_language()
    test_me()
    test_in_class()
    
    set_language('de_DE')
    test_me()
    test_in_class()
    
    set_language('zh_CN')     
    test_me()
    test_in_class()
