from tensorflow.python.tools import freeze_graph
from tensorflow.python.saved_model import tag_constants

import os
import argparse
import constants

def main(args, modelDir, outputDir):

    initializer_nodes = ""
    output_node_names = ""

    freeze_graph.freeze_graph(
        input_saved_model_dir = modelDir,
        output_graph = outputDir,
        saved_model_tags = tag_constants.SERVING,
        output_node_names = output_node_names,
        initializer_nodes = initializer_nodes,
        input_graph = None,
        input_saver = False,
        input_binary = False, 
        input_checkpoint = None,
        restore_op_name = None,
        filename_tensor_name = None,
        clear_devices = False,
        input_meta_graph = False
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Process a file through the model")
    parser.add_argument("-o", "--out", help="overwrites the default output name (format is automatically added). Default is ./data/results/result", default=os.path.join(constants.DATA_PATH, "results", "result"))
    parser.add_argument("-n", "--netName", help="chooses the network type to be used, default is gan", choices= ("gan", "vae", "vaegan", "aernn"), default="gan")
    parser.add_argument("-c", "--checkpoint", help="sets the checkpoint number, default is 29471", type=int, default=29471)

    args = parser.parse_args()

    #modelDir = os.path.join(constants.DATA_PATH, "features", "real", args.netName)
    #outputDir = os.path.join(constants.DATA_PATH, "features", "real", "frozen", args.netName)

    modelDir = os.path.join(constants.ROOT_PATH, "Seenomaly", "models", args.netName, f"model.ckpt-{args.checkpoint}")
    outputDir = os.path.join(constants.ROOT_PATH, "Seenomaly", "models", args.netName, "frozen", f"model.ckpt-{args.checkpoint}")

    main(args, modelDir, outputDir)