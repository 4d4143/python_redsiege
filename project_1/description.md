Write a script that will take an IP as input and output ownership and geolocation.

Additionally, implement a feature to read multiple IPs from a provided file and also to read a CIDR range.

Structure:
-Parse CLI args

-Two cases: One single IP/CIDR range via CLI or one filepath
    -Single IP/CIDR range:
        -Parse argument
        -Run query
    
    -Filepath:
        -Validate filepath is valid
        -Load contents from file
        -Run query on each item from contents

-Output contents to CSV file or CLI depending on flag set