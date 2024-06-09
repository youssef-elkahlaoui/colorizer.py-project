import PySimpleGUI as sg
from gui import create_window, update_window
from colorizer import load_model, colorize_image
import os

def main():
    net, pts = load_model()
    window = create_window()
    
    prev_filename = colorized = None
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        prev_filename, colorized = update_window(event, values, window, net, prev_filename, colorized)

    window.close()

if __name__ == "__main__":
    main()
