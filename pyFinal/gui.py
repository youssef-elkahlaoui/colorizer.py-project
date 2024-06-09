import PySimpleGUI as sg
import cv2
import os
from utils import convert_to_grayscale, resize_image
from colorizer import colorize_image

version = '27 May 2024'
FIXED_SIZE = (300, 300)  # Define the fixed image size

def create_window():
    left_col = [[sg.Text('Folder'), sg.In(size=(25, 1), enable_events=True, key='-FOLDER-'), sg.FolderBrowse()],
                
                [sg.Listbox(values=[], enable_events=True, size=(40, 20), key='-FILE LIST-')],
                [sg.CBox('Convert to gray first', key='-MAKEGRAY-')],
                [sg.Text('Version ' + version, font='Courier 8')]]

    images_col = [[sg.Text('Input file:'), sg.In(enable_events=True, key='-IN FILE-'), sg.FileBrowse()],
                  [sg.Button('Colorize Photo', key='-PHOTO-'), sg.Button('Save File', key='-SAVE-'), sg.Button('Exit')],
                  [sg.Image(filename='', key='-IN-'), sg.Image(filename='', key='-OUT-')]]

    layout = [[sg.Column(left_col), sg.VSeperator(), sg.Column(images_col)]]
    window = sg.Window('Photo Colorizer', layout, grab_anywhere=True)
    return window

def update_window(event, values, window, net, prev_filename, colorized):
    if event == '-FOLDER-':
        folder = values['-FOLDER-']
        img_types = (".png", ".jpg", "jpeg", ".tiff", ".bmp")
        try:
            flist0 = os.listdir(folder)
        except:
            return prev_filename, colorized
        fnames = [f for f in flist0 if os.path.isfile(
            os.path.join(folder, f)) and f.lower().endswith(img_types)]
        window['-FILE LIST-'].update(fnames)
    elif event == '-FILE LIST-':
        try:
            filename = os.path.join(values['-FOLDER-'], values['-FILE LIST-'][0])
            image = cv2.imread(filename)
            image_resized = resize_image(image, FIXED_SIZE)
            window['-IN-'].update(data=cv2.imencode('.png', image_resized)[1].tobytes())
            window['-OUT-'].update(data='')
            window['-IN FILE-'].update('')

            if values['-MAKEGRAY-']:
                gray_3_channels = convert_to_grayscale(image)
                gray_resized = resize_image(gray_3_channels, FIXED_SIZE)
                window['-IN-'].update(data=cv2.imencode('.png', gray_resized)[1].tobytes())
                image, colorized = colorize_image(net, cv2_frame=gray_3_channels)
            else:
                image, colorized = colorize_image(net, filename)
            
            colorized_resized = resize_image(colorized, FIXED_SIZE)
            window['-OUT-'].update(data=cv2.imencode('.png', colorized_resized)[1].tobytes())
        except:
            return prev_filename, colorized
    elif event == '-PHOTO-':
        try:
            if values['-IN FILE-']:
                filename = values['-IN FILE-']
            elif values['-FILE LIST-']:
                filename = os.path.join(values['-FOLDER-'], values['-FILE LIST-'][0])
            else:
                return prev_filename, colorized
            if values['-MAKEGRAY-']:
                gray_3_channels = convert_to_grayscale(cv2.imread(filename))
                gray_resized = resize_image(gray_3_channels, FIXED_SIZE)
                window['-IN-'].update(data=cv2.imencode('.png', gray_resized)[1].tobytes())
                image, colorized = colorize_image(net, cv2_frame=gray_3_channels)
            else:
                image, colorized = colorize_image(net, filename)
                image_resized = resize_image(image, FIXED_SIZE)
                window['-IN-'].update(data=cv2.imencode('.png', image_resized)[1].tobytes())
            
            colorized_resized = resize_image(colorized, FIXED_SIZE)
            window['-OUT-'].update(data=cv2.imencode('.png', colorized_resized)[1].tobytes())
        except:
            return prev_filename, colorized
    elif event == '-IN FILE-':
        filename = values['-IN FILE-']
        if filename != prev_filename:
            prev_filename = filename
            try:
                image = cv2.imread(filename)
                image_resized = resize_image(image, FIXED_SIZE)
                window['-IN-'].update(data=cv2.imencode('.png', image_resized)[1].tobytes())
            except:
                return prev_filename, colorized
    elif event == '-SAVE-' and colorized is not None:
        filename = sg.popup_get_file('Save colorized image.\nColorized image be saved in format matching the extension you enter.', save_as=True)
        try:
            if filename:
                cv2.imwrite(filename, colorized)
                sg.popup_quick_message('Image save complete', background_color='red', text_color='white', font='Any 16')
        except:
            sg.popup_quick_message('ERROR - Image NOT saved!', background_color='red', text_color='white', font='Any 16')
    
    return prev_filename, colorized
