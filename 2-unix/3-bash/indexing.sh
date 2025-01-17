#!/bin/bash
files=(/etc/hosts /etc/profile)
for file in "${files[@]}"; do
	ls -l "$file"
done
