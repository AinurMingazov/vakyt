#!/bin/bash

uv pip freeze > requirements.txt
cp requirements.txt vakyt_bot/
cp requirements.txt api/
