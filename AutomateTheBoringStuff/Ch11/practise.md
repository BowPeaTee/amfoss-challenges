1. assert spam>=10, 'spam is less than 10'
2. assert eggs.lower() != bacon.lower(), 'eggs and bacon contain the same string'
3. assert False, 'This is always triggered'
4. import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -
%(levelname)s -  %(message)s')
5. import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG,
format=' %(asctime)s -  %(levelname)s -  %(message)s')
6. DEBUG, INFO, WARNING, ERROR and CRITICAL
7. logging.disable(logging.CRITICAL)
8. You will have to spend some time removing the print lines after debugging. You might end up removing necessary print functions. You can easily disable logging messages without removing their lines. Logging also shows more information. 
9. Step In will take the debugger into a function call. Step Over will quickly execute the function call without stepping into it. The Step Out button will quickly execute the rest of the code in the function it is in.
10. Debugger will stop when its reached the end of the program or a breakpoint.
11. A breakpoint is a toggle on a line that ensures that the debugger will pause when that line is executed.
12. Click the line number to make a red dot appear.
