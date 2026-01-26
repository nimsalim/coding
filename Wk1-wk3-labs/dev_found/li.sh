#!/bin/bash

num=12

if [ $num -ge 1 ] && [ $num -le 10 ]
then
    echo "Number is between 1 and 10"
else     echo "Number is outside the range of 1 to 10"
fi



#!/bin/bash

num=6

if [ $num -eq 5 ]
then
    echo "Number is 5."
else
    echo "Number is not 5."
fi


#!/bin/bash

num=8

if [ $num -eq 5 ]
then
    echo "Number is 5."
elif [ $num -eq 10 ]
then 
    echo "Number is 10"
else
    echo "Number is neither 5 nor 10."
fi

# LOOPS
#!/bin/bash
for i in $(seq 1 10)
do
   echo $i
done

#!/bin/bash
for i in {10..20}
do
   echo $i
done

#!/bin/bash
for ((i=1 ;i<=5; i++)) 
do
   echo "Iteration $i"
done


While loops

You use a while loop to repeatedly run commands as long as a condition remains true. The following is the basic syntax of a while loop.

while [condition]
do
[commands to be run in each iteration]
done

#!/bin/bash
count=1
while [ $count -le 5 ];
do
   echo "Count: $count"
   count=$((count +1))
done

Until loops

The until loop is similar to the while loop, but it runs a block of code as long as a condition remains false. After the condition becomes true, the until loop stops. Following is the basic syntax of an until loop.

until [condition]
do
[commands to run in each iteration]
done

#!/bin/bash
count=1
until [ $count -gt 5 ];
do
   echo "Count: $count"
   count=$((count+1))
done

#!/bin/bash

countdown=5

echo "Starting car wash..."

until [ $countdown -eq 0 ];
do
    echo "T-$countdown"
    ((countdown--))
    sleep 1 
done

echo "Your wash is complete!"