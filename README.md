THL-statusboard
===============

Export script to send The Hit List tasks to Panic Status Board

Inspired by https://github.com/feju/things-status-board

To use:
0. Install this python library for The Hit List: https://github.com/kfdm/thehitlist
1. Place csvexporter in your Scripts directory.
2. Modify the directories specified, so my home directory, etc. aren't hard-coded in. Specify the output location to be inside your dropbox, or something else that will sync and be accessible in status board.
3. Add an item in your scripts folder to periodically run the item. Googling 'launchd scheduling' is your friend. Long story short, you end up with a Plist in your LaunchDaemons directory.
4. Add the new item in Statusboard.
