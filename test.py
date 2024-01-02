import pygame

pygame.init()

# Load the sound file
pygame.mixer.Sound('Audio\SICK_ASS_RIFF.mp3').play()  # Replace 'sound_file.wav' with your sound file path

# Play the sound

# Keep the program running to allow the sound to play
while pygame.mixer.get_busy():
    pygame.time.Clock().tick(10)  # Adjust the ticks per second as needed

pygame.quit()
