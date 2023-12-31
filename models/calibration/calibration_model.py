import numpy

from models.logistic_regression.log_reg_training_models import LR
from general.utils import k_fold


def calibrate_scores(scores, l, prior, model_desc):
    return k_fold(scores, l, 5, LR(0, prior), p=prior, seed=27, model_desc=model_desc, calibration=True)


def fusion(scores_list, l, prior, model_desc):
    d = numpy.vstack(scores_list)
    return k_fold(d, l, 5, LR(0, prior), p=prior, seed=27, model_desc=model_desc)
