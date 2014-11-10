n = input()
existing_qq_nums = {}
for i in xrange(n):
    cmd = raw_input().split()
    if cmd[0] == "N":
        if cmd[1] in existing_qq_nums:
            print "ERROR: Exist"
        else:
            existing_qq_nums[cmd[1]] = cmd[2]
            print "New: OK"
    else:
        if cmd[1] in existing_qq_nums:
            if cmd[2] == existing_qq_nums[cmd[1]]:
                print "Login: OK"
            else:
                print "ERROR: Wrong PW"
        else:
            print "ERROR: Not Exist"