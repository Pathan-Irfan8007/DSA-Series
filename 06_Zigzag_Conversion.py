'''
Q. The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
 
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
'''
# Ans :

def zigzagConversion(s, rows):
    rowList = [""]*rows
    first_row = 0
    last_row = rows-1
    goingDown = True
    currentRow = first_row
    i = 0
    if rows == 1:
        print(s)
        return
    
    while(i < (len(s))):
        
        rowList[currentRow] += s[i]
        i += 1
        if(currentRow == last_row):
            goingDown = False
        if(currentRow == first_row):
            goingDown = True


        if(goingDown):
            currentRow += 1
        else:
            currentRow -= 1


    print(rowList)
    print("".join(rowList))

zigzagConversion("PAYPALISHIRING", 3)
zigzagConversion("PAYPALISHIRING", 4)



