import hw2


def test_question1():
    text = 'Wings, horns, hooves? What are we saying? Is this Diablo?'          # change me with input
    key = 15                                                                    # change me with input
    correct_ans = 'Lxcvh, wdgch, wddkth? Lwpi pgt lt hpnxcv? Xh iwxh Sxpqad?'   # change me with correct output
    my_ans = hw2.encrypt(text, key)
    if my_ans == correct_ans:
        print('test 1 passed')
    else:
        print('test 1 failed')


def test_question2():
    text = 'J vtfe up cf bo bewfouvsfs mjlf zpv, uifo J uppl bo bsspx up uif loff.'             # change me with input
    key = 1                                                                                     # change me with input
    correct_ans = 'I used to be an adventurer like you, then I took an arrow to the knee.'      # change me with correct output
    my_ans = hw2.decrypt(text, key)
    if my_ans == correct_ans:
        print('test 2 passed')
    else:
        print('test 2 failed')


def test_question3():
    text = 'Dbkho kxihkmbgz.'                                              # change me with input
    correct_ans = ['Dbkho kxihkmbgz.', 'Cajgn jwhgjlafy.',
                   'Bzifm ivgfikzex.', 'Ayhel hufehjydw.',
                   'Zxgdk gtedgixcv.', 'Ywfcj fsdcfhwbu.',
                   'Xvebi ercbegvat.', 'Wudah dqbadfuzs.',
                   'Vtczg cpazcetyr.', 'Usbyf bozybdsxq.',
                   'Traxe anyxacrwp.', 'Sqzwd zmxwzbqvo.',
                   'Rpyvc ylwvyapun.', 'Qoxub xkvuxzotm.',
                   'Pnwta wjutwynsl.', 'Omvsz vitsvxmrk.',
                   'Nlury uhsruwlqj.', 'Mktqx tgrqtvkpi.',
                   'Ljspw sfqpsujoh.', 'Kirov reporting.',
                   'Jhqnu qdonqshmf.', 'Igpmt pcnmprgle.',
                   'Hfols obmloqfkd.', 'Genkr nalknpejc.',
                   'Fdmjq mzkjmodib.', 'Eclip lyjilncha.']                # change me with correct output
    my_ans = hw2.naive_break(text)
    if my_ans == correct_ans:
        print('test 3 passed')
    else:
        print('test 3 failed')


def test_question4a():
    text = 'Knowing the mouse might one day leave its hole and get the cheese... It fills you with DETERMINATION!'     # change me with input
    correct_ans = 'e'                                                                                                  # change me with correct output
    my_ans = hw2.find_common_letter(text)
    if my_ans == correct_ans:
        print('test 4a passed')
    else:
        print('test 4a failed')


def test_question4b():
    text = 'Bpqa qa ug abwzg, vwb gwcza. Gwc ucab tmb um nqvqap bmttqvo qb.'                                            # change me with input
    common_letter = 't'                                                                                                 # change me with input
    correct_ans = 'This is my story, not yours. You must let me finish telling it.'                                     # change me with correct output
    my_ans = hw2.frequency_break(text, common_letter)
    if my_ans == correct_ans:
        print('test 4b passed')
    else:
        print('test 4b failed')


if __name__ == '__main__':
    test_question1()
    test_question2()
    test_question3()
    test_question4a()
    test_question4b()