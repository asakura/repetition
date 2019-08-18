# Regex[Python 3]

## Introduction
-   [x] [Matching Specific String](https://www.hackerrank.com/challenges/matching-specific-string) solution: ```/hackerrank/``` 
-   [x] [Matching Anything But a Newline](https://www.hackerrank.com/challenges/matching-anything-but-new-line) solution: ```/^.{3}\..{3}\..{3}\..{3}$/```
-   [x] [Matching Digits & Non-Digit Characters](https://www.hackerrank.com/challenges/matching-digits-non-digit-character) solution: ```/\d\d\D\d\d\D\d{4}/```
-   [x] [Matching Whitespace & Non-Whitespace Character](https://www.hackerrank.com/challenges/matching-whitespace-non-whitespace-character) solution: ```/\S\S\s\S\S\s\S\S/```
-   [x] [Matching Word & Non-Word Character](https://www.hackerrank.com/challenges/matching-word-non-word) solution: ```/\w{3}\W\w{10}\W\w{3}/```
-   [x] [Matching Start & End](https://www.hackerrank.com/challenges/matching-start-end) solution: ```/^\d\w{4}\.$/```

## Character Class
-   [x] [Matching Specific Characters](https://www.hackerrank.com/challenges/matching-specific-characters) solution: ```/^[123][120][xs0][30Aa][xsu][.,]$/```
-   [x] [Excluding Specific Characters](https://www.hackerrank.com/challenges/excluding-specific-characters) solution: ```/^\D[^aeiou][^bcDF]\S[^AEIOU][^.,]$/```
-   [x] [Matching Character Ranges](https://www.hackerrank.com/challenges/matching-range-of-characters) solution: ```/^[a-z][1-9][^a-z][^A-Z][A-Z]/```

## Repetitions
-   [x] [Matching {x} Repetitions](https://www.hackerrank.com/challenges/matching-x-repetitions) solution: ```/^[a-zA-Z02468]{40}[\s13579]{5}$/```
-   [x] [Matching {x, y} Repetitions](https://www.hackerrank.com/challenges/matching-x-y-repetitions) solution: ```/^\d{1,2}[a-zA-Z]{3,}\.{0,3}$/```
-   [x] [Matching Zero Or More Repetitions](https://www.hackerrank.com/challenges/matching-zero-or-more-repetitions) solution: ```/^\d{2,}[a-z]*[A-Z]*$/```
-   [x] [Matching One Or More Repetitions](https://www.hackerrank.com/challenges/matching-one-or-more-repititions) solution: ```/^\d+[A-Z]+[a-z]+$/```
-   [x] [Matching Ending Items](https://www.hackerrank.com/challenges/matching-ending-items) solution: ```/^[a-zA-Z]*s$/```

## Grouping and Capturing
-   [x] [Matching Word Boundaries](https://www.hackerrank.com/challenges/matching-word-boundaries) solution: ```/\b[aeiouAEIOU][a-zA-Z]*\b/```
-   [x] [Capturing & Non-Capturing Groups](https://www.hackerrank.com/challenges/capturing-non-capturing-groups) solution: ```/(?:ok){3,}/```
-   [x] [Alternative Matching](https://www.hackerrank.com/challenges/alternative-matching) solution: ```/^(Mr|Mrs|Ms|Dr|Er)\.[a-zA-Z]+$/```

## Backreferences
-   [x] [Matching Same Text Again & Again](https://www.hackerrank.com/challenges/matching-same-text-again-again) solution: ```/^([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-Z])([aeiouAEIOU])(\S)\1\2\3\4\5\6\7\8\9\10$/```
-   [x] [Backreferences To Failed Groups](https://www.hackerrank.com/challenges/backreferences-to-failed-groups) solution: ```/^\d\d(-?)\d\d\1\d\d\1\d\d$/```
-   [x] [Branch Reset Groups](https://www.hackerrank.com/challenges/branch-reset-groups) solution: ```/^\d\d(?|(---)|(-)|(\.)|(:))\d\d\1\d\d\1\d\d$/```
-   [x] [Forward References](https://www.hackerrank.com/challenges/forward-references) solution: ```/^(\2tic|(tac))+$/```

## Assertions
-   [x] [Positive Lookahead](https://www.hackerrank.com/challenges/positive-lookahead) solution: ```/o(?=oo)/```
-   [x] [Negative Lookahead](https://www.hackerrank.com/challenges/negative-lookahead) solution: ```/(.)(?!\1)/```
-   [x] [Positive Lookbehind](https://www.hackerrank.com/challenges/positive-lookbehind) solution: ```/(?<=[13579])\d/```
-   [x] [Negative Lookbehind](https://www.hackerrank.com/challenges/negative-lookbehind) solution: ```/(?<![aeiouAEIOU])./```

## Applications
-   [x] [Detect HTML Links](https://www.hackerrank.com/challenges/detect-html-links) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/Detect HTML Links/solution.py>)
-   [x] [Detect HTML Tags](https://www.hackerrank.com/challenges/detect-html-tags) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/Detect HTML Tags/solution.py>)
-   [x] [Find A Sub-Word](https://www.hackerrank.com/challenges/find-substring) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/Find A Sub-Word/solution.py>)
-   [x] [Alien Username](https://www.hackerrank.com/challenges/alien-username) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/Alien Username/solution.py>)
-   [x] [IP Address Validation](https://www.hackerrank.com/challenges/ip-address-validation) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/IP Address Validation/solution.py>)
-   [x] [Find a Word](https://www.hackerrank.com/challenges/find-a-word) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/Find a Word/solution.py>)
-   [x] [Detect the Email Addresses](https://www.hackerrank.com/challenges/detect-the-email-addresses) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/Detect the Email Addresses/solution.py>)
-   [x] [Detect the Domain Name](https://www.hackerrank.com/challenges/detect-the-domain-name) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/Detect the Domain Name/solution.py>)
-   [x] [Building a Smart IDE: Identifying comments](https://www.hackerrank.com/challenges/ide-identifying-comments) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/Building a Smart IDE: Identifying comments/solution.py>)
-   [x] [Detecting Valid Latitude and Longitude Pairs](https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/Detecting Valid Latitude and Longitude Pairs/solution.py>)
-   [x] [HackerRank Tweets](https://www.hackerrank.com/challenges/hackerrank-tweets) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/HackerRank Tweets/solution.py>)
-   [x] [Build a Stack Exchange Scraper](https://www.hackerrank.com/challenges/stack-exchange-scraper) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/Build a Stack Exchange Scraper/solution.py>)
-   [x] [Utopian Identification Number](https://www.hackerrank.com/challenges/utopian-identification-number) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/Utopian Identification Number/solution.py>)
-   [x] [Valid PAN format](https://www.hackerrank.com/challenges/valid-pan-format) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/Valid PAN format/solution.py>)
-   [x] [Find HackerRank](https://www.hackerrank.com/challenges/find-hackerrank) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/Find HackerRank/solution.py>)
-   [x] [Saying Hi](https://www.hackerrank.com/challenges/saying-hi) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/Saying Hi/solution.py>)
-   [x] [HackerRank Language](https://www.hackerrank.com/challenges/hackerrank-language) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/HackerRank Language/solution.py>)
-   [x] [Building a Smart IDE: Programming Language Detection](https://www.hackerrank.com/challenges/programming-language-detection) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/Building a Smart IDE: Programming Language Detection/solution.py>)
-   [x] [Split the Phone Numbers](https://www.hackerrank.com/challenges/split-number) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/Split the Phone Numbers/solution.py>)
-   [x] [Detect HTML Attributes](https://www.hackerrank.com/challenges/html-attributes) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/Detect HTML Attributes/solution.py>)
-   [x] [The British and American Style of Spelling](https://www.hackerrank.com/challenges/uk-and-us) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/The British and American Style of Spelling/solution.py>)
-   [x] [UK and US: Part 2](https://www.hackerrank.com/challenges/uk-and-us-2) solution: [Python 3](<https://github.com/asakura/repetition/blob/master/hackerrank/Regex/UK and US: Part 2/solution.py>)
