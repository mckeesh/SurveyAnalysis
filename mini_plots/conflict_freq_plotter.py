import matplotlib.pyplot as plt
import os

def plotConflictFrequency():
    x = ['Every Day', 'A few times\na week', 'Once a week', 'A few times\na month', 'Once a month', 'A few times\na year', 'Once a year\nor less', 'Never']
    ys = [13, 73, 26, 72, 21, 16, 3, 2]
    valSums = sum(ys)
    y_percentages = [100*float(y)/valSums for y in ys]

    bars = plt.bar(range(len(x)), y_percentages)
    plt.xticks(range(len(x)), x)
    plt.yticks(range(0, 36, 5), ["%d%%" % n for n in range(0, 36, 5)])
    plt.xlabel('Merge Conflict Frequency', fontsize=14)
    plt.ylabel('Participants', fontsize=14)

    for bar in bars:
        bar.set_color('#b2abd2')

    fig = plt.figure(1)
    ax = fig.add_subplot(111)

    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(12) 

    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(12) 
        tick.label.set_rotation(45)
        tick.label.set_horizontalalignment("center")

    rects = ax.patches

    # Now make some labels
    labels = [("%.2f%%" % y_percentages[i]) for i in range(len(rects))]

    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2, height + 1, label, ha='center', va='bottom', size=12)

    ax.xaxis.set_tick_params(width=0, length=0, zorder=0)

    plt.tight_layout()
    ax.margins(0.03)
    axes = plt.gca()
    axes.set_ylim([0,max(y_percentages) + 5])
    # plt.show()
    savePlot(fig, '/conflict_frequency.pdf')

def savePlot(fig, path):
    full_dir_path = os.path.dirname(os.path.realpath(__file__))
    local_dir_path = "/".join(path.split("/")[:-1])
    fig.savefig(full_dir_path + path, bbox_inches='tight')

plotConflictFrequency()