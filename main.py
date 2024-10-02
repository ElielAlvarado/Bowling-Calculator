first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
user_age = input('Enter your age: ')

user_name = first_name[0] + last_name + user_age
user_name = user_name.lower()

first_bowling = int(input('Enter your first bowling score: '))
if first_bowling < 0:
    print('Invalid Score - Positive Scores Only!')
    quit()
elif first_bowling > 300:
    print('Invalid Score - Only Scores Lower Than 300!')
    quit()

second_bowling = int(input('Enter your second bowling score: '))
if second_bowling < 0:
    print('Invalid Score - Positive Scores Only!')
    quit()
elif second_bowling > 300:
    print('Invalid Score - Only Scores Lower Than 300!')
    quit()

third_bowling = int(input('Enter your third bowling score: '))
if third_bowling < 0:
    print('Invalid Score - Positive Scores Only!')
    quit()
elif third_bowling > 300:
    print('Invalid Score - Only Scores Lower Than 300!')
    quit()

avg_score = (first_bowling + second_bowling + third_bowling) / 3
avg_score = round(avg_score)
skill_level = ''
if 0 <= avg_score < 90:
    skill_level= 'Beginner'
elif 90 <= avg_score <= 184:
    skill_level = 'Intermediate'
elif 185 <= avg_score <= 300:
    skill_level = 'Advanced'

print(f'Hello {first_name} {last_name}! Your username is {user_name}, your average bowling score is {avg_score}.\nThat means that you\'ve achieved an {skill_level} skill level. Great Job and keep up the practice!')
