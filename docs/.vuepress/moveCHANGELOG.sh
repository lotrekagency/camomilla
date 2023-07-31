#!/bin/bash
destination="./docs"
destination=$(cd -- "$destination" && pwd)
changelog_dir="$destination/Changelog/"

mkdir -p $changelog_dir
cp ./CHANGELOG.md $changelog_dir/README.md
