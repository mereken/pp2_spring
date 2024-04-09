# import pygame
# clock = pygame.time.Clock()
# pygame.init()

# screen = pygame.display.set_mode((900 , 512)) #size of display
# pygame.display.set_caption("Player") #the name of display
# player = pygame.image.load("Lab7/ex2/images/player.jpg") #main object
# process = True #for cycle "for"
# playlist = ["Lab7/ex2/music/music1.mp3", "Lab7/ex2/music/music2.mp3" , "Lab7/ex2/music/music3.mp3"] #list of musics
# index_of_playlist = 0
# def play_music():
#     pygame.mixer.music.load(playlist[index_of_playlist])
#     pygame.mixer.music.play()
# def stop_music():
#     pygame.mixer.music.stop()
# def next_track():
#     global index_of_playlist
#     index_of_playlist = (index_of_playlist + 1) % len(playlist)
#     play_music()
# def previous_track():
#     global index_of_playlist
#     index_of_playlist = (index_of_playlist - 1) % len(playlist)
#     play_music()
# while process :
#     pygame.display.update()
#     screen.blit(player , (0 , 0))
#     for event in pygame.event.get():
#         if  event.type == pygame.QUIT:
#             process = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 play_music()
#             elif event.key == pygame.K_TAB:
#                 stop_music()
#             elif event.key == pygame.K_RIGHT:
#                 next_track()
#             elif event.key == pygame.K_LEFT:
#                 previous_track()

# pygame.display.flip()
# clock.tick(10)
# pygame.quit()


import pygame

pygame.init()
pygame.mixer.init()

def play_another_song():
    global currently_playing_song, songs, current_song_index
    next_song_index = (current_song_index + 1) % len(songs)
    currently_playing_song = songs[next_song_index]
    pygame.mixer.music.load(currently_playing_song)
    pygame.mixer.music.play()
    current_song_index = next_song_index

def play_previous_song():
    global currently_playing_song, songs, current_song_index
    previous_song_index = (current_song_index - 1) % len(songs)
    currently_playing_song = songs[previous_song_index]
    pygame.mixer.music.load(currently_playing_song)
    pygame.mixer.music.play()
    current_song_index = previous_song_index

def stop_music():
    pygame.mixer.music.stop()

def play_pause_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

window_width = 600
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
songs = ['ONF.mp3', 'Atlantis.mp3','Iracus.mp3']
current_song_index = 0
currently_playing_song = songs[current_song_index]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_pause_music()
            elif event.key == pygame.K_RIGHT:  # Next song
                play_another_song()
            elif event.key == pygame.K_LEFT:   # Previous song
                play_previous_song()
            elif event.key == pygame.K_s:      # Stop music
                stop_music()

    window.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
