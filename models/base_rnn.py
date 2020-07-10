"""
Created on Tue Jun 23 20:15:11 2020

@author: sarroutim2
"""


""" A base class for RNN. """

import torch.nn as nn


class BaseRNN(nn.Module):
    """Applies a multi-layer RNN to an input sequence.

    Note:
        Do not use this class directly, use one of the sub classes.

    Inputs: ``*args``, ``**kwargs``
        - ``*args``: variable length argument list.
        - ``**kwargs``: arbitrary keyword arguments.

    Attributes:
        SYM_MASK: masking symbol
        SYM_EOS: end-of-sequence symbol
    """
    SYM_MASK = "MASK"
    SYM_EOS = "EOS"

    def __init__(self, vocab_size, max_len, hidden_size, input_dropout_p,
                 dropout_p, n_layers, rnn_cell):
        """Constructor for BaseRNN.
        Args:
            vocab_size (int): size of the vocabulary
            max_len (int): maximum allowed length for the sequence to be processed
            hidden_size (int): number of features in the hidden state `h`
            input_dropout_p (float): dropout probability for the input sequence
            dropout_p (float): dropout probability for the output sequence
            n_layers (int): number of recurrent layers
            rnn_cell (str): type of RNN cell (Eg. 'LSTM' , 'GRU')
        """
        super(BaseRNN, self).__init__()
        self.vocab_size = vocab_size
        self.max_len = max_len
        self.hidden_size = hidden_size
        self.n_layers = n_layers
        self.input_dropout_p = input_dropout_p
        self.input_dropout = nn.Dropout(p=input_dropout_p)
        self.rnn_cell = getattr(nn, rnn_cell.upper())
        self.dropout_p = dropout_p

    def forward(self, *args, **kwargs):
        raise NotImplementedError()
