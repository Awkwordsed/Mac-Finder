with open("data.csv", "r") as f:
    database = f.readlines()

print(
    r"""
$$\      $$\                             $$$$$$$$\ $$\                 $$\                     
$$$\    $$$ |                            $$  _____|\__|                $$ |                    
$$$$\  $$$$ | $$$$$$\   $$$$$$$\         $$ |      $$\ $$$$$$$\   $$$$$$$ | $$$$$$\   $$$$$$\  
$$\$$\$$ $$ | \____$$\ $$  _____|$$$$$$\ $$$$$\    $$ |$$  __$$\ $$  __$$ |$$  __$$\ $$  __$$\ 
$$ \$$$  $$ | $$$$$$$ |$$ /      \______|$$  __|   $$ |$$ |  $$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|
$$ |\$  /$$ |$$  __$$ |$$ |              $$ |      $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
$$ | \_/ $$ |\$$$$$$$ |\$$$$$$$\         $$ |      $$ |$$ |  $$ |\$$$$$$$ |\$$$$$$$\ $$ |      
\__|     \__| \_______| \_______|        \__|      \__|\__|  \__| \_______| \_______|\__|      
                                                                                               
    """
)

print(" only insert the first three parts of a MAC address (example, 00:00:00)")

target = input(" Enter MacAddress: ")

for line in database:
    line = line.split("\n")[0]
    macaddr, vendid = line.split(",", maxsplit=1)

    if target == macaddr:
        print("\n", vendid)
        break
