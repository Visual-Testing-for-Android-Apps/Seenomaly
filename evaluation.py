import os
import pickle
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
import argparse
import constants

typical_list = [2]
K_list = [2]
class_num = 9
spc = 25
add_normal = 1

def evaluate(typical, K, save_dir, log_file):
  images, pca_features, labels = pickle.load(open(os.path.join(save_dir, 'features.p'), 'rb'))
  count = 0
  i = 0
  x_train = []
  x_test = []
  y_train = []
  y_test = []
  for image, feature, label in list(zip(images, pca_features, labels)):
    if count < spc * class_num:
      if i > spc:
        i = 0
      if i < typical:
        x_train.append(feature)
        y_train.append(label)
      else:
        x_test.append(feature)
        y_test.append(label)

    elif add_normal:
      if count < (spc + typical) * class_num:
        x_train.append(feature)
        y_train.append(label)
      else:
        x_test.append(feature)
        y_test.append(label)
    
    i += 1
    count += 1
  neigh = KNeighborsClassifier(n_neighbors=K)
  neigh.fit(x_train, y_train)
  score = neigh.score(x_test, y_test)
  y_pred = neigh.predict(x_test)
  conf_matrix = confusion_matrix(y_test, y_pred)
  report = classification_report(y_test, y_pred) 
  f = open(log_file, 'a')
  #print ('{}-NN, {} typical exampls, accuracy:{}'.format(K, typical, score))
  #print (conf_matrix)
  #print (report)
  #print ('***********************************')
  print ('{}-NN, {} typical exampls, accuracy:{}'.format(K, typical, score), file = f)
  print (conf_matrix, file = f)
  print (report, file = f)
  print ('***********************************', file = f)
  return score

def main(net_name, save_dir, log_file, result_file):
  score_list = []
  log_dir = os.path.join(constants.DATA_PATH, 'results', net_name)
  if not os.path.exists(log_dir):
    os.makedirs(log_dir) 
  r = open(result_file, 'a')
  time_list = []
  for T in typical_list:
    k_score = []
    k_time = []
    for k in K_list:
      start_time = time.time()
      k_score.append(evaluate(T, k, save_dir, log_file))
      k_time.append(time.time() - start_time)
      print ("Time: ", time.time() - start_time)
    score_list.append(k_score)
    time_list.append(sum(k_time) / len(K_list))
  print ('real', file = r)
  print (score_list, file = r)
  #print (time_list, file = r)
  print ("Score list: ", score_list)

  #fig = plt.figure()
  #plt.xlabel('K', fontsize = 20)
  #plt.ylabel('Accuracy', fontsize = 20)
  #x = range(len(score_list[0]))
  #for i in range(len(score_list)):
  #  plt.plot(x, score_list[i], label = str(typical_list[i]))
  #plt.xticks(fontsize = 20)
  #plt.yticks(fontsize = 20)
  #plt.legend(fontsize = 10)
  #plt.show()
      
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description = "Evaluate the model")
  parser.add_argument("-n", "--netName", help="chooses the network type to be used", choices= ("gan", "vae", "vaegan", "aernn"), default="gan")

  args = parser.parse_args()

  save_dir = os.path.join(constants.DATA_PATH, 'features', 'real', args.netName)
  log_file = os.path.join(constants.DATA_PATH, 'results', args.netName, 'real.txt')
  result_file = os.path.join(constants.DATA_PATH, 'results', args.netName, 'result.txt')

  main(args.netName, save_dir, log_file, result_file)
