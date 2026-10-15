# ec_syndrome
A medicine for Dell (or other)'s terrible EC thermal table. Might work.

## Why?
See [my reddit post](https://www.reddit.com/r/Dell/comments/1vu44f5/dell_did_my_precision_7550_dirty/).

There are also some laptop manufacturers that do this. 

## What is the safe zone for the clock?
It depends on the game/task you're playing/using. On CS2, [960,1300] gives best performance and temperature. Same thing for Overwatch and Strinova. Stellar Blade could use the same range, but if your GPU is still throwing error then goes with [960,1200]. FFXIV could use [960,1150]. Same with R6 Siege.

On Valve's Deadlock there is no definitive clock as the GPU will throttle itself after a few minutes anyway. This is a weird outlier.

## Usage
Download the ec_syndrome.zip on Releases. Extract it somewhere convenient.

Before running, make sure nvidia-smi and [Sudo for Windows](https://learn.microsoft.com/en-us/windows/advanced-settings/sudo/) is available on your system and is launchable from your command line.

Run the main.exe file from the extracted folder.

## Effectiveness
Most games could run nicely with GPU caps. On my system, CS2 can reach 120+ FPS, Siege and Overwatch at 90. Stellar Blade can run at a crisp 1080p60.

However there are some quirks. Siege will P3 throttle after some time (might be for 45-60 minutes). Deadlock can't run at all. And your GPU might randomly throttle itself even with clock caps. Your only option is to reboot or reset your GPU.

## License
MIT. Feel free to do anything (that is allowed by the license).
