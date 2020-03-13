# The Extractor

![Sarah Connor](https://cdn.vox-cdn.com/thumbor/80cX0s7Y6ID0iHU0KvH_pPrEE3k=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/16294722/phx03489r.jpg "Sarah Connor")

Phone and email extractor using Regular Expressions (regexes) &amp; python.

## Without Regex

The [isPhoneNumber()](wo_regex/isPhoneNumber.py) function works but is limited; it can only find one pattern of phone numbers.

Edge cases:
- 415.555.4242
- (415) 555-4242
- 415-555-4242 x 99

Function isPhoneNumber() would fail to validate the above edge cases. You can add more code but there is an easier way.

\d in regex stands for a digit character (0-9).
```
\d\d\d-\d\d\d-\d\d\d\d
```
The above pattern matches the same text pattern as the isPhoneNumber() function: a string of three numbers, a hyphen, three more numbers, another hyphen, and four numbers. Any other string would match the pattern.

## Creating Regex Objects

All regex functions are in the _re_ module.

```python
# import regex module
import re
# passing a string value representing your regular expression to re.compile() returns a Regex object
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# A Regex object search() method searches the string it is passed for any matches to the regex
# if a pattern is found, the search() method returns a Match object, which will have a group() method that will return the actual matched text from the searched string
mo = phoneNumRegex.search('My number is 415-555-4242.')
# mo.group displays the whole match
print('Phone number found: ' + mo.group())
Phone number found: 415-555-4242
```

## Review of Regular Expression Matching
While there are several steps to using regular expressions in Python, each step is fairly simple.

1. Import the regex module with import _re_.
2. Create a Regex object with the re.comple() function. (Remember to use a raw string.)
3. Pass the string you want to search into the Regex object's search() method. This returns a Match object.
4. Call the Match object's group() method to return a string of the actual matched text.

Online tester: [pythex](https://pythex.org/)

## More Pattern Matching with Regular Expressions

### Grouping with Parentheses

Want to separate the area code fromthe rest of the phone number? Adding parenthesis will create _groups_ in the regex: (\d\d\d)-(\d\d\d-\d\d\d\d). Then you can use the _group()_ match object method to grab the matching text from just one group.

- Group 1: the first set of parenthesis
- Group 2: the second set of parenthesis

You can grab different parts of the matched text by passing an integer to the group() match object method. Passing 0 or nothing to the group() method will return the entire matched text.

```python
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1)
# '415'
mo.group(2)
# '555-4242'
mo.group()  
# '415-555-4242'
mo.groups()
# ('415', '555-4242')
areaCode, mainNumber = mo.groups() # multiple assignment trick
print(areaCode)
# 415
print(mainNumber)
# 555-4242
```

Q: What happens if you need to match a parenthesis?
A: escape the ( and ) characters with a backslash

```python
import re

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')  
mo = phoneNumRegex.search('My number is (415) 555-4242.')     
mo.group(1)
# '(415)'
```

If you receive an error message about "missing )" or "unbalanced parenthesis,"  you may have forgotten to include the closing unescaped parenthesis for a group.