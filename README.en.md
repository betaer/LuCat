# 🐾 LuCat · Cat Petting Timer for Apple Watch

[English](README.en.md) | [简体中文](README.zh-Hans.md) | [繁體中文（香港）](README.zh-Hant-HK.md) | [Русский](README.ru.md) | [Português (Brasil)](README.pt-BR.md) | [Español (México)](README.es-MX.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Italiano](README.it.md) | [日本語](README.ja.md)

**[Free on the App Store](https://apps.apple.com/us/app/lucat-cat-petting-timer/id6835910184)** · [GitHub introduction](https://betaer.github.io/lucat/en/) · [Read the original post on X](https://x.com/Betaer/status/2124558620260188334)

![LuCat](site/assets/images/lucat-social.jpg)

## An app for petting your cat?

I built LuCat after a simple thought. Apple Watch can record a workout, so could its motion sensors also help record the time we spend petting our cats?

A few minutes together deserve a place in your activity log. LuCat saves those moments for each cat, from your wrist to your iPhone.

## How it works

Choose a cat on Apple Watch, tap Start, and enjoy your time together. Tap End to save the session and sync it to your paired iPhone. Browse your calendar to revisit which cat you spent time with, for how long, and the interaction patterns recorded.

## A profile for every cat

Add your cats, take a profile photo, and open it for a closer look. Keep separate histories for every cat, including Piggy, Little Black, Little Yellow, and Little Orange.

## Weight history

Log weigh-ins for growing kittens or cats managing their weight. Review each cat’s weight changes on a chart.

## Reminders and small goals

Set reminders and a daily goal such as three minutes or three sessions. Reminder notifications can cycle through your cats’ profile pictures.

## Movement insights

Review movement timelines and estimated interaction intensity derived from wrist motion. These are motion estimates, not direct measurements of force or pressure on your cat.

## How I built it

I built LuCat through natural-language conversations with ChatGPT Dot, occasionally sharing images, and used Google Gemini Carbon for two code reviews. The project took about a week, or roughly three eight-hour working days.

## What’s next

Vaccination records and notes, better recognition of interaction patterns, and an experiment in reconstructing a virtual petting scene from watch motion data. The animation idea is still exploratory, and I would love suggestions.

## Community

My four cats and I would love your feedback. Thank you to all their honorary aunties, uncles, big brothers, and big sisters!

[Join the X chat](https://x.com/i/chat/group_join/g2122385444969349533/55EEg15kcr) · [WeChat and Xiaohongshu](https://docs.qq.com/doc/DVmpqSXpBYmVsdnZK)

[Privacy](https://betaer.github.io/lucat/privacy/?lang=en)

## Maintaining this introduction

Edit the matching file in `content/`. Run `python3 scripts/build.py` to regenerate the README files and the website in `dist/`. English artwork lives in `site/assets/`. These public files contain the product introduction, website, and publishing tools.

GitHub Actions regenerates README files after content changes. The betaer.github.io workflow fetches this repository every 15 minutes and publishes the generated pages at /lucat/. Each language has its own static URL, canonical link, hreflang links, and sitemap entry. You can also run that workflow manually to publish immediately.
