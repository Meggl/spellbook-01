IntEx()
- Describe what the program does

ReadProfiles()
- Open text document
- Create empty list(s) for each type of metadata needed
- Create empty list(s) for each type of information needed
- Create a counter that keeps track of the count of metadata kinds |*|  count1 = 0  |*|
- Create a counter that keeps track of the count of profiles |*|  count2 = 0  |*|
- Create a list that notes the line number that starts each profile (initiate it with the integer 0:  |*|  tableContents1 = [0]  |*|)
- Create a list that notes the line number that starts each profile (initiate it with the integer 0:  |*|  tableContents2 = [0]  |*|)
- Create a 'list' that holds each line of the whole text doc:  |*|  content = textfile_variable.readlines()  |*|
- Every time there is a separator line in the text doc (------------etc), this denotes a new 'profile'. Every time there is a separator line in the text doc (~~~~~~~etc), this denotes a new type of 'metadata'.
~~ For each element in the 'content' list, do this:
  * 
