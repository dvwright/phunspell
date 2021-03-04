# basic, not ideal hack for test data
for i in `ls`; do echo $i >> words.txt && sort -R $i/*.dic|head -n 5 >> words.txt; done
