#!/bin/sh
# 3. Compile the translations files
msgfmt lang/en_US/LC_MESSAGES/i18n_util.po -o lang/en_US/LC_MESSAGES/i18n_util.mo
msgfmt lang/de_DE/LC_MESSAGES/i18n_util.po -o lang/de_DE/LC_MESSAGES/i18n_util.mo
msgfmt lang/zh_CN/LC_MESSAGES/i18n_util.po -o lang/zh_CN/LC_MESSAGES/i18n_util.mo
