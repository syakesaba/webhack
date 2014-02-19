with open("/etc/passwd","r") as f:
    query = []
    query.append("create table `passwd` (`id` CHAR[255] PRIMARY KEY, `uid` INTEGER UNIQUE, `gid` INTEGER, `gecos` CHAR[1024], `homeDirectory` CHAR[1024], `loginShell` CHAR[255]);")
    for line in f:
        _id,_shadow,_uid,_gid,_gecos,_homeDirectory,_loginShell = line.strip().replace("'"," ").split(":")
        query.append("insert into `passwd` values (\'%s\', %s, %s, \'%s\', \'%s\',\'%s\');" % (_id,_uid,_gid,_gecos,_homeDirectory,_loginShell))
for q in query:
    print q
