#!/bin/bash

poetry export --without-hashes --format requirements.txt > requirements.txt
cp requirements.txt vakyt_bot/
cp requirements.txt api/
