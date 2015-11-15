#!/bin/sh
# 2. Translate the template to different locales
msginit --input=lang/i18n_util.pot --locale=en_US --output=lang/en_US/LC_MESSAGES/i18n_util.po
msginit --input=lang/i18n_util.pot --locale=de_DE --output=lang/de_DE/LC_MESSAGES/i18n_util.po
msginit --input=lang/i18n_util.pot --locale=zh_CN --output=lang/zh_CN/LC_MESSAGES/i18n_util.po
