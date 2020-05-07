import cv2
# excpected output: 900x534 jpg file

def editThumbnail(cover_filepath, artist, title, player, player_avatar_path):

    # resizing, blurring, and applying grayscale to background image
    scale = 534/250
    tn = cv2.imread(cover_filepath)
    height, width = (round(tn.shape[0] * scale), round(tn.shape[1] * scale))
    tn = cv2.resize(tn, (width, height))
    tn = tn[0:height, 0:900]
    tn = cv2.blur(tn, (16, 16))
    tn = cv2.cvtColor(tn, cv2.COLOR_BGR2GRAY)
    tn = cv2.cvtColor(tn, cv2.COLOR_GRAY2BGR)
    tn = cv2.flip(tn, 1)

    # adding cover to background
    cover = cv2.imread(cover_filepath)
    tn[0:250, 0:900] = cover

    # adding text
    artistXY = (10, 300)
    titleXY = (10, 400)

    cv2.putText(tn, artist, artistXY, cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255,255,255), 1)
    cv2.putText(tn, title, titleXY, cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255,255,255), 2)

    cv2.imshow('test thumbnail', tn)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# testing purposes
# editPhoto('cover.jpg', 'Very long Arist name for testing', 'Road of Resistance', 'Spare', 'player_avatar.jpg')