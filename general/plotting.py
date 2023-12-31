import matplotlib.pyplot as plt
import numpy as np
import scipy
import sys
import os
from general.utils import *

sys.path.append("./")
from general.utils import k_fold, pca


def hist(d, l, labels):
    for i in range(d.shape[0]):
        plt.figure()
        for c in range(2):
            x = d[i, l == c]
            plt.hist(x.reshape(x.size, ), alpha=0.4, label=labels[c], bins=70, density=True, linewidth=1.0)
        plt.xlabel(f'Dimension {i + 1}')
        plt.legend()
        plt.savefig("figures/histograms/histograms_" + str(i))
        plt.close()


def plot_pca(d):
    s = pca(d, d.shape[0] + 1, eigen_values=True)
    sort_s = s[::-1]
    var = np.sum(sort_s)
    evr = np.cumsum(sort_s / var)
    plt.plot(range(1, s.size + 1), evr, marker='o')
    plt.xlabel('Dimensions')
    plt.ylabel('Fraction of explained variance')
    plt.savefig("figures/pca_var.png")
    plt.close()


def plot_heatmaps(d, l, labels):
    classes = [0, 1, None]
    colors = ["Blues", "hot", "Greys"]
    for c in range(3):
        if classes[c] is None:
            data = d
        else:
            data = d[:, l == classes[c]]
        heatmap = np.zeros((d.shape[0], d.shape[0]))

        for i in range(data.shape[0]):
            for j in range(data.shape[0]):
                heatmap[i, j] = abs(scipy.stats.pearsonr(data[i, :], data[j, :])[0])
                heatmap[j, i] = heatmap[i, j]
        plt.figure()
        plt.xticks(np.arange(0, data.shape[0]), np.arange(1, data.shape[0] + 1))
        plt.yticks(np.arange(0, data.shape[0]), np.arange(1, data.shape[0] + 1))
        plt.imshow(heatmap, cmap=colors[c])
        plt.colorbar()
        plt.savefig("figures/heatmaps/heatmaps_" + labels[c])
        plt.close()


def scatter_2d(d, l, labels):
    for i in range(d.shape[0]):
        for j in range(d.shape[0]):
            if i != j:
                plt.figure()
                for c in range(2):
                    d_c = d[:, l == c]
                    x1 = d_c[i, :]
                    x2 = d_c[j, :]
                    plt.scatter(x1, x2, label=labels[c])
                plt.xlabel(f'Dimension {i}')
                plt.ylabel(f'Dimension {j}')
                plt.legend()
                plt.savefig("figures/scatter_plots/scatter_plot_" + str(i)+"_"+str(j))
                plt.close()

