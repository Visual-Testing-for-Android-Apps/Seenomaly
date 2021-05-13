import use
import preprocess
import os

def handler(event, context):
    netName = "gan"
    checkpoint = 29471
    modelDir = os.path.join("models", netName)
    use.main(netName, checkpoint, modelDir, preprocess.fromJson(event))