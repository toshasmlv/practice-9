import pygame
import os
import sys
pygame.init()
pygame.mixer.init()

music_folder = 'music'
songs = [os.path.join(music_folder, f) for f in os.listdir(music_folder) 
         if f.endswith(('.mp3', '.wav'))]

durations = []
for song in songs:
    durations.append(pygame.mixer.Sound(song).get_length())

screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Keyboard Music Player")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)

font = pygame.font.SysFont(None, 36)
font_small = pygame.font.SysFont(None, 28)

music_index = 0
num_songs = len(songs)
current_times = 0
is_paused = False
done = False

clock = pygame.time.Clock()

pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)


def play_track():
    global current_times, is_paused
    pygame.mixer.music.load(songs[music_index])
    pygame.mixer.music.play()
    current_times = 0
    is_paused = False

def format_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    if h > 0:
        return font_small.render(f"{h}:{m:02}:{s:02}", True, BLACK)
    return font_small.render(f"{m:02}:{s:02}", True, BLACK)

while not done:
    screen.fill(WHITE)
    
    if pygame.mixer.music.get_busy() and not is_paused:
        current_times = pygame.mixer.music.get_pos() / 1000

    duration = durations[music_index]
    progress_ratio = min(current_times / duration, 1.0) if duration > 0 else 0
    circle_x = 200 + progress_ratio * 850  

    song_name = os.path.basename(songs[music_index])
    name_surface = font.render(f"Now Playing: {song_name}", True, RED)
    screen.blit(name_surface, (50, 20))

    
    controls = [
        'CONTROLS:',
        'P = Play / Unpause', 
        'S = Pause', 
        'N = Next track', 
        'B = Previous track', 
        'Q = Quit'
    ]
    for i, text in enumerate(controls):
        color = BLACK if i == 0 else (100, 100, 100)
        
    screen.blit(font.render("PLAYLIST:", True, BLACK), (400, 80))
    for i, s in enumerate(songs):
        s_name = os.path.basename(s)
        color = RED if i == music_index else BLACK
        col_offset = 400 if i < 12 else 800
        row_offset = 120 + (i % 12) * 30
        screen.blit(font_small.render(f'{i+1}. {s_name}', True, color), (col_offset, row_offset))

    pygame.draw.line(screen, GRAY, (200, 600), (1050, 600), 4) # Фон полосы
    pygame.draw.line(screen, RED, (200, 600), (circle_x, 600), 4) # Прогресс
    pygame.draw.circle(screen, RED, (int(circle_x), 600), 10) # Шарик

    
    screen.blit(format_time(current_times), (130, 590))
    screen.blit(format_time(duration), (1070, 590))

    status = "PAUSED" if is_paused else ("PLAYING" if pygame.mixer.music.get_busy() else "STOPPED")
    screen.blit(font.render(status, True, RED if status != "PLAYING" else BLACK), (560, 630))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
                
            elif event.key == pygame.K_p:
                if is_paused:
                    pygame.mixer.music.unpause()
                    is_paused = False
                elif not pygame.mixer.music.get_busy():
                    play_track()
                    
            elif event.key == pygame.K_s:
                pygame.mixer.music.pause()
                is_paused = True
                
            elif event.key == pygame.K_n:
                music_index = (music_index + 1) % num_songs
                play_track()
                
            elif event.key == pygame.K_b:
                music_index = (music_index - 1) % num_songs
                play_track()
                
        elif event.type == pygame.USEREVENT + 1:
            music_index = (music_index + 1) % num_songs
            play_track()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()