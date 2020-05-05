from pytesseract import image_to_string
class Recognizer(object):
    def getArtist(self, cropped_img):
        data = image_to_string(cropped_img)
        data = data.split(' - ')
        return data[0]

    def getTitle(self, cropped_img):
        data = image_to_string(cropped_img)
        data = data.split(' - ')
        return data[1].split(' [')[0]

    def getMapper(self, cropped_img):
        data = image_to_string(cropped_img)
        data = data.split('\n')
        return data[1].split('y ')[1]

    def getPlayer(self, cropped_img):
        data = image_to_string(cropped_img)
        data = data.split('\n')
        try:
            return data[3].split('y ')[1].split(' on')[0]
        except IndexError:
            return data[2].split('y ')[1].split(' on')[0]