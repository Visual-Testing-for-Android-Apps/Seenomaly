import os
import argparse
import constants
import extract_features

import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

import math
import functools
import operator

def printExit(out):
    print(out)
    exit()

def evaluate(modelDir, toCompare):
    """
    Model should be saved and loaded from disk, so the neighbour classification cost isn't incurred each run

    neigh.fit(x_train, y_train)
    pickle.dump(neigh, open(filename, 'wb'))
    
    # load from disk
    neigh = pickle.load(open(filename, 'rb'))
    result = neigh.score(X_test, Y_test)
    """
    x_train = []
    y_train = []

    testList = []

    images, pca_features, labels = pickle.load(open(os.path.join(modelDir, 'features.p'), 'rb'))
    for image, feature, label in list(zip(images, pca_features, labels)):
        #print("Image: {}, Feature: {}, Label: {}".format(image, feature, label))
        #print("Image: {}, Label: {}".format(image, label))
        #dist = math.sqrt(functools.reduce(operator.add, [pow(feature[j] - toCompare[0][j], 2) for j in range(len(toCompare[0]))]))
        #print("Distsance: {}", dist)
        #testList.append((dist, image))
        label = int(label)

        x_train.append(feature)
        y_train.append(label)
    K = 2
    neigh = KNeighborsClassifier(n_neighbors=K)
    neigh.fit(x_train, y_train)
    yPred = neigh.predict(toCompare)
    print(neigh.score(toCompare, [4]))
    #testList.sort()
    #print(testList)
    return yPred[0]

def main(args, modelDir):
    logitsName = "gan/generator/encoder/fc6"
    ckPath = os.path.join(constants.ROOT_PATH, "Seenomaly", "models", args.netName, f"model.ckpt-{args.checkpoint}")
    imagePaths = [os.path.join(constants.DATA_PATH,"custom","label.txt")]
    saveDir = os.path.join(constants.DATA_PATH,"custom")
    gifFiles, pcaFeatures, labels = extract_features.extract_features(args.netName, ckPath, False, logitsName, imagePaths, modelDir)

    resultString = [
        "Unknown",
        "Pass through other material",
        "Lack of scrimmed background",
        "Snackbar blocks bottom app bar",
        "Stack multiple banners",
        "Flip card to reveal information",
        "Move one card behind other card",
        "Stack multiple snackbars",
        "Lack of shadow",
        "Invisible scrime of modal bottom sheet",
    ]

    pred = evaluate(modelDir, pcaFeatures)
    print("Prediciton: {}".format(pred))
    print("Result: {}".format(resultString[pred]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Process a file through the model")
    #parser.add_argument("file", nargs='?', help="file to be processed", default=None)
    parser.add_argument("-o", "--out", help="overwrites the default output name (format is automatically added). Default is ./data/results/result", default=os.path.join(constants.DATA_PATH, "results", "result"))
    parser.add_argument("-n", "--netName", help="chooses the network type to be used, default is gan", choices= ("gan", "vae", "vaegan", "aernn"), default="gan")
    parser.add_argument("-c", "--checkpoint", help="sets the checkpoint number, default is 29471", type=int, default=29471)

    args = parser.parse_args()

    # Verification
    #if args.file == None: printExit("File must be present, use --help for more information.")

    modelDir = os.path.join(constants.DATA_PATH, 'features', 'real', args.netName)
    main(args, modelDir)
