from pytesseract import image_to_string

class Recognizer(object):
    def getArtist(self, cropped_img):
        data = image_to_string(cropped_img)
        data = data.split(' - ')
        try:
            return data[0]
        except IndexError:
            return 'FAILED TO RECOGNIZE'

    def getTitle(self, cropped_img):
        data = image_to_string(cropped_img)
        data = data.split(' - ')
        try:
            return data[1].split(' [')[0]
        except IndexError:
            return 'FAILED TO RECOGNIZE'

    def getMapper(self, cropped_img):
        data = image_to_string(cropped_img)
        data = data.split('\n')
        try:
            return data[1].split('y ')[1]
        except IndexError:
            return 'FAILED TO RECOGNIZE'

    def getPlayer(self, cropped_img):
        data = image_to_string(cropped_img)
        data = data.split('\n')
        try:
            return data[3].split('y ')[1].split(' on')[0]
        except IndexError:
            return 'FAILED TO RECOGNIZE'

    def getDiffName(self, cropped_img):
        data = image_to_string(cropped_img)
        try:
            data = data.split(' [')[1]
            return '[' + data.split(']')[0] + ']'
        except IndexError:
            return 'FAILED TO RECOGNIZE'