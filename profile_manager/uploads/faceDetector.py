#This module is to process a picture and draw rectangle for each identified face.

def getRectangle(faceDictionary):
    rect = faceDictionary['faceRectangle']
    left = rect['left']
    top = rect['top']
    bottom = left + rect['height']
    right = top + rect['width']
    return ((left, top), (bottom, right))
def draw_face(img):
    import requests
    from io import BytesIO
    from PIL import Image, ImageDraw
    #Convert width height to a point in a rectangle

    subscription_key = '7532d57c84d447a9adf222de78fe71a3'  # Replace with a valid subscription key (keeping the quotes in place).

    BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'  # Replace with your regional Base URL
    headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',   # this should be the content type
    'Ocp-Apim-Subscription-Key': subscription_key,
    }


 
    response = requests.post(BASE_URL,  headers=headers, data=img)
        
    faces = response.json()



    output_image = Image.open(BytesIO(img))

    #For each face returned use the face rectangle and draw a red box.
    draw = ImageDraw.Draw(output_image)
    for face in faces:
        draw.rectangle(getRectangle(face), outline='red')

    return len(faces),output_image
def photo_verify(img1, img2):
    import requests
    from io import BytesIO
    from PIL import Image, ImageDraw
    #Convert width height to a point in a rectangle

    subscription_key = '7532d57c84d447a9adf222de78fe71a3'  # Replace with a valid subscription key (keeping the quotes in place).

    DETECT_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'  # Replace with your regional Base URL
    VERIFY_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/verify'  # Replace with your regional Base URL

    headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',   # this should be the content type
    'Ocp-Apim-Subscription-Key': subscription_key,
    }

    headers_verify = {
    # Request headers
        'Content-Type': 'application/json',   # this should be the content type

    'Ocp-Apim-Subscription-Key': subscription_key,
    }


 
    response1 = requests.post(DETECT_URL,  headers=headers, data=img1)
    face_1 =response1.json()[0] #assuming the first pic only has one face    
    face_id1 = face_1['faceId']
    response2 = requests.post(DETECT_URL,  headers=headers, data=img2)
    faces_2 =  response2.json()
    face_2=""
    match= False
    for face in faces_2:
        params = {
    'faceId1': face_id1,
    'faceId2': face['faceId']
     }
        if(requests.post(VERIFY_URL,  headers=headers_verify, json=params).json()['isIdentical']):
            face_2 = face
            break
    if face_2!="":match=True


    output_image1 = Image.open(BytesIO(img1))

    #For each face returned use the face rectangle and draw a red box.
    draw1 = ImageDraw.Draw(output_image1)
    draw1.rectangle(getRectangle(face_1), outline='red')
    output_image2 = Image.open(BytesIO(img2))

    if match:

            draw2 = ImageDraw.Draw(output_image2)
            draw2.rectangle(getRectangle(face_2), outline='red')



    return match, output_image1, output_image2

#Unit Test
#image_path_1 = "C:/Users/janguy/Pictures/Camera Roll/flowers.jpg"
#image_path_2 = "C:/Users/janguy/Pictures/Camera Roll/pic2.jpg"

#image_data_1 = open(image_path_1, "rb").read()
#image_data_2 = open(image_path_2, "rb").read()

#match, image1, image2 = photo_verify(image_data_2,image_data_1)
#print(match)
#image1.show()
#image2.show()






