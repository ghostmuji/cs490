for i in {0..2001}; do 

convert GenerationLoss_step$i.jpg -rotate 90 -quality 85 GenerationLoss_step$(($i+1)).jpg

if [ $(($i%100)) -ne 0 ]; then
 rm GenerationLoss_step$i.jpg
fi
#
# (( i % 100 )) && rm GenerationLoss_step$i.jpg

echo -n "."

done