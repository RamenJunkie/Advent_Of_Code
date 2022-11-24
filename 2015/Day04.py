import hashlib

input_value = "yzbqklnj"
# input_value = "abcdef"
number = 0
looper = True
result = 0

while looper:
    hash_check = f'{input_value}{number}'
    result = hashlib.md5(hash_check.encode())
    hash_value = result.hexdigest()

    # Part 1
    # if hash_value[0:5] == '00000':
    #     looper = False

    # Part 2
    if hash_value[0:6] == '000000':
        looper = False
    else:
        number+=1

print(result.hexdigest())
print(number)

#Part 1
#282750 too high
#282749 was correct

#Part 2
#6742839
#9962623 Nope
#9962624