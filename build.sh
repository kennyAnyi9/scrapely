#!/usr/bin/env bash
apt-get update && apt-get install -y libxml2-dev libxslt1-dev
pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt