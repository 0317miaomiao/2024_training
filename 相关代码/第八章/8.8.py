def make_album(artist_name, album_name, songs_num=None):
    album_dict = {'artist': artist_name, 'album': album_name}
    if songs_num:
        album_dict['songs_num'] = songs_num
    return album_dict

# 创建一个无限循环来获取用户输入
while True:
    print("\nPlease enter the artist name and album name:")
    print("(enter 'q' at any time to quit)")
    
    artist_name = input("Artist name: ")
    # 如果用户输入'q'，则退出循环
    if artist_name == 'q':
        break
    
    album_name = input("Album name: ")
    # 如果用户输入'q'，则退出循环
    if album_name == 'q':
        break
    
    # 可选：让用户输入歌曲数
    songs_num = input("Number of songs (optional): ")
    if songs_num == 'q':
        break
    # 如果用户没有输入歌曲数，则调用不带songs_num的函数版本
    if songs_num:
        album_dict = make_album(artist_name, album_name, int(songs_num))
    else:
        album_dict = make_album(artist_name, album_name)
    
    print(album_dict)
