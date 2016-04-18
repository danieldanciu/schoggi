#!/bin/bash
# Converts a bunch of lessons exported from MS Word as Web Page (Filtered) to the course format
for i in {4..9}
do
  python ./assets/html/generate_laute_A.py assets/html/laute0$i.html
  python ./assets/html/generate_laute_B.py assets/html/laute0$i.html
done
for i in {10..30}
do
  python ./assets/html/generate_laute_A.py assets/html/laute$i.html
  python ./assets/html/generate_laute_B.py assets/html/laute$i.html
done
