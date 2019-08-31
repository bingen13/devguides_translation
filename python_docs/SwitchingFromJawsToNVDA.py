# -*- coding: utf-8 -*-
documentation = [
_(u"""# Switching From JAWS To NVDA"""),
"",_(u"""## Introduction"""),
"",_(u"""The purpose of this guide is to assist users of JAWS (Job Access With Speech), a commercial screen reader by Freedom Scientific to switch to the open-source screen reader NVDA (NonVisual Desktop Access) with ease. It assumes prior knowledge of JAWS and that you are proficient in its use."""),
"",_(u"""It is not intended to be a replacement of the included user guide, rather as a means to make NVDA seem less daunting."""),
"",_(u"""## Strengths And Weaknesses """),
"",_(u"""The intent of this guide is not to be a comparison of JAWS and NVDA, but it is necessary to mention some things that work differently.  In most daily situations, NVDA works just as well as JAWS, if not better in some cases."""),
"",_(u"""## A Quick Note about NVDA's Laptop Keyboard Layout"""),
"",_(u"""Selecting the laptop keyboard layout does not automatically set the CapsLock key to act as the NVDA modifier key.  In NVDA's keyboard settings, a checkbox is provided next to the Keyboard Layout combo box to toggle this setting.  Press NVDA+control+k to open these settings."""),
"",_(u"""## Note On The Insert Key."""),
"",_(u"""As you may be aware, both JAWS and NVDA can use the insert key for its modifier key. Both screen readers treat it slightly differently, which could lead to some confusion if you are used to one or the other."""),
"",_(u"""With JAWS loaded, the insert key is solely for its use. This means that, in order to use the original function assigned to it (such as switching between insert and overwrite modes in a text editor or word processor), you first have to activate JAWS's pass key through command."""),
"",_(u"""NVDA, on the other hand, allows you to carry out the insert key's original function by pressing it twice quickly."""),
_(u"""Keep this in mind the next time you're editing text while using NVDA and find yourself erasing what you've already written by typing over it.  This also works for caps lock when it is assigned as the NVDA modifier key (press it twice to toggle caps lock)."""),
"",_(u"""## Alternative Synthesizers"""),
"",_(u"""Windows OneCore voices, included in Windows 10, is used by NVDA as the default synthesizer in Windows 10.  Windows OneCore voices are responsive, natural-sounding and available in many languages.  To add extra voices install a new language in Windows 10 itself, including the language pack.  Variants of a language, such as \"English (United Kingdom)\" and \"English (United States)\" each include different voices."""),
"",_(u"""The eSpeak NG synthesizer is also included with NVDA.  It is used as the default in Windows 8.1 and earlier. Like NVDA itself, eSpeak NG is also free and open-source, which is one of the reasons for its inclusion. Another being the sheer amount of languages it can speak."""),
"",_(u"""Both Windows OneCore Voices, and eSpeak NG, have access to features such as \"rate boost\", enabling the speech rate to effectively be doubled.  You can also press SHIFT to pause, and continue, speaking, instead of CONTROL which simply stops speech."""),
"",_(u"""To change synthesizer, press NVDA+control+s.  To set other voice options, press NVDA+control+v."""),
"",_(u"""However, you may find that, for whatever reason, neither Windows OneCore, nor eSpeak NG is right for you. If this is the case you will be glad to know that there are alternatives, which will be discussed in the following sections."""),
"",_(u"""### Eloquence"""),
"",_(u"""Code Factory has released a version of [eloquence as an NVDA add-on which can be purchased from this link.](http://codefactoryglobal.com/app-store/voices-for-nvda/).  A license to use Nuance's Vocalizer synthesizer is also included in the price."""),
"",_(u"""See the section entitled \"Scripts\" for information about NVDA add-ons."""),
"",_(u"""### Even more voices"""),
"",_(u"""If you still cannot find the perfect voice for you, the [Extra Voices page](http://community.nvda-project.org/wiki/ExtraVoices) lists several other speech synthesizers (both free and paid you can use instead."""),
"",_(u"""## Terminology"""),
"",_(u"""Most of the time, both NVDA and JAWS share a lot of the same terminology to describe controls e.g. radio buttons, combo boxes, checkboxes etc."""),
"",_(u"""One notable difference is that NVDA differentiates between single and multi-line edit fields, and will also tell you if a field is \"protected\" (anything you type will be replaced by asterisks).  It will also alert you if text is selected in a field when you tab over to it.  If so, typing will replace the highlighted text."""),
"",_(u"""NVDA  refers to the different languages a speech synthesizer can speak as voices, and the different voices supported by your synthesizer as variants."""),
"",_(u"""## Cursors"""),
"",_(u"""NVDA has various cursors to aid in navigating Windows and applications, similar to JAWS.  The terminology is slightly different as described below."""),
"",_(u"""The PC cursor in NVDA's documentation is referred to as the system focus and system caret."""),
"",_(u"""The equivalent to the JAWS cursor is a combination of object navigation, the review cursor and the various review modes; such as  Document review, object review and Screen Review. The Screen Review function is the one perhaps most similar to the JAWS cursor.  However, it is beneficial to become familiar with all of these. You will find thorough, easy to understand instructions in the user guide, or the [Basic Training for NVDA](https://www.nvaccess.org/product/basic-training-for-nvda-ebook/) ($30 AUD)."""),
"",_(u"""Unlike JAWS, you don't have to switch between the PC and JAWS cursor equivalents as the numpad is reserved exclusively for working with the JAWS cursor like functions."""),
"",_(u"""It is worth noting that when you use object navigation or the review cursor, the mouse does not, by default, move in sync. You have to press a command to move the mouse to the location of the review cursor, which is similar to how JAWS' \"invisible cursor\" works. There are also commands to simulate clicking or locking both mouse buttons."""),
"",_(u"""However, if you simply want to activate the current object you are focused on when using object navigation, there is a command to do this without having to move the mouse cursor to it first."""),
"",_(u"""### Accessing the notification area (system tray)"""),
"",_(u"""NVDA does not provide a dialog to access the notification area, as this is accessible natively.  Press WINDOWS+B to access the notification area.  To move between notification area items, either use the arrow keys or press the first letter of an item.  Pressing the spacebar on an icon is the same as left-clicking the mouse.  Pressing enter is the same as double-clicking the left mouse button (there is no distinction between these in Windows 10).  Pressing the applications key or or shift+f10 to open the context menu for an item."""),
"",_(u"""If the first item in the notification area is \"Notification chevron button\", Windows is not set to show all icons.  Press ENTER or spacebar to open this and then arrow through the items.  To set Windows to always show all notification area icons, open \"notification area\" windows settings, or \"select which icons appear on the taskbar\", and ensure \"Always show all icons in the notification area\" is checked."""),
"",_(u"""If you prefer to have a dialog you can access with NVDA+F11, there is a \"SysTrayList\" add-on available in the [Add-ons website](https://addons.nvda-project.org/index.en.html)."""),
"",_(u"""### Accessing the ribbon"""),
"",_(u"""Microsoft Office 2007 replaced the menu and toolbars with a \"ribbon\".  Like the notification area, these are accessible so NVDA does not provide a \"virtual ribbon\" replacement.  Microsoft has a page on [Using the keyboard to work with the ribbon](https://support.office.com/en-us/article/use-the-keyboard-to-work-with-the-ribbon-954cd3f7-2f77-4983-978d-c09b20e31f0e).  Essentially press ALT or ALT+letter to access individual ribbons.  Press CONTROL+LEFT and RIGHT ARROWS to move between groups within the current ribbon (eg Clipboard, font, paragraph, etc in Word's Home ribbon).  Press TAB to move between individual items in each ribbon and spacebar or enter to activate the current ribbon item.  The Ribbon also includes \"tell me\".  Press alt+q, type the command or feature you would like to access, use the arrow keys to select it from the list and enter to activate it."""),
"",_(u"""### Checking the status of progress bars"""),
"",_(u"""Jaws provides a command control+insert+b to check the status of progress bars in the current window.  NVDA has options to have progress bars automatically reported as they update.  This can be done verbally (\"5%\", \"6%\", \"23%\", etc), as beeps, increasing in pitch, or both.  To adjust this, press NVDA+U.  Alternatively, it is available from the Object Presentation settings.  Press NVDA+control+o to open these settings."""),
"",_(u"""### Accessing characters and emoji"""),
"",_(u"""Jaws has a command INSERT+4 to select symbols.  In NVDA INSERT+4 (assuming INSERT is your NVDA modifier key) toggle speak command keys, which reports when non-alphanumeric keys, such as spacebar or arrows are pressed.  To select special characters can be done in different ways in many programs.  For instance, press CONTROL+ALT+E to type a Euro symbol in Word.  The insert symbol functionality in Word (ALT+N, then U) is accessible, although some of the symbols listed in the \"more symbols\" dialog are not read correctly in all versions of Word.  Similarly, the \"charmap\" program in Windows itself allows any symbol from any font to be inserted.  Again, not all characters are completely described."""),
"",_(u"""The Windows 10 Emoji window is accessible.  Press WINDOWS+. (WINDOWS+full stop).  Press TAB to move to the categories, select a category then press enter.  Press SHIFT+TAB to move to the list of emoji for that category, use the arrows to move between the available emoji and enter to insert the current emoji into text.  Press escape when done."""),
"",_(u"""### Touch cursor"""),
"",_(u"""In JAWS 15 or later, you can use numpad keys to navigate apps using a tree-like structure, similar to how users of smartphone screen readers such as VoiceOver would navigate touchscreens. in NVDA, object navigation and object mode touch commands can be used for this purpose"""),
"",_(u"""## Virtual Cursor"""),
"",_(u"""The virtual cursor in NVDA is known as browse mode. It functions in much the same way as JAWS, giving you access to navigation quick keys, or in NVDA speak, single letter navigation."""),
"",_(u"""Following are some common issues you may encounter when browsing the web with NVDA for the first time, and how to address them."""),
"",_(u"""### Why Is Everything On One Line?"""),
"",_(u"""In case you are unaware, JAWS has two modes for displaying webpages or other documents using the virtual cursor; simple layout and screen layout.  Simple layout is the default, which displays content in a linear fashion - putting each link or control on its own line.  Screen layout formats the content similar to how it's displayed on screen."""),
"",_(u"""The default in NVDA is screen layout, but you can easily switch to its version of simple layout by pressing NVDA+V while in browse mode. This will turn Screen layout off. Be sure to save your configuration after making this change with NVDA+CTRL+c."""),
"",_(u"""### It Keeps Saying Clickable Clickable Clickable."""),
"",_(u"""While reading webpages, you might notice sometimes that NVDA says \"clickable\", even multiple times on the same link or control."""),
"",_(u"""As of version 2018.4 and later, NvDA will now only say clickable once, so if you experience this issue, please upgrade your copy. Because there is no cost associated with upgrading, NV Access recommends always using the latest stable release of NVDA."""),
"",_(u"""You can also turn off the announcement of clickable elements entirely by going to document formatting in settings (NVDA+control+d) and unchecking \"clickable\" in the elements group."""),
"",_(u"""### Find doesn't work on the web."""),
"",_(u"""While JAWS is loaded, pressing ctrl+f in Internet Explorer or Firefox brings up the JAWS Find dialogue rather than activating the browser's built-in find command.  This is to allow you to search for text using the virtual cursor.  The regular find command will search for the next occurrence of the entered text, but will not move the virtual cursor to that location.  This is due to how screen readers interact with web pages."""),
"",_(u"""NVDA has its own find command to search in browse mode, but it has not been tied to CTRL+F, so pressing that shortcut key calls up the browser's find command, hence find not working as expected."""),
"",_(u"""To bring up NVDA's find dialogue, press ctrl+NVDA+F.  Type in what you wish to find then press enter."""),
"",_(u"""### No commands to view forms and headings?"""),
"",_(u"""In JAWS, you can press JAWS+F5 to list forms, JAWS+F6 to list headings and JAWS+F7 to list links. In NVDA, the latter two have been combined into an elements list dialog, and you can access it by pressing NVDA+F7.  You can then press ALT+H to select Headings (the default), ALT+F for form field, ALT+B for buttons and ALT+D for landmarks."""),
"",_(u"""## Forms Mode"""),
"",_(u"""The equivalent of forms mode in NVDA is focus mode, and it behaves very similar to JAWS, Even switching modes automatically when navigating through a webpage. It will play a sound alerting you to which mode you are in.  If desired, NVDA can speak the mode change rather than use a sound."""),
"",_(u"""Details about Focus Mode can be found in the user guide."""),
"",_(u"""## NVDA talks too much."""),
"",_(u"""Sometimes you may find that NVDA can seem overly verbose, particularly in some list views. This is because as far as NVDA is concerned, list views are tables.   NVDA is configured by default to announce each column or row header."""),
"",_(u"""To turn that option off, uncheck \"Report table row/column headers\" in the \"Document Formatting\" screen of NVDA's settings dialogue.  Press NVDA+control+d to open this setting screen."""),
"",_(u"""## the Speech dictionary"""),
"",_(u"""NVDA has always included a function to edit \"Speech Dictionaries\", which are similar to JAWS' dictionary manager files.  There is a group of radio buttons in the Add/edit dictionary entry labelled type, which determines how the text in the pattern, (NVDA speak for actual word), box will be treated."""),
"",_(u"""* anywhere, which is the default behavior."""),
_(u"""* Whole word, which is how JAWS handles dictionary entries."""),
_(u"""* Regular Expression, which is complicated."""),
"",_(u"""You will also find a case sensitive checkbox."""),
"",_(u"""Access the speech dictionaries with NVDA+n (to open the NVDA menu), then P for preferences, then D for dictionaries.  There are three options.  Default dictionary works across the board, Voice dictionary works only for the current voice, and temporary works only for the current session.  Unless you know you want one of the other two, most of the time \"default dictionary\" is the desired dictionary to edit."""),
"",_(u"""## Scripts"""),
"",_(u"""Like JAWS, scripts can be added to NVDA to provide support for other applications or to add new features that can be accessed from anywhere.  These script packages are called NVDA Add-ons.  You can find add-ons on the [NVDA Community Add-ons page](http://addons.nvda-project.org/)."""),
"",_(u"""These include a few that emulate JAWS features not currently present in NVDA such as a system tray list, virtualise window function and ability to append text to clipboard. Scripts for popular applications such as GoldWave are also available. The user guide has details on installing add-ons, and you can read help documentation that comes with each add-on to learn more about how to use the add-on."""),
"",_(u"""There is an [NVDA Developer Guide](https://www.nvaccess.org/files/nvda/documentation/developerGuide.html) with information on how to create add-ons."""),
"",_(u"""## Remote access"""),
"",_(u"""In 2015, Christopher Toth and Tyler Spivey released a free add-on to allow NVDA users to provide remote support, similar to JAWS Tandem. To learn more about this add-on, go to the [NVDA Remote site](http://www.nvdaremote.com)."""),
"",_(u"""## Application-specific settings"""),
"",_(u"""NVDA can use configuration profiles, which make it possible to configure certain settings to be applied only when using a program. This is done by creating an app-specific configuration profile. To create an app-specific profile, open the Configuration Profiles dialogue while using the app in question. To open the dialogue, hit NVDA+N, to bring up the NVDA menu. arrow down until you hear configuration profiles and press enter, or press NVDA+control+P.  """),
"",_(u"""When the dialogue opens, select New, and select \"current application\" when asked when to use this profile.  Any changes made to NVDA settings (eg synthesizer, speech rate or punctuation level) are applied to this profile."""),
"",_(u"""### Alternate say all"""),
"",_(u"""In recent versions of JAWS, you can configure a different speech synthesizer to be used when say all is active. You can do this in NVDA by creating a say all profile in the configuration profiles menu."""),
"",_(u"""Here are the steps."""),
"",_(u"""1. Open the configurations profile from the main NVDA menu. Press NVDA, N, then arrow down to configuration profiles."""),
_(u"""2. Create a new profile by tabbing to the *new* button or press alt, N."""),
_(u"""3. After you name your profile, tab to the profile usage radio butttons. arrow down until you hear \"say all\". Hit *OK* """),
"",_(u"""while this profile is active, you need to complete the process by configuring the synthesizer while the say all profile is active."""),
]