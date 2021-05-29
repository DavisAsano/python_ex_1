# part 4
# task: abbreviate a potentially long string s to have only the x first and x last chars with ... in between.
# for x = 5 this would be: "A very long description" => "A ver...ption" (... is called filler).
# In a loop, set x from 5 to and to 15 and print out x and the abbreviated version 
# there'll be an issue where the result would actually be longer(!) than the un-abbreviated s. 
# For these cases, do not perform your abbreviation, simply print out s. Note that this
# should work for any other string a or filler as well, so don't hardcode things!
# 
# Optional:
# write a general function abbr(s, filler="...", total_width=15) which abbreviates s
# to total_width chars and uses the string filler in between them. Again, make sure the
# result would not be longer than s!
# call your function a couple of times with different parameters and also test edge cases
print("start of part 4") # set breakpoint here
s = "A very long description" # a long string
filler = "..."
# your code here
for x in range(5,15):
    if x * 2 + len(filler) > len(s):
        print(x,s)
    else:
        shortened = s[0:x] + filler + s[-x:] 
        print(x,shortened)
    

print("end of 4") # set breakpoint here 
'''


















# solution 4
s = "A very long description" # a long string
filler = "..."
for x in range(5, 15):
    # check if abbreviation would be longer than s
    if x * 2 + len(filler) > len(s):
        print(x, s)
    else:
        abb_str = s[0:x] + filler + s[-x:] # slice off ends and glue together with filler chars
        print(x, abb_str)
def abbr(s, filler="...", total_width=15):
    "returns a copy of s abbreviated to total_width with filler in the middle" 
    x = total_width // 2 # integer division
    rem = total_width % 2 # remainder will be 1 if width is odd
    abb_str = s[0:x+rem] + filler + s[-x:] # for odd width, add one to front
    if len(abb_str) > len(s):
        return s
    return abb_str
# Test
s = "A very long description"
for tw in range(5, len(s)+1):
    print(tw, abbr(s, "...", tw))
# Edge cases
print(abbr("", "...", 0))
print(abbr("", "...", 999))
print(abbr("", "", 0))
print(abbr("", "", 999))
print(abbr("test", "...", 0))
print(abbr("test", "...", 999))
print(abbr("test", "", 0))
print(abbr("test", "", 999))
print(abbr("A very long description", "....................................", 999))
print(abbr("A very long description", "....................................", 0))
'''
