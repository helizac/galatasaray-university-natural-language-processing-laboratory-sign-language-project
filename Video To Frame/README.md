Required File Layout :

    - gesture_folder
        - a
            - video1.mp4
            - video2.mp4
            ...
        - b
        ...
        
Output File Structure :

    - target_folder
        - a
            - video1
                - video1_frame_1.jpeg
                - video1_frame_2.jpeg
                ...
            - video2
            ...
        - b
        ...   

How the file works :

    On Terminal :

        python3 video-to-frame.py gesture_folder target_folder

        # In case there is a problem with your library versions
        python video-to-frame.py gesture_folder target_folder