def plot_min_dcfs_svm(min_dcf_list, description, values, pt=None):
    label = "C"
    folder = "SVM"
    e = [0.5, 0.1, 0.9]
    # e = [0.001, 0.01, 0.1]
    # e = [0.1, 1, 10]
    for i in range(len(min_dcf_list)):
        plt.plot(values, min_dcf_list[i], label=f"prior={e[i]}")
    plt.xscale("log")
    plt.xlabel(label)
    plt.ylabel("minDCF")
    plt.xlim([values[0], values[-1]])
    plt.ylim([0, 1])
    plt.legend()
    plt.savefig(f"figures/{folder}/{description}_pt_{pt}")
    plt.close()

    # # svm mie
    # min_dcf_list = [
    #     [
    #         0.34503968253968254,
    #         0.19523809523809524,
    #         0.1523809523809524,
    #         0.135515873015873,
    #         0.12658730158730158,
    #         0.12083333333333333,
    #         0.11865079365079365,
    #         0.11805555555555555,
    #         0.12023809523809524,
    #         0.11825396825396825,
    #         0.11865079365079365,
    #         0.11845238095238095,
    #         0.11904761904761904,
    #         0.11865079365079365,
    #         0.11964285714285713,
    #         0.12123015873015873,
    #         0.12123015873015874,
    #         0.12222222222222222,
    #         0.13134920634920635,
    #         0.2642857142857143,
    #         0.16865079365079366,
    #         0.4876984126984127,
    #         0.43154761904761907,
    #         0.5928571428571429,
    #         0.5259920634920635,
    #         0.6672619047619047,
    #         0.6557539682539683,
    #         0.709920634920635,
    #         0.602579365079365,
    #         0.6136904761904762,
    #         0.6017857142857143
    #     ],
    #     [
    #         0.661904761904762,
    #         0.4172619047619048,
    #         0.3494047619047619,
    #         0.3482142857142857,
    #         0.3202380952380952,
    #         0.3047619047619048,
    #         0.29523809523809524,
    #         0.30357142857142855,
    #         0.2922619047619048,
    #         0.30952380952380953,
    #         0.305952380952381,
    #         0.29642857142857143,
    #         0.2988095238095238,
    #         0.2946428571428571,
    #         0.29166666666666663,
    #         0.3,
    #         0.2994047619047619,
    #         0.3071428571428571,
    #         0.31785714285714284,
    #         0.43988095238095243,
    #         0.36607142857142855,
    #         0.8863095238095239,
    #         0.9666666666666668,
    #         0.9988095238095238,
    #         0.9636904761904761,
    #         0.9583333333333334,
    #         0.9940476190476191,
    #         0.993452380952381,
    #         0.9952380952380953,
    #         0.8845238095238096,
    #         0.9976190476190477
    #     ],
    #     [
    #         0.6712301587301588,
    #         0.6005952380952381,
    #         0.49940476190476196,
    #         0.44305555555555554,
    #         0.40436507936507937,
    #         0.3567460317460318,
    #         0.33968253968253975,
    #         0.35039682539682543,
    #         0.34722222222222227,
    #         0.3380952380952381,
    #         0.34186507936507937,
    #         0.343452380952381,
    #         0.339484126984127,
    #         0.3400793650793651,
    #         0.34246031746031746,
    #         0.3492063492063493,
    #         0.341468253968254,
    #         0.3464285714285714,
    #         0.3890873015873016,
    #         0.9496031746031746,
    #         0.44325396825396834,
    #         0.9734126984126985,
    #         0.9763888888888888,
    #         0.9589285714285714,
    #         0.8890873015873016,
    #         0.9444444444444443,
    #         0.9952380952380953,
    #         0.9970238095238096,
    #         0.9720238095238096,
    #         0.9972222222222222,
    #         0.9958333333333333
    #     ]
    #
    # ]
    # # svm_leo_giulia
    # min_dcf = [
    #     [
    #         0.34503968253968254,
    #         0.19523809523809524,
    #         0.1523809523809524,
    #         0.135515873015873,
    #         0.12658730158730158,
    #         0.12083333333333333,
    #         0.11865079365079365,
    #         0.11865079365079365,
    #         0.12023809523809524,
    #         0.11825396825396825,
    #         0.11865079365079365,
    #         0.11845238095238095,
    #         0.11904761904761904,
    #         0.11865079365079365,
    #         0.11964285714285713,
    #         0.12142857142857143,
    #         0.11944444444444445,
    #         0.12043650793650792,
    #         0.13115079365079363,
    #         0.1349206349206349,
    #         0.19702380952380952,
    #         0.4291666666666667,
    #         0.40436507936507937,
    #         0.6021825396825397,
    #         0.5337301587301587,
    #         0.7021825396825396,
    #         0.6196428571428572,
    #         0.7186507936507937,
    #         0.602579365079365,
    #         0.6136904761904762,
    #         0.6017857142857143
    #     ],
    #     [
    #         0.661904761904762,
    #         0.4172619047619048,
    #         0.3494047619047619,
    #         0.3482142857142857,
    #         0.3202380952380952,
    #         0.30654761904761907,
    #         0.29523809523809524,
    #         0.30357142857142855,
    #         0.2922619047619048,
    #         0.30952380952380953,
    #         0.305952380952381,
    #         0.29642857142857143,
    #         0.2988095238095238,
    #         0.2946428571428571,
    #         0.2898809523809524,
    #         0.3,
    #         0.2910714285714286,
    #         0.2904761904761905,
    #         0.33988095238095234,
    #         0.33214285714285713,
    #         0.4125,
    #         0.8529761904761904,
    #         0.9666666666666668,
    #         0.8404761904761905,
    #         1.0,
    #         0.9726190476190477,
    #         0.9940476190476191,
    #         0.9755952380952382,
    #         0.9952380952380953,
    #         0.8845238095238096,
    #         0.9976190476190477
    #     ], [
    #         0.6712301587301588,
    #         0.6005952380952381,
    #         0.49940476190476196,
    #         0.44305555555555554,
    #         0.40436507936507937,
    #         0.3567460317460318,
    #         0.33968253968253975,
    #         0.35039682539682543,
    #         0.34722222222222227,
    #         0.3380952380952381,
    #         0.34186507936507937,
    #         0.343452380952381,
    #         0.339484126984127,
    #         0.3400793650793651,
    #         0.34246031746031746,
    #         0.34722222222222227,
    #         0.351984126984127,
    #         0.3452380952380953,
    #         0.39900793650793653,
    #         0.36884920634920637,
    #         0.6132936507936508,
    #         0.7188492063492063,
    #         0.9763888888888888,
    #         0.950595238095238,
    #         0.9972222222222222,
    #         0.9914682539682541,
    #         0.9952380952380953,
    #         0.946031746031746,
    #         0.9720238095238096,
    #         0.9972222222222222,
    #         0.9958333333333333
    #     ]
    # ]


def plot_bayes_error(scores, ltr, cfn, cfp, model_desc):
    effPriorLogOdds = np.linspace(-4, 4, 31)
    k = 0
    dcf = []
    mindcf = []
    for e in effPriorLogOdds:
        print(k)
        k += 1
        # CALCOLO DCF EFFETTIVO
        pi = 1 / (1 + np.exp(-e))
        th = -np.log(pi / (1 - pi))
        PL = predict_labels(scores, th)
        conf_matrix = get_confusion_matrix(PL, ltr, 2)
        dcf.append(compute_dcf(conf_matrix, cfn, cfp, pi))
        mindcf.append(compute_min_dcf(scores, ltr, pi, cfn, cfp))

    plt.figure()
    plt.plot(effPriorLogOdds, dcf, label="actDCF", color="r")
    plt.plot(effPriorLogOdds, mindcf, label="minDCF", color="b")
    plt.ylim([0, 1])
    plt.xlim([-4, 4])
    plt.legend()
    if not os.path.exists("calibration_plots"):
        os.makedirs("calibration_plots")
    plt.savefig(f"calibration_plots/{model_desc}")
    plt.show()

