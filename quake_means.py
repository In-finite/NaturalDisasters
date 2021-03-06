import warnings
warnings.filterwarnings("ignore")

import time
import datetime as dt
import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.cluster import KMeans
from sklearn import datasets

def get_data_clusters(loc_df, num_clusters):
	clf_km = KMeans(n_clusters=num_clusters).fit(loc_df)
	unique_clusters = {i: np.where(clf_km.labels_ == i)[0] for i in range(clf_km.n_clusters)}
	return unique_clusters

def get_info_index(loc_df, main_df, num_clusters):
	quake_zones = get_data_clusters(loc_df, num_clusters)
	q_vals = main_df.values
	q_z = {}
	for i, j in quake_zones.items():
		z_lls = []
		for v in list(j):
			s_ll = (q_vals[v][0], q_vals[v][2], q_vals[v][3], q_vals[v][21], q_vals[v][8], q_vals[v][5])
			z_lls.append(s_ll)
		q_z[i] = z_lls
	return q_z

def segregation_llmd(r_list):
	daty = []; laty = []; lony = []; placy = []; magy = []; depthy = []
	for llmd in r_list:
		daty.append(llmd[0])
		laty.append(llmd[1])
		lony.append(llmd[2])
		placy.append(llmd[3])
		magy.append(llmd[4])
		depthy.append(llmd[5])
	return daty, laty, lony, placy, magy, depthy

def inside_place_wise(place_in):
	aplace_in = []
	for pi in place_in:
		fpi = pi.split(', ')
		aplace_in.append(fpi[0])

	cplace_in = {}
	uplace_in = list(set(aplace_in))
	for pi in uplace_in:
		cplace_in[pi] = aplace_in.count(pi)

	reverse_p = sorted(cplace_in.items(), key=lambda x : x[1], reverse=True)
	in_places = [str(pi[0]) + ' -- ' + str(pi[1]) for pi in reverse_p]
	in_places.insert(0, 'All')
	return in_places
