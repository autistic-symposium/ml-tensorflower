#!/usr/bin/env python 

""" Create dream """ 

IMAGE_TO_DREAM = "saturn.jpg"
IMAGE_TO_DREAM_OUTPUT = "dream.jpg"

bc = BatCountry(IMAGE_TO_DREAM)
image = bc.dream(np.float32(Image.open())
bc.cleanup()
result = Image.fromarray(np.uint8(image))

result.save(IMAGE_TO_DREAM_OUTPUT)