1. re.compile()
2. so that escape characters needn't be used.
3. Match objects
4. group()
5. group 0 covers the whole match, whereas 1 and 2 returns the first and second set of parantheses.
6. escape characters, preceding them with backslash
7. If regex has no groups, a list of strings is returned. If the regex has groups, a list of tuples of strings is returned.
8. | signifies that either the preceding or succeeding group should match, not both or neither at the same time.
9. ? can either mean to match zero or one of the preceding group, or to indicate non-greedy matching.
10. + means one or more, while * means zero or more of the preceding group.
11. {3} means exactly three instances of the preceding group. The {3,5} means between three and five instances.
12. Single digit, word or space character respectively.
13. Not a single digit, word or space character respectively.
14. .* performs a greedy match, and the .*? performs a non-greedy match.
15. [a-z0-9] 
16. passing re.IGNORECASE as second argument in the re.compile() function
17. . usually matches any character that isn't a newline character. When re.DOTALL is passed, it matches newline characters too.
18. X drummers, X pipers, five rings, X hens
19. It allows you to add whitespace and comments to the string passed to re.compile()
20. re.compile(r'\d{1,3}(,\d{3})*')
21. re.compile(r'[A-Z][a-zA-Z]*\sWatanabe')
22. re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs).', re.IGNORECASE)