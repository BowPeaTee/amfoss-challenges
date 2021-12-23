import random, time, pyinputplus as pyip

questions = 10
correct = 0

for qNo in range(questions):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    prompt = '#%s: %s x %s = ' % (qNo, n1, n2)

    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (n1*n2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)

    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')

    else:
        print('Correct!')
        correct+=1
        time.sleep(1)

print('Score: %s / %s' % (correct, questions))                           