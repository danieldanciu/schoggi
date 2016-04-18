# Extracts the list of words from a lauteXX.html file (used for the "play all" feature
# -n means don't print by default
# /p at the end actually means print the result
sed -n  "s/.*id=\"\([^\"]*\)\".*playAudio.*/\"\1\",/p" $1
