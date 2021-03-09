import os
import re
mylines=[]
# Regex used to match relevant loglines (in this case, a specific IP address)
reg = re.compile(r"order(.+)api_key: '44e77b482d86ae86791a8b228e0d711c'}", re.DOTALL)
# Output file, where the matched loglines will be copied to
output_filename = os.path.normpath("output.json")
# Overwrites the file, ensure we're starting out with a blank file
with open(output_filename, "w") as out_file:
    out_file.write("")

# Open output file in 'append' mode
with open(output_filename, "a") as out_file:
    # Open input file in 'read' mode
    with open("C:\\Users\\belar\\Desktop\\File_Log.log", "r") as in_file:
        # Loop over each log line
        for line in in_file:
            #mylines=mylines.append(line.rstrip('\n'))

            if reg.search(line) != None:  # If a match is found


              out_file.write(reg)