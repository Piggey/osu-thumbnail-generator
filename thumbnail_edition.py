import cv2
# excpected output: 900x534 jpg file

def editThumbnail(cover_filepath, artist, title, player, diffname, player_avatar_path):

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
    # cover = addRoundedRectangleBorder(cover)
    tn[0:250, 0:900] = cover

    # adding player avatar
    avatar = cv2.imread(player_avatar_path)
    avatar = cv2.resize(avatar, (128, 128))
    tn[260:388, 386:514] = avatar

    # adding text
    artistXY = (8, 160)
    titleXY = (5, 240)
    playerXY = (width/2, height/2)
    diffXY = (250, 250)

    cv2.putText(tn, artist, artistXY, cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 0), 2)
    cv2.putText(tn, artist, artistXY, cv2.FONT_HERSHEY_SIMPLEX, 1.6, (240, 240, 240), 1)

    cv2.putText(tn, title, titleXY, cv2.FONT_HERSHEY_SIMPLEX, 2.6, (0, 0, 0), 4)
    cv2.putText(tn, title, titleXY, cv2.FONT_HERSHEY_SIMPLEX, 2.6, (240, 240, 240), 2)

    cv2.putText(tn, player, playerXY, cv2.FONT_HERSHEY_SIMPLEX, 2.4, (0, 0, 0), 3)
    cv2.putText(tn, player, playerXY, cv2.FONT_HERSHEY_SIMPLEX, 2.4, (255, 255, 255), 1)

    # cv2.imshow('test thumbnail', tn)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.imwrite(f'thumbnails/{artist} - {title} ({player}).jpg', tn)

# testing purposes
editThumbnail('cover.jpg', 'big gay', 'Road of Resistance', 'Spare', '[Lapse]', 'player_avatar.jpg')