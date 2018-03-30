#!/usr/bin/env python

"""
EnergyDataSimulationChallenge by Cambridge Energy Data Lab

"""

import pandas as pd
import matplotlib.pyplot as pl
import numpy as np
import os
import sklearn as sk

def import_csv_data():
	
	df_train=pd.read_csv('../../data/training_dataset_500.csv')
	df_test=pd.read_csv('../../data/test_dataset_500.csv')

	return df_train,df_test


def MAPE(predictions,target):
	''' Find the mean absolute percentage error '''
    predictions,target=np.array(predictions),np.array(target)
	return np.mean((np.absolute(predictions-target)/target)*100)


def main():
	


if __name__ == "__main__":
	main()


