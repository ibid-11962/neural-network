# neural-network-

These two Python programs to train and test a neural network with one hidden layer, and using a sigmoid activation function and back propagation.

# train.py

When you run this program it will prompt you for five things

- name of the file with the initial nueral network weights
- name of the training set file
- name of the output file
- number of epochs to run
- learning rate to use

The initial weights file must be formatted as follows:

- The first line contains three integers separated by spaces, reprsenting the number of input nodes (N_i), the number of hidden nodes (N_h), and the number of output nodes.
- The next N_h lines contain the weights from the input nodes to the hidden nodes, with one line for each hidden node. The weights are floating point numbers seperated by spaces. Each line containes N_i+1 weights, one for each input node and one bias weight from a fixed -1 input.
- The next N_o lines have the weights from the hidden nodes to the output nodes, one line for each output node with N_h+1 weights per line.

The training set file must be formated as follows:

- The first line contains three intergers separated by spaces, reprsenting the number of training examples, N_i, and N_o.
- Every other line represents a single example and contains N_i floating point inputs followed by N_o boolean outputs.

The output will be a trained neural network in the same format as the initial one.

# test.py

When you run this program it will prompt you for three things

- name of the trained nueral network
- name of the test set file
- name of the output results file

The neural network and test set files must use the same format described above.

The output results file will be formatted as follows

- The first N_o lines each correspond to a single output node and specify its (1) Overall accuracy, (2) Precision, (3) Recall, and (4) F1
- The last two lines contain the same four values computed for the micro-averaged metrics macro-averaged metrics, respectively.
