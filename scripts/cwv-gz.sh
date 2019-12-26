#/bin/bash
#
# Copyright CWV Corp All Rights Reserved
#
# 打包all
git pull
rm -rf ../zruntime.tar.gz
tar -zcvf ../zruntime.tar.gz modules conf keystore clib genesis
echo 'zruntime.tar.gz successed...'
sleep 1
# git 获取增量包
# rm -rf ../zruntime-incremet.tar.gz
# git archive --format=tar.gz -o ../zruntime-increment.tar.gz HEAD $(git diff --name-only HEAD^)
# echo 'bruntime-increment.tar.gz successed...'
