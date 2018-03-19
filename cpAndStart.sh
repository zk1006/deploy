#! /bin/bash

dir=$(date +%Y%m%d)

IFS=',' pro=($3)
for s in ${pro[@]}
do
    cd $2/$dir;
    pack=`find $s*.war `
    #复制包到tomcat
    cp -rp $pack $1/webapps/$s.war
done

cd $1/bin/
./startup.sh