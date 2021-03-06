#
# (c) 2016 -- onwards Georgios Gousios <gousiosg@gmail.com>
#

import pandas as pd
import time
import os

## Files
ORIG_DATA_URL = "https://dl.dropboxusercontent.com/u/57978013/data.csv"
ORIG_DATA_FILE = "pr-data.csv"
DIFFS_DATA_URL = "http://dutihr.st.ewi.tudelft.nl/downloads/pullreq-diffs.tar.gz"
DIFFS_DIR = "pullreq-patches"
TXTS_DIR = "pullreq-txts"
DIFFS_FILE = "pullreq-patches.tar.gz"
DATASETS_DIR = "datasets"
CHECKPOINT_DIR = "checkpoints"
CSV_DIR = "csvs"

pd.set_option('display.max_rows', 10)

if not os.path.exists(DATASETS_DIR):
    os.makedirs(DATASETS_DIR)

if not os.path.exists(CHECKPOINT_DIR):
    os.makedirs(CHECKPOINT_DIR)

train_csv_file = os.path.join(CSV_DIR, 'train_%s.csv')
test_csv_file = os.path.join(CSV_DIR, 'test_%s.csv')
validation_csv_file = os.path.join(CSV_DIR, 'validation_%s.csv')

diff_train_file = os.path.join(DATASETS_DIR, 'diff_train_%s.pcl')
comment_train_file = os.path.join(DATASETS_DIR, 'comment_train_%s.pcl')
title_train_file = os.path.join(DATASETS_DIR, 'title_train_%s.pcl')
y_train_file = os.path.join(DATASETS_DIR, 'y_train_%s.pcl')

diff_val_file = os.path.join(DATASETS_DIR, 'diff_val_%s.pcl')
comment_val_file = os.path.join(DATASETS_DIR, 'comment_val_%s.pcl')
title_val_file = os.path.join(DATASETS_DIR, 'title_val_%s.pcl')
y_val_file = os.path.join(DATASETS_DIR, 'y_val_%s.pcl')

diff_test_file = os.path.join(DATASETS_DIR, 'diff_test_%s.pcl')
comment_test_file = os.path.join(DATASETS_DIR, 'comment_test_%s.pcl')
title_test_file = os.path.join(DATASETS_DIR, 'title_test_%s.pcl')
y_test_file = os.path.join(DATASETS_DIR, 'y_test_%s.pcl')

config_file = os.path.join(DATASETS_DIR, 'config_%s.pcl')
checkpoint_file_1 = os.path.join(CHECKPOINT_DIR, 'checkpoint_%s_model2.{epoch:02d}-{val_loss:.2f}.hdf5')
checkpoint_file_2 = os.path.join(CHECKPOINT_DIR, 'checkpoint_%s_model2.{epoch:02d}-{val_loss:.2f}.hdf5')

diff_vocab_file = os.path.join(DATASETS_DIR, 'diff_vocab_%s.pcl')
comment_vocab_file = os.path.join(DATASETS_DIR, 'comment_vocab_%s.pcl')
title_vocab_file = os.path.join(DATASETS_DIR, 'title_vocab_%s.pcl')


def timeit(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print 'func:%r took: %2.4f sec' % \
              (f.__name__, te - ts)
        return result

    return timed
