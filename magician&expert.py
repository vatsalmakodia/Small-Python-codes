is_magician = True
is_expert = True

# to check if magician and expert
if is_magician and is_expert:
    print('You are a Master Magician')

# to check if magician only
elif is_magician and not is_expert:
    print('At least you are getting there')

elif not is_magician:
    print('You need magic powers')

