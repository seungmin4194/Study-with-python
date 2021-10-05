#!/usr/bin/env sh

REMOTE_REPO=$(git remote)
WORKING_BRANCH=$(git branch --show-current)

git pull ${REMOTE_REPO} ${WORKING_BRANCH}
echo "> pull complete from remote:${REMOTE_REPO} branch:${WORKING_BRANCH}"

git status
echo "> git status"

git add .
echo "> add all files"

if [ $# -eq 0 ]; then
	read -p "> enter commit message: " COMMIT_MESSAGE
else
	COMMIT_MESSAGE=${1}
fi

git commit -m "${COMMIT_MESSAGE}"
echo "> commit complete"

if [ $? = 0 ]; then
	echo "> push complete to remote:${REMOTE_REPO} branch :${WORKING_BRANCH}"
else
	git reset --soft HEAD^
	echo "> push failed. Please check the git error message."
fi

git push
echo "> push complete"
