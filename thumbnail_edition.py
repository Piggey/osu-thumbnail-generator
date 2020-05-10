import cv2
from os import mkdir
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
    black = (0, 0, 0)
    white = (255, 255, 255)
    font = cv2.FONT_HERSHEY_SIMPLEX
    artistScale = 2
    titleScale = 2.2
    playerSize = cv2.getTextSize(player, font, 2.6, 3)[0]
    diffSize = cv2.getTextSize(diffname, font, 1.8, 3)[0]

    artistXY = (8, 140)
    titleXY = (5, 230)
    playerXY = ((tn.shape[1] - playerSize[0]) // 2, ((tn.shape[0] + playerSize[1]) // 2) + 160)
    diffXY = ((tn.shape[1] -  diffSize[0]), 60)

    cv2.putText(tn, artist, artistXY, font, artistScale, black, 2)
    cv2.putText(tn, artist, artistXY, font, artistScale, white, 1)

    cv2.putText(tn, title, titleXY, font, titleScale, black, 4)
    cv2.putText(tn, title, titleXY, font, titleScale, white, 2)

    cv2.putText(tn, player, playerXY, font, 2.4, black, 3)
    cv2.putText(tn, player, playerXY, font, 2.4, white, 1)

    cv2.putText(tn, diffname, diffXY, font, 1.8, black, 3)
    cv2.putText(tn, diffname, diffXY, font, 1.8, white, 1)

    # showing the image
    cv2.imshow('thumbnail', tn)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # saving the image
    try:
        mkdir('thumbnails')
    except FileExistsError:
        pass
    cv2.imwrite(f'thumbnails/{artist} - {title} {diffname} ({player}).jpg', tn)
    print(f'thumbnail saved as: {artist} - {title} {diffname} ({player}).jpg')

# testing purposes
# editThumbnail('temp/cover.jpg', 'imprecial dead bicycle lol', 'thats a really long title for a song', 'what', '[Big Gay]', 'temp/player_avatar.jpg')