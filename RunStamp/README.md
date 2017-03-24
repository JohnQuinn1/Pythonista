# RunStamp

A script for noting the times of runners reaching a checkpoint/finish.

There is the option to mark as 'DNF' (did not finish) and to add a flag ('ERR') to indicate a previous entry was entered in error.

At any point the list and times of runners in so far can be copied to the clipboard as a CSV file.

It is based on the example calculator application that comes with Pythonista.

A function runs in the background updating the time in the UI each second. I find that when the script is stopped the 'x' button needs to be pressed a second time to completely stop the script.

An optional runners.txt file with a comma-separated list of "race_number, runner_name" can be included for diplaying runners names.
There is an issue in that if the script is run directly from the home screen then it starts in the root folder - so the path to where the runners.txt file is expected to be ('Documents/Git/Pythonista/RunStamp/') is added explicitly to the root folder and is chdir'd to. This is also where a log file is kept in case of a crash.

The user interface should be ok for iPhone6s and larger screens (including iPad) but not for smaller screens.
