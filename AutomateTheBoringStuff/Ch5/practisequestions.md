1. {}
2. {'foo':42}
3. Items stored in a dictionary are unordered, where in list it is ordered.
4. KeyError is recieved.
5. There is no difference. Both code checks if 'cat' is present in spam as a key.
6. 'cat' in spam checks if 'cat' is present in spam as a key, whereas 'cat' in spam.values() checks if there is a key for which 'cat' is the value.
7. spam.setdefault('color','black')
8. pprint and pprint()