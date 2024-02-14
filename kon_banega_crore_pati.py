'''This is how the lists created in this project -  'Questions', 'Options' and 'Answers' '''
'''lt = [["question1", ["o1", "o2", "o3", "o4"], "answer1"], ["question2", ["o1", "o2", "o3", "o4"], "answer2"]]'''


hardQuestions = [
    (
        '''What is the name of the technique that allows the user to move at nearly the speed of light?''',
        (
            '''Flying Thunder God Technique''',
            '''Body Flicker Technique''',
            '''Hiraishin Technique''',
            '''Shunshin no Jutsu''',
        ),
        '''Body Flicker Technique''',
    ),
    (
        '''Which Akatsuki member has the ability to control and manipulate paper for offensive and defensive purposes?''',
        ('''Deidara''', '''Hidan''', '''Konan''', '''Kisame'''),
        '''Konan''',
    ),
    (
        '''What is the name of the ninja tool that amplifies the user's chakra and abilities temporarily?''',
        ('''Chakra Pills''', '''Ninja Scrolls''', '''Chakra Armor''', '''Curse Mark Seal'''),
        '''Chakra Pills''',
    ),
    (
        '''Who is known as the 'Copy Ninja' and has the ability to copy any jutsu after seeing it once?''',
        ('''Jiraiya''', '''Kakashi Hatake''', '''Might Guy''', '''Hiruzen Sarutobi'''),
        '''Kakashi Hatake''',
    ),
    (
        '''Which of the Tailed Beasts is also known as the Three-Tails and is initially sealed within Yagura?''',
        ('''Matatabi''', '''Isobu''', '''Son Goku''', '''Shukaku'''),
        '''Isobu''',
    ),
    (
        '''What is the name of the genjutsu technique used by Itachi Uchiha that traps the opponent in an illusionary world?''',
        ('''Tsukuyomi''', '''Kotoamatsukami''', '''Izanagi''', '''Sharingan'''),
        '''Tsukuyomi''',
    ),
    (
        '''Who is the founder and leader of the village of the Hidden Rain?''',
        ('''Yahiko''', '''Hanzo''', '''Nagato''', '''Jiraiya'''),
        '''Yahiko''',
    ),
    (
        '''Which character is known for wielding the 'Samehada,' a sentient, sharkskin-covered sword?''',
        ('''Killer Bee''', '''Zabuza Momochi''', '''Suigetsu Hozuki''', '''Kisame Hoshigaki'''),
        '''Kisame Hoshigaki''',
    ),
    (
        '''What is the name of the forbidden jutsu that Orochimaru uses to transfer his consciousness into another person's body, achieving a form of immortality?''',
        (
            '''Edo Tensei''',
            '''Rinne Rebirth''',
            '''Cursed Seal Technique''',
            '''Living Corpse Reincarnation''',
        ),
        '''Living Corpse Reincarnation''',
    ),
    (
        '''Who is the creator of the Akatsuki organization and serves as its initial leader?''',
        ('''Madara Uchiha''', '''Kaguya Otsutsuki''', '''Obito Uchiha''', '''Yahiko'''),
        '''Yahiko''',
    ),
]

extremeQuestions = [
    (
        '''What is the name of the technique used by Minato Namikaze to teleport himself and others to a marked location instantaneously?''',
        (
            '''Space–Time Migration Technique''',
            '''Kamui''',
            '''Reverse Summoning Technique''',
            '''Edo Tensei''',
        ),
        '''Space–Time Migration Technique''',
    ),
    (
        '''Who is the original wielder of the sword known as "Kubikiribōchō"?''',
        ('''Mangetsu Hōzuki''', '''Zabuza Momochi''', '''Kisame Hoshigaki''', '''Raiga Kurosuki'''),
        '''Raiga Kurosuki''',
    ),
    (
        '''What is the name of the creature summoned by Jiraiya using the Summoning Technique during the battle against Pain?''',
        ('''Gamakichi''', '''Gamabunta''', '''Gamaken''', '''Gamahiro'''),
        '''Gamaken''',
    ),
    (
        '''Who possesses the Kekkei Genkai known as "Lava Release" in the Akatsuki organization?''',
        ('''Deidara''', '''Itachi Uchiha''', '''Kakuzu''', '''Kurotsuchi'''),
        '''Kurotsuchi''',
    ),
    (
        '''In the Fourth Great Ninja War, what technique does Naruto use to form an alliance with Kurama, the Nine-Tails?''',
        ('''Sage Art: Lava Rasengan''', '''Tailed Beast Ball''', '''Tailed Beast Chakra Arms''', '''Tailed Beast Rasengan'''),
        '''Tailed Beast Chakra Arms''',
    ),
]

price_list = [5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 30000000, 50000000, 70000000]

hardQuestions = hardQuestions + extremeQuestions

correctAns = 0
priceMoney = 0


def takingInput():
    while True:
        try:
            user_input = int(input("Enter your choice to lock the answer : "))
            if 1<= user_input <=4:
                return user_input
            else:
                print("Enter A Valid Option Number !!!")
        except ValueError:
            print("Enter A Valid Option Number !!!")


def validate_YesOrNo(optionNumber, option):
    while True:
        
        try:
            user_input = input(f"\nKya Aap Option Number ({optionNumber}) ({option}) Ko Lock Karna Chahte Hai?\nType 'y' for 'yes' or 'n' for 'no' : ")
            
            if user_input.lower() == 'y':
                print(f"\nComputer Ji Option Number ({optionNumber}) ({option}) Par Taala Lagaya Jaye")
                return True
            elif user_input.lower() == 'n':
                return False
            else:
                print("Enter Y/N !!!")
        except j:
            print("Enter Y/N !!!")


"""Loop through each question"""
for i, (question, option, answer) in zip(range(1, len(hardQuestions)+1), hardQuestions):
    print(f"\n~~Savaal Number ({i}) Pure ({price_list[i-1]}) Rupay Ke Liye Apki Computer Screen Par Ye Raha~~\n")
    print(f"Q{i}.) ", question)
    
    """Display question options"""
    for j in range(1,5):
        print(f"\tOption {j}) {option[j - 1]}")
    print()
    
    """Get and validate user input"""
    while True:
        userChoice = takingInput()
        shouldContinue = validate_YesOrNo(userChoice, option[userChoice - 1])
        if shouldContinue:
            break            
    print()
    
    """Check user's answer and provide feedback"""
    if answer == option[userChoice - 1]:
        correctAns += 1
        priceMoney = price_list[i-1]
        print("-"*100)
        print(f"Sahi Jawaab!!!\n Or Isi Ke Sath Aap Jitte hai ({priceMoney}) rupay")
        print("-"*100)
        print("\n~~Khela Ko Aage Badhate Huye Agla Savaal~~",end="")
    else:
        print("-"*100)
        print(f"Galat Jawaab\nIs Savaal Ka Sahi Javab Hai : Option Number ({option.index(answer)}) ({answer})")
        print(f"Or Isi Ke Saath Apka Khela Yahi Samapt Hota Hai Or Aap Jitte Hai ({priceMoney}) Rupay Ki Dhanrashi")
        print("-"*100)
        break
    

print("\n\nYour Total Correct Answers are : ", correctAns)
print("You win", priceMoney)

if priceMoney == 70000000:
    print("!!!!!!!!!!!!!!!!!!!!!!!! SAAAAT KARROOOOD !!!!!!!!!!!!!!!!!!!!!!!!".center(125))
