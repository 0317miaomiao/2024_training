# 定义函数，其中songs_num参数有一个默认值None
def make_album(artist_name, album_name, songs_num=None):
    album_dict = {'artist': artist_name, 'album': album_name}
    if songs_num:
        album_dict['songs_num'] = songs_num
    return album_dict

# 使用函数创建三个字典，并打印每个字典以核实信息
album1 = make_album('Taylor Swift', 'Folklore')
album2 = make_album('Billie Eilish', 'When We All Fall Asleep, Where Do We Go?')
album3 = make_album('Ed Sheeran', 'Divide', songs_num=16)

print(album1)
print(album2)
print(album3)

# 进行一次调用，指定专辑包含的歌曲数
album4 = make_album('Ariana Grande', 'Thank U, Next', songs_num=12)
print(album4)
