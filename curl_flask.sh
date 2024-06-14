result=`curl -s http://127.0.0.1:8001`
echo $result

numWords=`echo $result | wc -w`
echo $numWords