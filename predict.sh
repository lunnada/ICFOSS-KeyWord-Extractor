#!/bin/bash
cd /home/rohith/ICFOSS-KeyWord-Extractor/Features
cp features.txt /home/rohith/ICFOSS-KeyWord-Extractor/CRF
cd /home/rohith/ICFOSS-KeyWord-Extractor/CRF
crf_test -m kw_extractor features.txt > output.txt
cp output.txt /home/rohith/ICFOSS-KeyWord-Extractor/Extraction