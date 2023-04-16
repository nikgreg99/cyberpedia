#!/usr/bin/env bash
# Download sigma rules from https://github.com/SigmaHQ/sigma
git clone https://github.com/SigmaHQ/sigma.git
cd sigma
cp rules cyberpedia/rules

#Download Yara rules from https://github.com/SupportIntelligence/Icewater.git
git clone https://github.com/SupportIntelligence/Icewater.git
