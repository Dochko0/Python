post_dict = {}

while True:
    line = input()
    if line == 'drop the media':
        break

    line = line.split()

    post = line[1]
    move = line[0]

    if move == 'post':
            post_dict[post] = {
                'Likes': 0,
                'Dislikes': 0,
                'Comments': []
            }
    elif move == 'like' and post in post_dict:
            post_dict[post]['Likes'] += 1
    elif move == 'dislike' and post in post_dict:
            post_dict[post]['Dislikes'] += 1
    elif move == 'comment' and post in post_dict:
            post_dict[post]['Comments'].append(f'{line[2]}: {" ".join(line[3:])}')


for x in post_dict:
    print(f'Post: {x} | Likes: {post_dict[x]["Likes"]} | Dislikes: {post_dict[x]["Dislikes"]}')
    print('Comments:')
    if not post_dict[x]['Comments']:
        print("None")
    else:
        for z in post_dict[x]['Comments']:
            print(f'*  {z}')